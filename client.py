import sys
import grpc
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2


channel = 0
stub = 0
server_type = 0

channel = grpc.insecure_channel("1.1.1.1.1.1.")
stub = pb2_grpc.SimpleServiceStub(channel)


def send_messages(val):
    for n in list(map(int, val)):
        req = pb2.PrimeMessage(
            num=n)
        yield req


def connect(ip):
    channel = grpc.insecure_channel(ip)
    stub = pb2_grpc.SimpleServiceStub(channel)
    server_type = stub.GetType(pb2.GetInfo())
    return 'Connected to' + server_type


def NodeInfo():
    resp = stub.GetNode(pb2.GetInfo())
    print(f'Node id: {resp[0]}')
    print("Finger table:")
    for elem in resp[1:]:
        print(elem)


def ChordInfo():
    resp = stub.GetChord(pb2.GetInfo())
    for elem in resp:
        print(elem)


if __name__ == "__main__":
    while True:
        response = 0
        try:
            line = input("> ")
            if len(line) != 0:
                line = line.split(' ', 1)

                if line[0] == 'connect':
                    print(connect(line[1]))

                if line[0] == 'get_info':
                    if server_type == 'Node':
                        NodeInfo()
                    elif server_type == "Registry":
                        ChordInfo()
                    else:
                        print(
                            "You aren't connected, first of all connect to chord/node")

                if line[0] == 'save':
                    text = line[1].split(' ', 1)
                    key = text[0][1:-1]
                    msg = text[1]
                    response = stub.Save(
                        pb2.SaveKey(key=key, text=msg))

                if line[0] == 'find':
                    response = stub.Find(
                        pb2.RemFiKey(key=line[1])
                    )
                if line[0] == 'remove':
                    response = stub.Remove(
                        pb2.RemFiKey(key=line[1])
                    )
                if line[0] == 'exit':
                    break
                print(response)
        except KeyboardInterrupt:
            break

        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                print("There is no registry/node on this address, try again.")
            else:
                print("Something wrong with grpc, try again.")
            pass
        except:
            print("Something wrong, try again!")
            pass

print("Shutting down")
