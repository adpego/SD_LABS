from multiprocessing import Process
import redisOperations
import time
import calculator
WORKERS = {}
WORKER_ID = 0

def start_worker(id):
    while True:
        job = redisOperations.get_redis_job_queue(redisOperations.QUEUE_JOBS)
        text = calculator.do_request(job['file_URL'])
        if job['operation'] == 'countingWords':
            result = calculator.countingWords(text) 
        elif job['operation'] == 'wordCount':
            result = calculator.wordCount(text)
        redisOperations.send_operation_to_redis_queue(result, '', job['id_result'], '')


# create_worker: create a worker
def create_worker():
    global WORKERS
    global WORKER_ID

    proc = Process(target=start_worker, args=(WORKER_ID,))
    proc.start()
    WORKERS[WORKER_ID] = proc

    WORKER_ID += 1
    return 0

# delete_worker: delete a worker by id
def delete_worker(id):
    global WORKERS
    WORKERS[id].terminate()
    del WORKERS[id]
    return 0

def list_workers():
    global WORKERS
    return str(WORKERS)