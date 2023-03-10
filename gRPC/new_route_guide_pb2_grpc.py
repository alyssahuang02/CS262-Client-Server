# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import new_route_guide_pb2 as new__route__guide__pb2


class ChatStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.login_user = channel.unary_unary(
                '/routeguide.Chat/login_user',
                request_serializer=new__route__guide__pb2.Text.SerializeToString,
                response_deserializer=new__route__guide__pb2.Text.FromString,
                )
        self.register_user = channel.unary_unary(
                '/routeguide.Chat/register_user',
                request_serializer=new__route__guide__pb2.Text.SerializeToString,
                response_deserializer=new__route__guide__pb2.Text.FromString,
                )
        self.display_accounts = channel.unary_stream(
                '/routeguide.Chat/display_accounts',
                request_serializer=new__route__guide__pb2.Text.SerializeToString,
                response_deserializer=new__route__guide__pb2.Text.FromString,
                )
        self.check_user_exists = channel.unary_unary(
                '/routeguide.Chat/check_user_exists',
                request_serializer=new__route__guide__pb2.Text.SerializeToString,
                response_deserializer=new__route__guide__pb2.Text.FromString,
                )
        self.delete_account = channel.unary_unary(
                '/routeguide.Chat/delete_account',
                request_serializer=new__route__guide__pb2.Text.SerializeToString,
                response_deserializer=new__route__guide__pb2.Text.FromString,
                )
        self.logout = channel.unary_unary(
                '/routeguide.Chat/logout',
                request_serializer=new__route__guide__pb2.Text.SerializeToString,
                response_deserializer=new__route__guide__pb2.Text.FromString,
                )
        self.client_receive_message = channel.unary_stream(
                '/routeguide.Chat/client_receive_message',
                request_serializer=new__route__guide__pb2.Text.SerializeToString,
                response_deserializer=new__route__guide__pb2.Note.FromString,
                )
        self.client_send_message = channel.unary_unary(
                '/routeguide.Chat/client_send_message',
                request_serializer=new__route__guide__pb2.Note.SerializeToString,
                response_deserializer=new__route__guide__pb2.Text.FromString,
                )


class ChatServicer(object):
    """Missing associated documentation comment in .proto file."""

    def login_user(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def register_user(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def display_accounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def check_user_exists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_account(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def logout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def client_receive_message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def client_send_message(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login_user': grpc.unary_unary_rpc_method_handler(
                    servicer.login_user,
                    request_deserializer=new__route__guide__pb2.Text.FromString,
                    response_serializer=new__route__guide__pb2.Text.SerializeToString,
            ),
            'register_user': grpc.unary_unary_rpc_method_handler(
                    servicer.register_user,
                    request_deserializer=new__route__guide__pb2.Text.FromString,
                    response_serializer=new__route__guide__pb2.Text.SerializeToString,
            ),
            'display_accounts': grpc.unary_stream_rpc_method_handler(
                    servicer.display_accounts,
                    request_deserializer=new__route__guide__pb2.Text.FromString,
                    response_serializer=new__route__guide__pb2.Text.SerializeToString,
            ),
            'check_user_exists': grpc.unary_unary_rpc_method_handler(
                    servicer.check_user_exists,
                    request_deserializer=new__route__guide__pb2.Text.FromString,
                    response_serializer=new__route__guide__pb2.Text.SerializeToString,
            ),
            'delete_account': grpc.unary_unary_rpc_method_handler(
                    servicer.delete_account,
                    request_deserializer=new__route__guide__pb2.Text.FromString,
                    response_serializer=new__route__guide__pb2.Text.SerializeToString,
            ),
            'logout': grpc.unary_unary_rpc_method_handler(
                    servicer.logout,
                    request_deserializer=new__route__guide__pb2.Text.FromString,
                    response_serializer=new__route__guide__pb2.Text.SerializeToString,
            ),
            'client_receive_message': grpc.unary_stream_rpc_method_handler(
                    servicer.client_receive_message,
                    request_deserializer=new__route__guide__pb2.Text.FromString,
                    response_serializer=new__route__guide__pb2.Note.SerializeToString,
            ),
            'client_send_message': grpc.unary_unary_rpc_method_handler(
                    servicer.client_send_message,
                    request_deserializer=new__route__guide__pb2.Note.FromString,
                    response_serializer=new__route__guide__pb2.Text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'routeguide.Chat', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Chat(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def login_user(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.Chat/login_user',
            new__route__guide__pb2.Text.SerializeToString,
            new__route__guide__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def register_user(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.Chat/register_user',
            new__route__guide__pb2.Text.SerializeToString,
            new__route__guide__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def display_accounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/routeguide.Chat/display_accounts',
            new__route__guide__pb2.Text.SerializeToString,
            new__route__guide__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def check_user_exists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.Chat/check_user_exists',
            new__route__guide__pb2.Text.SerializeToString,
            new__route__guide__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_account(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.Chat/delete_account',
            new__route__guide__pb2.Text.SerializeToString,
            new__route__guide__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def logout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.Chat/logout',
            new__route__guide__pb2.Text.SerializeToString,
            new__route__guide__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def client_receive_message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/routeguide.Chat/client_receive_message',
            new__route__guide__pb2.Text.SerializeToString,
            new__route__guide__pb2.Note.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def client_send_message(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.Chat/client_send_message',
            new__route__guide__pb2.Note.SerializeToString,
            new__route__guide__pb2.Text.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
