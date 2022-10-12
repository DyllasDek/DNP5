import sys
import grpc
import random
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2

address, m = sys.argv[1], sys.argv[2]
max_size = 2 ** m
chord = {}


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


def populate_finger_table(node_id):
    finger_table = []

    def find(entry):
        for id in sorted(chord.keys()):
            if entry <= id:
                return id
    for i in range(1, m+1):
        node = find((node_id+2**(i-1)) % max_size)
        finger_table.append(chord[node])
    return finger_table


class Handler(pb2_grpc.SimpleServiceServicer):
    def GetReverseResponse(self, request, context):
        return pb2.ReverseResponse(message='%s' % request.input[::-1])

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


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SimpleServiceServicer_to_server(Handler(), server)
    server.add_insecure_port("localhost:"+port)
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutdowned xD")
