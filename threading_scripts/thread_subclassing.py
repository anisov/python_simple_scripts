import threading
import time


class TestThread(threading.Thread):
    def run(self):
        print(f'{self.getName()} has started')
        super().run()
        print(f'{self.getName()} has finished')


def sleeper(n, name):
    print(f'Sleep, {name}')
    time.sleep(n)
    print(f'Awoke, {name}')


def double(number, cycles):
    for _ in range(cycles):
        number += number
    print(number)


threads_list = []


for i in range(50):
    t = TestThread(target=double, name=f'thread {i + 1}', args=[i, 3])
    threads_list.append(t)
    t.start()

for t in threads_list:
    t.join()
