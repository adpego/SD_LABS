import grpc

import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

stub = calculator_pb2_grpc.CalculatorStub(channel)

text = calculator_pb2.String(value="hola que tal")

with open("test.txt") as file:
    textFile = file.read()

textFile = calculator_pb2.String(value=textFile)



response1 = stub.countingWords(text)
response2 = stub.countingWords(textFile)
response3 = stub.wordCount(textFile)


print(response1.value)
print(response2.value)
print(response3.value)