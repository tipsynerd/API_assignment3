# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import service.inventorySystem_pb2 as inventorySystem__pb2


class InventoryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createBook = channel.unary_unary(
                '/service.inventorySystem.Inventory/createBook',
                request_serializer=inventorySystem__pb2.Book.SerializeToString,
                response_deserializer=inventorySystem__pb2.response.FromString,
                )
        self.getBook = channel.unary_unary(
                '/service.inventorySystem.Inventory/getBook',
                request_serializer=inventorySystem__pb2.isbn.SerializeToString,
                response_deserializer=inventorySystem__pb2.Book.FromString,
                )


class InventoryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def createBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createBook': grpc.unary_unary_rpc_method_handler(
                    servicer.createBook,
                    request_deserializer=inventorySystem__pb2.Book.FromString,
                    response_serializer=inventorySystem__pb2.response.SerializeToString,
            ),
            'getBook': grpc.unary_unary_rpc_method_handler(
                    servicer.getBook,
                    request_deserializer=inventorySystem__pb2.isbn.FromString,
                    response_serializer=inventorySystem__pb2.Book.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service.inventorySystem.Inventory', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Inventory(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def createBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.inventorySystem.Inventory/createBook',
            inventorySystem__pb2.Book.SerializeToString,
            inventorySystem__pb2.response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service.inventorySystem.Inventory/getBook',
            inventorySystem__pb2.isbn.SerializeToString,
            inventorySystem__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)