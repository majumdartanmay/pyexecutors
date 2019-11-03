from pyexecutors.Executors.Executors import Executors
from pyexecutors.Holders.Tasks import  SyncTasks, AsyncTasks
import time
import threading


def test():
    time.sleep(1)
    print('Hello world '+ str(threading.current_thread()))


Executors()\
    .enqueue(SyncTasks(test))\
    .enqueue(SyncTasks(test)) \
    .enqueue(SyncTasks(test)) \
    .enqueue(SyncTasks(test))\
    .enqueue(SyncTasks(test))\
    .enqueue(SyncTasks(test)).\
    execute()
