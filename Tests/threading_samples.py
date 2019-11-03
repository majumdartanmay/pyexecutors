import threading
import time

lock = threading.RLock()


def lock_test():
    lock.acquire()
    time.sleep(1)
    print('Hello world')
    lock.release()


def test_1():
    t1 = threading.Thread(target=lock_test)
    t1.start()

    t2 = threading.Thread(target=lock_test)
    t2.start()
