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
import json
import logging
import grpc
from zeebe_grpc import gateway_pb2, gateway_pb2_grpc

with grpc.insecure_channel("localhost:26500") as channel:
    stub = gateway_pb2_grpc.GatewayStub(channel)

    # print the topology of the zeebe cluster
    topology = stub.Topology(gateway_pb2.TopologyRequest())
    print(topology)

    # deploy a process definition
    with open("bpmn/echo.bpmn", "rb") as process_definition_file:
        process_definition = process_definition_file.read()
        process = gateway_pb2.ProcessRequestObject(
            name="echo.bpmn",
            definition=process_definition
        )
    stub.DeployProcess(
        gateway_pb2.DeployProcessRequest(
            processes=[process]
        )
    )

    # start a process instance
    variables = {
        "message": "This is a Message"
    }
    stub.CreateProcessInstance(
        gateway_pb2.CreateProcessInstanceRequest(
            bpmnProcessId="ECHO",
            version=-1,
            variables=json.dumps(variables)
        )
    )

    # start a worker
    activate_jobs_response = stub.ActivateJobs(
        gateway_pb2.ActivateJobsRequest(
            type="echo",
            worker="Python worker",
            timeout=60000,
            maxJobsToActivate=32
        )
    )
    for response in activate_jobs_response:
        for job in response.jobs:
            try:
                print(job.variables)
                stub.CompleteJob(gateway_pb2.CompleteJobRequest(jobKey=job.key, variables=json.dumps({})))
                logging.info("Job Completed")
            except Exception as e:
                stub.FailJob(gateway_pb2.FailJobRequest(jobKey=job.key))
                logging.info(f"Job Failed {e}")
```

## How to (re)build the Python gRPC?

```bash
wget https://raw.githubusercontent.com/zeebe-io/zeebe/0.21.1/gateway-protocol/src/main/proto/gateway.proto -O ./zeebe_grpc/gateway.proto

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./zeebe_grpc/gateway.proto
```