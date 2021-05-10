from multiprocessing import Process
import redisOperations
import time
import calculator
import json
from ast import literal_eval
WORKERS = {}
WORKER_ID = 0

def start_worker(id):
    while True:
        job = redisOperations.get_redis_job_queue(redisOperations.QUEUE_JOBS)
        if (len(job['file_URL']) == 1):
            text = calculator.do_request(job['file_URL'][0])

            if job['operation'] == 'countingWords':
                result = calculator.countingWords(text) 
            elif job['operation'] == 'wordCount':
                result = calculator.wordCount(text)

        elif (len(job['file_URL']) > 1):
            id_worker = 'queue:worker'+str(id)
            for i in range(len(job['file_URL'])):
                redisOperations.send_operation_to_redis_queue(job['operation'], [job['file_URL'][i]], redisOperations.QUEUE_JOBS, id_worker)

            if job['operation'] == 'countingWords':
                result = 0
                for i in range(len(job['file_URL'])):
                    result += redisOperations.get_redis_job_queue(id_worker)['operation']

            elif job['operation'] == 'wordCount':
                result = {}

                for i in range(len(job['file_URL'])):
                    aux = literal_eval(redisOperations.get_redis_job_queue(id_worker)['operation'])
                    for key in aux:
                        if key in result:
                            result[key] += aux[key]
                        else:
                            result[key] = aux[key]
                            
        redisOperations.send_operation_to_redis_queue(result, '', job['id_queue_result'], '')
    

# create_worker: create a worker
def create_worker():
    global WORKERS
    global WORKER_ID

    proc = Process(target=start_worker, args=(WORKER_ID,))
    proc.start()
    WORKERS[WORKER_ID] = proc

    WORKER_ID += 1
    print("Se ha creado un worker!")
    return 0

# delete_worker: delete a worker by id
def delete_worker(id):
    global WORKERS
    WORKERS[id].terminate()
    del WORKERS[id]
    
    print("Se ha eliminado un worker!")
    return 0

def list_workers():
    global WORKERS
    return str(WORKERS)