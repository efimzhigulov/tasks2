import time


def clock():
    st_time = round(time.time())
    while True:
        if round(time.time() - st_time) % 5 == 0:
            yield "5 sec"
        else:
            yield 0

def counter():
    for i in range(100000000):
            yield i


def main():
    cl = clock()
    co = counter()
    while True:
        data = next(co)
        print(data)
        timer = next(cl)
        if timer:
            print(timer)
        time.sleep(1)

print(main())

