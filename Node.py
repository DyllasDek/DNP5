import sys
import grpc
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2
from concurrent import futures
import zlib

args = sys.argv
server_address, listen_address = args[1], args[2]

channel = grpc.insecure_channel(server_address)
reg_stub = pb2_grpc.SimpleServiceStub(channel)
ip, port = listen_address.split(":")

nodeid = -1
max_size = -1
predecessor = None
data = {}
finger_table = {}


def hash(key):
    hash_value = zlib.adler32(key.encode())
    target_id = hash_value % 2 ** max_size
    return target_id


def find(key):
    id = hash(key)
    if (predecessor[0] < id <= nodeid):
        return True, (nodeid, listen_address)
    succ = reg_stub.GetSuccessor(nodeid)
    if (nodeid < id <= succ.nodeId):
        return True, (succ.nodeId, succ.address)
    keys = sorted(list(finger_table))
    for i in range(len(keys)):
        if (keys[i] >= id):
            ch = grpc.insecure_channel(finger_table[keys[i-1]])
            f_stub = pb2_grpc.SimpleServiceStub(channel)
            reply, _ = f_stub.Find(pb2.RemFiKey(key=key))
            reply = reply.split("||", 1)
            return True, (reply[0], reply[1])
    return False, "No key result"


def save(key, text):
    ack, result = find(key)
    if (ack):
        send_channel = grpc.insecure_channel(result[1])
        send_stub = pb2_grpc.SimpleServiceStub(send_channel)
        result = send_stub.Save(pb2.SaveKey(key=key, text=text))
        if (result.success):
            print(result.reply)
            return (True, id)
        else:
            print(result.reply)
            return (False, result.reply)
    else:
        return (False, result)


def remove(key):
    ack, result = find(key)
    if (ack):
        send_channel = grpc.insecure_channel(result[1])
        send_stub = pb2_grpc.SimpleServiceStub(send_channel)
        result = send_stub.Remove(pb2.RemFiKey(key=key))
        if (result.success):
            print(result.reply)
            return (True, id)
        else:
            print(result.reply)
            return (False, result.reply)
    else:
        return (False, result)


def get_finger_table():
    print("norm1")
    result = reg_stub.GetFingerTable(pb2.NodeId(id=nodeid))
    print("norm2")
    message_table = result.pairs
    print("norm3")
    output_table = {}
    for message in message_table:
        output_table[message.nodeId] = message.address
    print("norm")
    output_table = sorted(output_table.keys())
    print(output_table)
    predecessor_message = result.id
    predecessor = predecessor_message.nodeId, predecessor_message.address
    return output_table, predecessor


def start():
    register_output = reg_stub.RegisterNode(pb2.NodeInit(ipaddr=ip, port=port))
    return register_output.id, register_output.m


def exit():
    reg_stub.DeregisterNode(pb2.NodeId(nodeid))


def GetKeys():
    return data.keys()


class Handler(pb2_grpc.SimpleServiceServicer):
    def GetType(self, request, context):
        return pb2.TypeReply(type="Node")

    def Find(self, request, context):
        flag, reply = find(request.key)
        msg = ""
        if flag:
            msg = f'{reply[0]}||{reply[1]}'
        else:
            msg = reply
        return pb2.SRFReply(reply=msg, success=flag)

    def FindKey(self, request, context):
        flag, reply = find(request.key)
        if reply[0] == nodeid:
            if request.key in data:
                return pb2.SRFReply(reply=f"{request.key} is saved in {nodeid}", success=True)
        else:
            ch = grpc.insecure_channel(reply[1])
            f_stub = pb2_grpc.SimpleServiceStub(channel)
            keys = f_stub.GetKeysText(pb2.GetInfo())
            if request.keys in keys:
                return pb2.SRFReply(reply=f"{request.key} is saved in {reply[0]}", success=True)
        return pb2.SRFReply(reply=f'{request.key} does not exist in node {reply[0]}', success=False)

    def Save(self, request, context):
        if (request.key in data):
            return pb2.SRFReply(reply=f"{request.key} already exists in node {nodeid}", success=False)
        data[request.key] = request.text
        return pb2.SRFReply(reply=f"{request.text} is saved in node {nodeid}", success=True)

    def Remove(self, request, context):
        if (request.key not in data):
            return pb2.SRFReply(reply=f"{request.key} does not exist in node {nodeid}", success=False)
        del data[request.key]
        return pb2.SRFReply(reply=f"{request.key} is removed from {nodeid}", success=True)

    def GetNode(self, request, context):
        print(finger_table)
        msg = []
        for key in finger_table:
            msg.append(f'{key}:   {finger_table[key]}')
        return pb2.GetNodeChordReply(id=nodeid, table=msg)

    def GetKeysText(self, request, context):
        msg = []
        k = GetKeys()
        for key in k:
            msg.append(key)
        return pb2.KeysTextReply(keys=msg)


if __name__ == "__main__":
    nodeid, max_size = start()
    finger_table, predecessor = get_finger_table()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SimpleServiceServicer_to_server(Handler(), server)
    server.add_insecure_port(listen_address)
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutdowned")
