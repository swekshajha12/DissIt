import grpc
from concurrent import futures


# define a grpc service
class MyService(my_service_pb2_grpc.MyServiceServicer):
    def MyMethod(self, request, context):
        # implementation of the gRPC method
        response = my_service_pb2.MyResponse()
        response.message = "Response from the server"
        return response


# create a grpc server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
my_service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
server.add_insecure_port('[::]:50051')

# start the server
server.start()

# You can now make multiple gRPC calls to the MyMethod on the same connection concurrently.
