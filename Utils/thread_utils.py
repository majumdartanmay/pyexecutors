import threading
from pyexecutors.Holders.Tasks import Tasks, AsyncTasks, SyncTasks


def execute_function(task, lock):
    if task is not isinstance(task, (AsyncTasks, SyncTasks)):
        raise ValueError("Invalid data type : {} for {}, please use {}"
                         .format(type(task),
                                 'execute_function',
                                 type(Tasks).__name__))
    task.acquire(lock)
    task.f(task.args, task.kwargs)
    task.release(lock)


def execute_functions_async(task, lock):
    thread = threading.Thread(target=task, args=(lock,))
    thread.start()


def create_lock():
    return threading.RLock()


def create_barrier(parties):
    return threading.Barrier(parties=parties)


def barrier_wait(barrier):
    if barrier is not isinstance(barrier, threading.Barrier):
        raise ValueError('Invalid param passed to barrier_wait. It should be an instance of threading.Barrier')


def acquire_lock(lock):
    if lock is not isinstance(lock, (threading.RLock, threading.Lock)):
        raise ValueError('Invalid param passed to acquire_lock. It should be an instance of Lock')
    lock.acquire()


def release_lock(lock):
    if lock is not isinstance(lock, (threading.RLock, threading.Lock)):
        raise ValueError('Invalid param passed to acquire_lock. It should be an instance of Lock')
    lock.release()
