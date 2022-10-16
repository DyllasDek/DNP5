import sys
import grpc
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2

channel = 0
stub = 0


def send_messages(val):
    for n in list(map(int, val)):
        req = pb2.PrimeMessage(
            num=n)
        yield req


def connect(ip):
    channel = grpc.insecure_channel(ip)
    stub = pb2_grpc.SimpleServiceStub(channel)
    server_type = stub.GetType(pb2.GetInfo())
    return stub, server_type.type


def NodeInfo():
    resp = stub.GetNode(pb2.GetInfo())
    print(resp)
    print(f'Node id: {resp.id}')
    print("Finger table:")

    for elem in resp.table:
        print(elem)


def ChordInfo():
    resp = stub.GetChord(pb2.GetInfo())
    print(resp)
    for elem in resp.table:
        print(elem)


if __name__ == "__main__":
    server_type = 0

    stub = None
    while True:
        response = 0
        try:
            line = input("> ")
            if len(line) != 0:
                line = line.split(' ', 1)

                if line[0] == "connect":
                    stub, server_type = connect(line[1])
                    print()
                    print(f'Connected to {server_type}')
                    continue

                if line[0] == "get_info":
                    if server_type == "Node":
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

        # except grpc.RpcError as rpc_error:
         #   if rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
          #      print("There is no registry/node on this address, try again.")
           # else:
            #    print("Something wrong with grpc, try again.")
            # pass
        # except:
         #   print("Something wrong, try again!")
          #  pass

print("Shutting down")
