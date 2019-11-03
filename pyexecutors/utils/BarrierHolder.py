from pyexecutors.holders.Tasks import AsyncTasks, SyncTasks
from pyexecutors.utils.thread_utils import create_barrier, create_lock


class BarrierHolder:
    sync_lock = create_lock()

    def __init__(self, async_task):
        self.tasks = list()
        self.barrier = None
        self.async_task = async_task
        self.barrier = None

    def add_task(self, task):
        if self.async_task and not isinstance(task, AsyncTasks):
            raise ValueError('Only Async Tasks can inserted in a async barrier holder')
        elif not self.async_task and not isinstance(task, SyncTasks):
            raise ValueError('Only Sync Tasks can inserted in a sync barrier holder')

        self.tasks.append(task)

    def get_barrier(self):
        if self.async_task:
            if self.barrier is None:
                self.barrier = create_barrier(len(self.tasks))
        else:
            self.barrier = BarrierHolder.sync_lock

        return self.barrier

    def get_tasks(self):
        return self.tasks
