from concurrent.futures import wait, ALL_COMPLETED
from time import sleep
from concurrent.futures import ThreadPoolExecutor

def worker(task_id):
    """Если в конце функции ставить print вместо
    return, выводится хаотично"""
    print(f'started task with id {task_id}')
    sleep(1)
    return (f"task with id {task_id} done")

# """Не понял, зачем нужен wait, выводит результат
# в рандомном порядке"""
# with ThreadPoolExecutor() as executor:
#      futures = [executor.submit(worker, task_id) for task_id in range(4)]
#      ok = wait(futures,return_when=ALL_COMPLETED)
#      for future in ok.done:
#          res = future.result()
#          print(res)

"""Выводит результат по порядку"""
with ThreadPoolExecutor() as executor:
    results = executor.map(worker, [1,2,3,4])
    for result in results:
        print(result)





