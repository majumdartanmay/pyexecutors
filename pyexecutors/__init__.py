from pyexecutors.executors.Executors import Executors
from pyexecutors.holders.Tasks import AsyncTasks, SyncTasks
"""
    pyexecutors
    ~~~~~~~~~~~
    
    a lite-weight library to efficiently run series of 
    asynchronous and synchronous tasks concurrently
    without worrying about managing different threads
    in your own.
    
"""


def executor():
    return Executors()


def async_tasks(f, args=None, kwargs=None):
    if args is None:
        args = []
    if kwargs is None:
        kwargs = {}
    return AsyncTasks(f, args, kwargs)


def sync_tasks(f, args=None, kwargs=None):
    if kwargs is None:
        kwargs = {}
    if args is None:
        args = []
    return SyncTasks(f, args, kwargs)


__version__ = "0.0.3.dev"
