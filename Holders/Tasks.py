from pyexecutors.Utils.thread_utils import acquire_lock, release_lock, barrier_wait


class Tasks:

    def __init__(self, f, *args, **kwargs):
        assert f is not None, 'Function cannot be null'
        self.f = f
        self.args = args
        self.kwargs = kwargs

    def acquire(self, lock):
        pass

    def release(self, lock):
        pass


class SyncTasks(Tasks):
    def acquire(self, lock):
        acquire_lock(lock)

    def release(self, lock):
        release_lock(lock)


class AsyncTasks(Tasks):
    def acquire(self, barrier):
        barrier_wait(barrier)
