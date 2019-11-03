from pyexecutors.Holders.Tasks import AsyncTasks, SyncTasks, Tasks
from pyexecutors.Utils.thread_utils import create_lock, create_barrier, execute_functions_async
from queue import Queue
from pyexecutors.Utils.BarrierHolder import BarrierHolder


class Executors:

    def __init__(self):
        self.tasks = list()
        self.barrier_tasks_queue = list()

    def enqueue(self, task):
        if task is not isinstance(task, (AsyncTasks, SyncTasks)):
            raise ValueError('Invalid objects passed to {}'.format('enqueue method'))

        sync_task = isinstance(task, SyncTasks)
        prev_sync_task = len(self.tasks) != 0 and isinstance(self.tasks[-1], SyncTasks)

        if sync_task or (not sync_task and prev_sync_task):
            barrier_holder = BarrierHolder(async_task=not sync_task)
            barrier_holder.add_task(task)
            self.barrier_tasks_queue.append(barrier_holder)
        elif not sync_task:
            if not prev_sync_task:
                barrier_holder = BarrierHolder(async_task=True) if len(self.barrier_tasks_queue) == 0 else self.barrier_tasks_queue[-1]
                barrier_holder.add_task(task)

        return self

    def execute(self, callback=None):
        for barrier_task in self.barrier_tasks_queue:
            lock = barrier_task.get_barrier()
            tasks = barrier_task.get_tasks()

    def execute_tasks(self, tasks, lock):
        for task in tasks:
            execute_functions_async(task, lock)