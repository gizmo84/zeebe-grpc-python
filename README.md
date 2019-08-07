# zeebe Python GRPC gateway files

This package contains two GRPC Gateway Files needed to build a zeebe-client or a zeebe-worker (https://zeebe.io/) 
with Python.

Both files were generated following the instructions on this (now outdated) blog post:
https://zeebe.io/blog/2018/11/grpc-generating-a-zeebe-python-client/

```bash
wget https://raw.githubusercontent.com/zeebe-io/zeebe/0.20.0/gateway-protocol/src/main/proto/gateway.proto

pip install grpcio grpcio-tools

python -m grpc_tools.protoc -Izeebe_grpc/ --python_out=zeebe_grpc/ --grpc_python_out=zeebe_grpc/ ./gateway.proto
```

## How to install and use this package?

```bash
pip install zeebe-grpc
```
```python
from zeebe_grpc import gateway_pb2
from zeebe_grpc import gateway_pb2_grpc
```