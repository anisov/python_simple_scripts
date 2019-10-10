from multiprocessing import Process
from multiprocessing import Value
from multiprocessing import Lock
import time


def add_value(val, lock):
    for _ in range(1000):
        time.sleep(.001)
        with lock:
            val.value = val.value + 1


def delete_value(val, lock):
    for _ in range(1000):
        time.sleep(.001)
        with lock:
            val.value = val.value - 1


def main():
    shared_value = Value('i', 1)
    lock = Lock()
    print(shared_value.value)

    process1 = Process(target=add_value, args=(shared_value, lock))
    process2 = Process(target=delete_value, args=(shared_value, lock))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print(shared_value.value)


if __name__ == '__main__':
    main()
