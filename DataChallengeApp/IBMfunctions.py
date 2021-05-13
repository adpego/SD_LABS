import time
from lithops.multiprocessing import Pool

def f(x):
    time.sleep(10)
    return x*x

if __name__ == '__main__':
    with Pool() as p:
        p.map(f,range(100))
    print("hola IBM")