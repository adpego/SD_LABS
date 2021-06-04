import grpc
import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = calculator_pb2_grpc.CalculatorStub(channel)

operation = calculator_pb2.Operation(operation="wordCount", url=["http://localhost:8000/fitxer1.txt", "http://localhost:8000/fitxer2.txt"])
operation1 = calculator_pb2.Operation(operation="countingWords", url=["http://localhost:8000/fitxer1.txt", "http://localhost:8000/fitxer2.txt"])
operation2 = calculator_pb2.Operation(operation="wordCount", url=["http://localhost:8000/fitxer1.txt", "http://localhost:8000/fitxer2.txt", "http://localhost:8000/fitxer3.txt", "http://localhost:8000/fitxer4.txt"])

response1 = stub.create_worker(calculator_pb2.Empty()) # Create worker

response2 = stub.job_worker(operation)
print("Response with 1 worker")
print(response2.value)

print()
response1 = stub.create_worker(calculator_pb2.Empty()) # Create worker
response2 = stub.job_worker(operation)
print("Response with 2 worker, wordCount")
print(response2.value)

print()
response2 = stub.job_worker(operation1)
print("Response with 2 worker, countingWords")
print(response2.value)

print()
response2 = stub.job_worker(operation2)
print("Response with 2 worker, wordCount, 4 urls")
print(response2.value)


response1 = stub.create_worker(calculator_pb2.Empty()) # Create worker
response1 = stub.create_worker(calculator_pb2.Empty()) # Create worker
response2 = stub.job_worker(operation)
response3 = stub.job_worker(operation1)
response4 = stub.job_worker(operation2)

print()
print("All operations, 4 workers")
print(response2.value)
print(response3.value)
print(response4.value)


print()
print(stub.list_workers(calculator_pb2.Empty()).value) # List sorkers