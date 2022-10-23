# gRPC server

Create a gRPC server that implements the x --> x+1 method

## Steps

### Prerequisites

Need ``pip`` and ``python3`` for this project

### Installation

``pip install -r requirements.txt``

### Generate protobuf

``python3 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. templateGRPC.proto``

### Run Server
``python3 server.py``

### Run Client

Run this command on another terminal window

``python3 client.py``


# Ressources

https://grpc.github.io/grpc/python/grpc.html#create-client-credentials

https://grpc.io/blog/wireshark/

