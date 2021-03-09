import redis
import time
import json
import requests

conn = redis.Redis()
def send_operation_to_redis_queue(operation, file_URL):
   data = {
        'id': id,       #TODO Ojito con la id 
        'operation': operation,
        'file_URL': file_URL,
        'time': time.time()
   }
   conn.rpush('queue:jobs', json.dumps(data))

def get_redis_job_queue():
    packed = conn.blpop(['queue:jobs'], 0)
    return json.loads(packed[1])

#print(do_request("http://localhost:8000/client.py"))

#blpop rpush