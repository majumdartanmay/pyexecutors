import time
from pyexecutors.Executors.Executors import Executors
from pyexecutors.Holders.Tasks import SyncTasks


def test(a=None, asd = None):
    if a is None:

        a = -1
    if asd is None:
        asd = -1
    time.sleep(1)
    print('Hello world ' + str(a) + " , " +str(asd))

def final_callback():
    print("all tasks executed")

Executors() \
    .enqueue(SyncTasks(test, args=(2,))) \
    .enqueue(SyncTasks(test, kwargs={"asd":2})) \
    .enqueue(SyncTasks(test)) \
    .enqueue(SyncTasks(test)) \
    .enqueue(SyncTasks(test)) \
    .enqueue(SyncTasks(test)). \
    execute(final_callback)
