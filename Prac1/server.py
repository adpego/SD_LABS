import grpc 
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
import calculator
# import the original workers.py
import workers
# import the original redisOperation.py
import redisOperations

from hashlib import md5
# Create a class to define the server functions, derived from
# calculator_pbc_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    
    def create_worker (self, request, context):
        response = calculator_pb2.String()
        response.value = workers.create_worker()
        return response

    def delete_worker (self, request, context):
        response = calculator_pb2.String()
        response.value = workers.delete_worker(request.id)
        return response

    def list_worker (self, request, context):
        response = calculator_pb2.String()
        response.value = workers.list_workers()
        return response 

    def job_worker (self, request, context):
        id_queue = 'queue:'+create_id_queue(request.operation, request.file_URL)
        response = calculator_pb2.String()
        redisOperations.send_operation_to_redis_queue(request.operation, request.file_URL, redisOperations.QUEUE_JOBS, id_queue)
        response.value = get_redis_job_queue(id_queue)
        return response

def create_id_queue (operation, URL):
      aux = str(time.time())+operation+str(URL)     
      return md5(aux.encode()).hexdigest()

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_CalculatorServicer_to_server(
    CalculatorServicer(), server
)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)