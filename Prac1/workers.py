from multiprocessing import Process
import time
WORKERS = {}
WORKER_ID = 0

def start_worker(id):
    time.sleep(2)
    print('Echo',id)
    time.sleep(30)

def create_worker():
    global WORKERS
    global WORKER_ID

    proc = Process(target=start_worker, args=(WORKER_ID,))
    proc.start()
    WORKERS[WORKER_ID] = proc

    WORKER_ID += 1

def delete_worker(id):
    global WORKERS
    WORKERS[id].terminate()
    del WORKERS[id]



create_worker()
create_worker()
print(WORKERS)
create_worker()
print(WORKERS)
delete_worker(1)
print(WORKERS)