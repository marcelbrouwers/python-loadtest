from multiprocessing import Pool
from multiprocessing import cpu_count

def f(x):
    while True:
        x*x

if __name__ == '__main__':
    processes = cpu_count()
    print('Running load on CPU')
    pool = Pool(processes)
    pool.map(f, range(processes))

