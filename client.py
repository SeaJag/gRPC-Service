import grpc
import templateGRPC_pb2_grpc
import templateGRPC_pb2
import time
import random
import os


def request():
    request = templateGRPC_pb2.TemplateGRPCRequest(
        number=random.randint(0, 9999)
    )

    try:
        response = stub.TemplateGRPCEndpoint(request)
        print(response)
    except:
        print("Server not connected")
        os._exit(0)


if __name__ == '__main__':
    with open('ssl/server.crt', 'rb') as f:
        creds = grpc.ssl_channel_credentials(f.read())
    # channel = grpc.insecure_channel('localhost:5000')
    channel = grpc.secure_channel('localhost:5000', creds)
    stub = templateGRPC_pb2_grpc.TemplateGRPCStub(channel)

    try:
        while True:
            request()
            time.sleep(2)
    except KeyboardInterrupt:
        exit
