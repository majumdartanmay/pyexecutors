import threading
import time

lock = threading.RLock()

def test():
    lock.acquire()
    time.sleep(1)
    print('Hello world')
    lock.release()

t1 = threading.Thread(target=test)
t1.start()

t2 = threading.Thread(target=test)
t2.start()
