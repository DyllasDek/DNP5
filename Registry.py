import sys
import grpc
import random
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2
from concurrent import futures

server_address, m = sys.argv[1], int(sys.argv[2])
max_size = 2 ** m
chord = {}


def parse_address(address):
    split_res = address.split(":")
    if len(split_res) == 1:  # we pass value only of the port
        return f"localhost:{address}"
    return address


def register(ipaddr, port):
    random.seed(0)
    if len(chord) == max_size:
        return -1, 'Chord is full'
    while True:
        node_id = random.randrange(max_size)
        if node_id not in chord:
            break
    chord[node_id] = f'{ipaddr}:{port}'
    return node_id, m


def deregister(node_id):
    try:
        chord.pop(node_id)
        return True, f'Node with id {node_id} successfully was deregistered'
    except KeyError:
        return False, 'No such id exists'


def get_chord_info():
    output = []
    for key in chord:
        output.append(f'{key}:   {chord[key]}')
    return output


def findSucc(entry):
    for id in sorted(chord.keys()):
        if entry <= id:
            return id


def findPred(entry):
    for id in reversed(sorted(chord.keys())):
        if entry >= id:
            return id


def populate_finger_table(node_id):
    finger_table = {}
    for i in range(1, m+1):
        node = findSucc((node_id+2**(i-1)) % max_size)
        finger_table[node] = chord[node]
    return finger_table


class Handler(pb2_grpc.SimpleServiceServicer):
    def RegisterNode(self, request, context):
        output = register(request.ipaddr, request.port)
        return pb2.NodeReply(id=output[0], m=output[1])

    def GetReverseResponse(self, request, context):
        return pb2.ReverseResponse(message='%s' % request.input[::-1])

    def GetFingerTable(self, request, context):
        table = populate_finger_table(request.id)
        out_pred = findPred(request.id)
        out_table = []
        for key in table:
            out_table.append(pb2.NodePair(nodeId=key, address=table[key]))
        print(out_table)
        return pb2.FingerTable(id=pb2.NodePair(nodeId=out_pred, address=chord[out_pred]), pairs=out_table)

    def GetSplitResponse(self, request, context):

        m_string = request.input.split(request.delim)
        num = len(m_string)
        response = {
            "number": num,
            "parts": m_string
        }
        return pb2.SplitResponse(**response)

    def GetPrimeResponse(self, request_iterator, context):
        for request in request_iterator:
            if is_prime(request.num):
                yield pb2.PrimeResponse(output='%s is prime ' % request.num)
            else:
                yield pb2.PrimeResponse(output='%s is not prime ' % request.num)

    def DeregisterNode(self, request, context):
        return super().DeregisterNode(request, context)


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SimpleServiceServicer_to_server(Handler(), server)
    server.add_insecure_port(parse_address(server_address))
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutdowned xD")
