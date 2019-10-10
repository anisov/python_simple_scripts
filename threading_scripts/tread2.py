# coding: UTF-8
from threading import Thread
import time


def prescript(file_name, num, thread):
    with open(file_name, 'w') as f:
        for i in range(num):
            f.write(f'{thread} \n')


thread1 = Thread(target=prescript, args=('f1.txt', 10, 'thread1'))
thread2 = Thread(target=prescript, args=('f1.txt', 1000, 'thread2'))

thread1.start()
time.sleep(4)
thread2.start()
thread1.join()
thread2.join()
