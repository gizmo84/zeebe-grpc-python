# zeebe Python GRPC gateway files

This package contains two GRPC Gateway Files needed to build a zeebe-client (https://zeebe.io/) with Python.

Both files were generated following this blog post: https://zeebe.io/blog/2018/11/grpc-generating-a-zeebe-python-client/

```bash
wget https://github.com/zeebe-io/zeebe/raw/0.17.0/gateway-protocol/src/main/proto/gateway.proto

pip install grpcio grpcio-tools

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./gateway.proto
```