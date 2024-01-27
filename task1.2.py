import time
import multiprocessing

def worker(task_id):
    print(f'start {task_id}')
    time.sleep(2)
    print(f'end {task_id}')

if __name__  ==  '__main__':

    p1 = multiprocessing.Process(target=worker(task_id=1))
    p2 = multiprocessing.Process(target=worker(task_id=2))
    p3 = multiprocessing.Process(target=worker(task_id=3))
    p4 = multiprocessing.Process(target=worker(task_id=4))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()



