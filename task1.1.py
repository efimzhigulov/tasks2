import threading
import time
from threading import Lock

mutex = Lock()
counter = 0
def increment_counter():
    global counter
    mutex.acquire()
    for _ in range(100):
        counter += 1
    mutex.release()


for _ in range(3):
    threading.Thread(target=increment_counter,).start()

print(counter)