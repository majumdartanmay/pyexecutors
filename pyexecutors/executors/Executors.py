from pyexecutors.holders.Tasks import AsyncTasks, SyncTasks
from pyexecutors.utils.BarrierHolder import BarrierHolder
from pyexecutors.utils.thread_utils import execute_functions_async


def execute_tasks(tasks, lock):
    for task in tasks:
        execute_functions_async(task, lock)


class Executors:

    def __init__(self):
        self.tasks = list()
        self.barrier_tasks_queue = list()

    def enqueue(self, task):
        if not isinstance(task, (AsyncTasks, SyncTasks)):
            raise ValueError('Invalid objects passed to {}'.format('enqueue method'))

        sync_task = isinstance(task, SyncTasks)
        prev_sync_task = len(self.tasks) != 0 and isinstance(self.tasks[-1], SyncTasks)
        barrier_holder = BarrierHolder(async_task=not sync_task)

        if sync_task or (not sync_task and prev_sync_task):
            barrier_holder.add_task(task)
            self.barrier_tasks_queue.append(barrier_holder)
        else:
            prev_queue_used = False
            if len(self.barrier_tasks_queue) != 0:
                barrier_holder = self.barrier_tasks_queue[-1]
                prev_queue_used = True
            barrier_holder.add_task(task)
            if not prev_queue_used:
                self.barrier_tasks_queue.append(barrier_holder)

        self.tasks.append(task)

        return self

    def execute(self, final_callback=None):

        if final_callback is not None:
            self.enqueue(SyncTasks(final_callback))

        for barrier_task in self.barrier_tasks_queue:
            lock = barrier_task.get_barrier()
            tasks = barrier_task.get_tasks()
            execute_tasks(tasks, lock)

