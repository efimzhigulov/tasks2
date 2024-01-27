from multiprocessing import Pool
from time import sleep

def worker(task_id):
    print(f'started task with id {task_id}')
    sleep(1)
    return (f"task with id {task_id} done")

if __name__ == '__main__':
    with Pool() as p:
        p = Pool(2)
        results = p.map(worker, [1,2,3,4])
        for result in results:
            print(result)



