from multiprocessing import Process
from multiprocessing import Array
from multiprocessing import Queue
import time


def sq(nums, sh_list):
    for index, n in enumerate(nums):
        time.sleep(1)
        res = n**2
        sh_list[index] = res
        print(f'sq {n} = {res}')


def sq_queue(nums, shared_q):
    for index, n in enumerate(nums):
        time.sleep(1)
        res = n**2
        shared_q.put(res)


def cu(nums, sh_list):
    for index, n in enumerate(nums):
        time.sleep(1)
        res = n**3
        sh_list[index+5] = res
        print(f'cu {n} = {res}')


def main():
    nums = [2, 3, 4, 5, 6]

    shared_array = Array('i', 15)
    shared_q = Queue()
    process1 = Process(target=sq, args=(nums, shared_array))
    process2 = Process(target=cu, args=(nums, shared_array))
    process3 = Process(target=sq_queue, args=(nums, shared_q))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
    process3.join()

    while not shared_q.empty():
        print('get shared_q: ', shared_q.get())

    print(shared_array[:])


if __name__ == '__main__':
    main()
