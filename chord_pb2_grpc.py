# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chord_pb2 as chord__pb2


class SimpleServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetChord = channel.unary_stream(
                '/SimpleService/GetChord',
                request_serializer=chord__pb2.GetInfo.SerializeToString,
                response_deserializer=chord__pb2.GetNodeChordReply.FromString,
                )
        self.GetNode = channel.unary_unary(
                '/SimpleService/GetNode',
                request_serializer=chord__pb2.GetInfo.SerializeToString,
                response_deserializer=chord__pb2.GetNodeChordReply.FromString,
                )
        self.Save = channel.unary_unary(
                '/SimpleService/Save',
                request_serializer=chord__pb2.SaveKey.SerializeToString,
                response_deserializer=chord__pb2.SRFReply.FromString,
                )
        self.Remove = channel.unary_unary(
                '/SimpleService/Remove',
                request_serializer=chord__pb2.RemFiKey.SerializeToString,
                response_deserializer=chord__pb2.SRFReply.FromString,
                )
        self.Find = channel.unary_unary(
                '/SimpleService/Find',
                request_serializer=chord__pb2.RemFiKey.SerializeToString,
                response_deserializer=chord__pb2.SRFReply.FromString,
                )
        self.GetType = channel.unary_unary(
                '/SimpleService/GetType',
                request_serializer=chord__pb2.GetInfo.SerializeToString,
                response_deserializer=chord__pb2.TypeReply.FromString,
                )
        self.RegisterNode = channel.unary_unary(
                '/SimpleService/RegisterNode',
                request_serializer=chord__pb2.NodeInit.SerializeToString,
                response_deserializer=chord__pb2.NodeReply.FromString,
                )
        self.DeregisterNode = channel.unary_unary(
                '/SimpleService/DeregisterNode',
                request_serializer=chord__pb2.NodeId.SerializeToString,
                response_deserializer=chord__pb2.DeregReply.FromString,
                )
        self.GetFingerTable = channel.unary_unary(
                '/SimpleService/GetFingerTable',
                request_serializer=chord__pb2.NodeId.SerializeToString,
                response_deserializer=chord__pb2.FingerTable.FromString,
                )
        self.GetSuccessor = channel.unary_unary(
                '/SimpleService/GetSuccessor',
                request_serializer=chord__pb2.NodeId.SerializeToString,
                response_deserializer=chord__pb2.NodePair.FromString,
                )
        self.ReloadTable = channel.unary_unary(
                '/SimpleService/ReloadTable',
                request_serializer=chord__pb2.GetInfo.SerializeToString,
                response_deserializer=chord__pb2.GetInfo.FromString,
                )


class SimpleServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetChord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeregisterNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFingerTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSuccessor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReloadTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetChord': grpc.unary_stream_rpc_method_handler(
                    servicer.GetChord,
                    request_deserializer=chord__pb2.GetInfo.FromString,
                    response_serializer=chord__pb2.GetNodeChordReply.SerializeToString,
            ),
            'GetNode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNode,
                    request_deserializer=chord__pb2.GetInfo.FromString,
                    response_serializer=chord__pb2.GetNodeChordReply.SerializeToString,
            ),
            'Save': grpc.unary_unary_rpc_method_handler(
                    servicer.Save,
                    request_deserializer=chord__pb2.SaveKey.FromString,
                    response_serializer=chord__pb2.SRFReply.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=chord__pb2.RemFiKey.FromString,
                    response_serializer=chord__pb2.SRFReply.SerializeToString,
            ),
            'Find': grpc.unary_unary_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=chord__pb2.RemFiKey.FromString,
                    response_serializer=chord__pb2.SRFReply.SerializeToString,
            ),
            'GetType': grpc.unary_unary_rpc_method_handler(
                    servicer.GetType,
                    request_deserializer=chord__pb2.GetInfo.FromString,
                    response_serializer=chord__pb2.TypeReply.SerializeToString,
            ),
            'RegisterNode': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterNode,
                    request_deserializer=chord__pb2.NodeInit.FromString,
                    response_serializer=chord__pb2.NodeReply.SerializeToString,
            ),
            'DeregisterNode': grpc.unary_unary_rpc_method_handler(
                    servicer.DeregisterNode,
                    request_deserializer=chord__pb2.NodeId.FromString,
                    response_serializer=chord__pb2.DeregReply.SerializeToString,
            ),
            'GetFingerTable': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFingerTable,
                    request_deserializer=chord__pb2.NodeId.FromString,
                    response_serializer=chord__pb2.FingerTable.SerializeToString,
            ),
            'GetSuccessor': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSuccessor,
                    request_deserializer=chord__pb2.NodeId.FromString,
                    response_serializer=chord__pb2.NodePair.SerializeToString,
            ),
            'ReloadTable': grpc.unary_unary_rpc_method_handler(
                    servicer.ReloadTable,
                    request_deserializer=chord__pb2.GetInfo.FromString,
                    response_serializer=chord__pb2.GetInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SimpleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimpleService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetChord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/SimpleService/GetChord',
            chord__pb2.GetInfo.SerializeToString,
            chord__pb2.GetNodeChordReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/GetNode',
            chord__pb2.GetInfo.SerializeToString,
            chord__pb2.GetNodeChordReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Save(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/Save',
            chord__pb2.SaveKey.SerializeToString,
            chord__pb2.SRFReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/Remove',
            chord__pb2.RemFiKey.SerializeToString,
            chord__pb2.SRFReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/Find',
            chord__pb2.RemFiKey.SerializeToString,
            chord__pb2.SRFReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/GetType',
            chord__pb2.GetInfo.SerializeToString,
            chord__pb2.TypeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/RegisterNode',
            chord__pb2.NodeInit.SerializeToString,
            chord__pb2.NodeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeregisterNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/DeregisterNode',
            chord__pb2.NodeId.SerializeToString,
            chord__pb2.DeregReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFingerTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/GetFingerTable',
            chord__pb2.NodeId.SerializeToString,
            chord__pb2.FingerTable.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSuccessor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/GetSuccessor',
            chord__pb2.NodeId.SerializeToString,
            chord__pb2.NodePair.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReloadTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleService/ReloadTable',
            chord__pb2.GetInfo.SerializeToString,
            chord__pb2.GetInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
