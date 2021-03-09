from multiprocessing import Process
import redisOperations
import time
import calculator
WORKERS = {}
WORKER_ID = 0

def start_worker(id):
    while True:
        job = redisOperations.get_redis_job_queue()
        text = calculator.do_request(job['URL'])
        if job['operation'] == 'countingWords':
            calculator.countingWords(text) 
        elif job['operation'] == 'wordCount':
            calculator.wordCount(text)


# create_worker: create a worker
def create_worker():
    global WORKERS
    global WORKER_ID

    proc = Process(target=start_worker, args=(WORKER_ID,))
    proc.start()
    WORKERS[WORKER_ID] = proc

    WORKER_ID += 1

# delete_worker: delete a worker by id
def delete_worker(id):
    global WORKERS
    WORKERS[id].terminate()
    del WORKERS[id]

def list_workers():
    global WORKERS
    return WORKERS