import threading
import time

resource = {'A': threading.Lock(), 'B': threading.Lock()}


def proc(n, rs):
    for r in rs:
        print("Процесс %s запрашивает ресурс %s" % (n, r))
        resource[r].acquire()
        print("Процесс %s получил ресурс %s" % (n, r))
        time.sleep(1)
        print("Процесс %s выполняется" % n)
    for r in rs:
        resource[r].release()
        print("Процесс %s закончил выполнение" % n)


p1 = threading.Thread(target=proc, name="t1", args=["1", "AB"])
p2 = threading.Thread(target=proc, name="t2", args=["2", "BA"])
p1.start()
p2.start()
p1.join()
p2.join()
