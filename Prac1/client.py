import grpc
import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = calculator_pb2_grpc.CalculatorStub(channel)

operation = calculator_pb2.Operation(operation="wordCount", url=["http://localhost:8000/fitxer1.txt", "http://localhost:8000/fitxer2.txt"])
operation1 = calculator_pb2.Operation(operation="countingWords", url=["http://localhost:8000/fitxer1.txt", "http://localhost:8000/fitxer2.txt"])

response1 = stub.create_worker(calculator_pb2.Empty())
response1 = stub.create_worker(calculator_pb2.Empty())

response2 = stub.job_worker(operation)
response3 = stub.job_worker(operation1)

print(response1.value)
print(response2.value)
print(response3.value)
print(stub.list_workers(calculator_pb2.Empty()).value)