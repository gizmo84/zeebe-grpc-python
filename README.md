# zeebe Python GRPC gateway files

This package contains two GRPC Gateway Files needed to build a zeebe-client or a zeebe-worker (https://zeebe.io/) 
with Python.

Both files were generated following the instructions on this (now outdated) blog post:
https://zeebe.io/blog/2018/11/grpc-generating-a-zeebe-python-client/

## How to install and use this package?

```bash
pip install zeebe-grpc
```
```python
import grpc
from zeebe_grpc import gateway_pb2
from zeebe_grpc import gateway_pb2_grpc

with grpc.insecure_channel(<zeebe brocker>) as channel:
    stub = gateway_pb2_grpc.GatewayStub(channel)
    topology = stub.Topology(gateway_pb2.TopologyRequest())
    
    print(topology)
```