import grpc
import grpc_tools_pb2
import grpc_tools_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:5500') as channel:
        stub = grpc_tools_pb2_grpc.ExecutorServiceStub(channel)
        request = grpc_tools_pb2.ExecuteRequestData(
            code="print('Hello, World!')",
            files=[
                grpc_tools_pb2.FileData(filename="example.txt", content=b"Sample content")
            ]
        )
        response = stub.ExecuteRequest(request)
        print("gRPC response:")
        print(f"Success: {response.success}")
        print(f"Message: {response.message}")
        print("Response JSON:")
        for item in response.response_json:
            print(f"  {item.key}: {item.value}")

if __name__ == "__main__":
    run()
