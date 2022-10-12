import sys
import grpc
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2

args= sys.argv
server_address, listen_address= args[1], args[2]

data = None

channel = grpc.insecure_channel(server_address)
stub = pb2_grpc.SimpleServiceStub(channel)
ip,address=server_address.split(":")
nodeid=-1
def start():
    register_output= stub.RegisterNode(pb2.NodeInit(ipaddr= ip,port=address))
    nodeid=register_output["id"]



def exit():
    stub.DeregisterNode(pb2.NodeId(nodeid))
    
        #def get_finger_table():

if __name__ == "__main__":    
    start()