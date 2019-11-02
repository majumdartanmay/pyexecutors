from pyexecutors.Holders.Tasks import AsyncTasks, SyncTasks, Tasks
from pyexecutors.Utils.thread_utils import create_lock, create_barrier, execute_functions_async


class Executors:

    def __init__(self):
        self.barriers = list()
        self.tasks = list()
        self.barrier_length = 0
        self.barrier_cache = None

    def enqueue(self, task):
        if task is not isinstance(task, (SyncTasks, AsyncTasks)):
            raise ValueError("Invalid data type : {} for {}, please use {}"
                             .format(type(task),
                                     type(self).__name__),
                             type(Tasks).__name__)

        sync_operation = isinstance(task, SyncTasks)
        prev_task_async = len(self.tasks) > 0 and self.tasks[-1] is isinstance(task, AsyncTasks)

        if sync_operation and not prev_task_async:
            self.barrier_cache = create_barrier(self.barrier_length)
            self.barriers.append(self.barrier_cache)
        elif not sync_operation:
            self.barrier_length += 1
            self.barriers.append(self.barrier_cache)
        elif sync_operation:
            self.barriers.append(create_lock())
        self.tasks.append(task)

    def execute(self, callback):
        if len(self.tasks) == 0:
            raise Exception('There are not tasks to execute')
        elif len(self.barriers) != len(self.tasks):
            raise Exception('Length of the tasks and barriers should always be the same')
