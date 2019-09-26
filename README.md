# zeebe Python gRPC gateway files

This package contains two gRPC Gateway Files needed to build a zeebe-client or a zeebe-worker (https://zeebe.io/)
with Python.

Both files were generated following the instructions on this (now outdated) blog post:
https://zeebe.io/blog/2018/11/grpc-generating-a-zeebe-python-client/

## How to install and use this package?

```bash
pip install zeebe-grpc
```
```python
import grpc
from zeebe_grpc import gateway_pb2, gateway_pb2_grpc

with grpc.insecure_channel("zeebe:26500") as channel:
    stub = gateway_pb2_grpc.GatewayStub(channel)
    topology = stub.Topology(gateway_pb2.TopologyRequest())
    
    print(topology)
```

## How to (re)build the Python gRPC?

```bash
wget https://raw.githubusercontent.com/zeebe-io/zeebe/0.20.0/gateway-protocol/src/main/proto/gateway.proto -O ./zeebe_grpc/gateway.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./zeebe_grpc/gateway.proto
```