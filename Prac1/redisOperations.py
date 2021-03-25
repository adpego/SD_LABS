import redis
import time
import json
import requests

QUEUE_JOBS = 'queue:jobs'
conn = redis.Redis()

def send_operation_to_redis_queue(operation, file_URL, id_queue, id_queue_result):
   data = {
        'id_queue_result': id_queue_result,
        'operation': operation,
        'file_URL': file_URL,
        'time': time.time()
   }
   conn.rpush(id_queue, json.dumps(data))

def get_redis_job_queue(id_queue):
    packed = conn.blpop([id_queue, 0])
    return json.loads(packed[1])

#print(do_request("http://localhost:8000/client.py"))

#blpop rpush