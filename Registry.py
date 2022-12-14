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
        return -1, 'Chord is full.'
    while True:
        node_id = random.randrange(max_size)
        if node_id not in chord:
            break
    chord[node_id] = f'{ipaddr}:{port}'
    for keys in chord:
        if node_id != keys:
            ch = grpc.insecure_channel(chord[keys])
            f_stub = pb2_grpc.SimpleServiceStub(ch)
            f_stub.ReloadTable(pb2.GetInfo())
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
        if entry < id:
            return id
    return entry


def findPred(entry):
    for id in reversed(sorted(chord.keys())):
        if entry > id:
            return id
    return entry


def find(entry):
    successor = entry
    for i in range(0, max_size):
        if (successor + i) % max_size in chord.keys():
            successor = (successor + i) % max_size
            break
    return successor


def populate_finger_table(node_id):
    finger_table = {}
    for i in range(1, m+1):
        try:
            node = find((node_id+2**(i-1)) % max_size)
            finger_table[node] = chord[node]
        except:
            continue
    return finger_table


class Handler(pb2_grpc.SimpleServiceServicer):
    def GetType(self, request, context):
        return pb2.TypeReply(type="Registry")

    def RegisterNode(self, request, context):
        output = register(request.ipaddr, request.port)
        for keys in chord:
            if keys != output[0]:
                ch = grpc.insecure_channel(chord[keys])
                f_stub = pb2_grpc.SimpleServiceStub(ch)
                f_stub.ReloadTable(pb2.GetInfo())
        return pb2.NodeReply(id=output[0], m=output[1])

    def GetReverseResponse(self, request, context):
        return pb2.ReverseResponse(message='%s' % request.input[::-1])

    def GetFingerTable(self, request, context):
        table = populate_finger_table(request.id)
        out_pred = findPred(request.id)
        msg = []
        for keys in table:
            msg.append(pb2.NodePair(nodeId=keys, address=chord[keys]))

        return pb2.FingerTable(id=pb2.NodePair(nodeId=out_pred, address=chord[out_pred]), pairs=msg)

    def GetSuccessor(self, request, context):
        succ_id = findSucc(request.id)
        succ_address = chord[succ_id]
        return pb2.NodePair(nodeId=succ_id, address=succ_address)

    def GetChord(self, request, context):
        msg = []
        for key in chord:
            msg.append(f'{key}:   {chord[key]}')
        return pb2.GetNodeChordReply(id=-1, table=msg)

    def DeregisterNode(self, request, context):
        try:
            deregister(request.id)
            for keys in chord:
                ch = grpc.insecure_channel(chord[keys])
                f_stub = pb2_grpc.SimpleServiceStub(ch)
                f_stub.ReloadTable(pb2.GetInfo())
            return pb2.DeregReply(ack=True, output="Done!")
        except:
            return pb2.DeregReply(ack=False, output="Already deleted")


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SimpleServiceServicer_to_server(Handler(), server)
    server.add_insecure_port(parse_address(server_address))
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutdowned registry.")
