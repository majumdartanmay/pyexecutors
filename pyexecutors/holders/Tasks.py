from pyexecutors.utils.thread_utils import acquire_lock, release_lock, barrier_wait
from abc import abstractmethod


class Tasks:

    def __init__(self, f, args=[], kwargs={}):
        assert f is not None, 'Function cannot be null'
        self.f = f
        self.args = args
        self.kwargs = kwargs

    @abstractmethod
    def acquire(self, lock):
        pass

    @abstractmethod
    def release(self, lock):
        pass


class SyncTasks(Tasks):
    def acquire(self, lock):
        acquire_lock(lock)

    def release(self, lock):
        release_lock(lock)


class AsyncTasks(Tasks):
    def release(self, lock):
        pass

    def acquire(self, barrier):
        barrier_wait(barrier)
