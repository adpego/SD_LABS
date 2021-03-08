import redis
import time
import json
import requests
def send_operation_to_redis_queue(conn, operation, file_URL):
   data = {
        'operation': operation,
        'file_URL': file_URL,
        'time': time.time()
   }
   conn.rpush('queue:jobs', json.dumps(data))

def get_redis_job_queue(conn):
    packed = conn.blpop(['queue:jobs'], 0)
    to_send = json.loads(packed[1])
    print(packed[2])
    print(to_send)

def do_request(URL):
    return requests.get(URL).text


print(do_request("http://localhost:8000/client.py"))

#blpop rpush