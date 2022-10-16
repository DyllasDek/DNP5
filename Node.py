import sys
import grpc
import chord_pb2_grpc as pb2_grpc
import chord_pb2 as pb2
import zlib

args= sys.argv
server_address, listen_address= args[1], args[2]

data = None

channel = grpc.insecure_channel(server_address)
stub = pb2_grpc.SimpleServiceStub(channel)
ip,address=server_address.split(":")
nodeid=-1
max_size= -1
predessor = None

def hash(key):
    hash_value = zlib.adler32(key.encode())
    target_id = hash_value % 2 ** max_size
    return target_id

def save(key, text):
   ack, result= find(key)
   if(ack):
        id,address=result

        return (True, id)
   else:
        return (False, result)
    
def get_finger_table():
    result= stub.GetFingerTable(pb2.NodeId(id=nodeid))
    finger_table= result["pairs"]
    predessor= result["id"]

def get_successor_id():
    return None


def request_successor_data():

def find(key):
    id = hash(key)



def start():
    register_output= stub.RegisterNode(pb2.NodeInit(ipaddr= ip,port=address))
    nodeid, max_size=register_output["id"], register_output["m"]

def exit():
    stub.DeregisterNode(pb2.NodeId(nodeid))
    
        #def get_finger_table():

if __name__ == "__main__":    
    start()