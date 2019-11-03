import re
import threading

from pyexecutors.executors.Executors import SyncTasks, AsyncTasks, Executors


def execute_method(exec_thread_number):
    current_thread = str(threading.current_thread()).lower()
    current_thread_number = re.search('-(\\d+)', current_thread).group(1)
    assert int(current_thread_number) == exec_thread_number, 'argument number and thread number dont match ' \
                                                             'for thread_number {} and arguement passed {}'.format(
        current_thread_number, exec_thread_number)


def test_threads():
    Executors() \
        .enqueue(AsyncTasks(execute_method, args=(1,))) \
        .enqueue(AsyncTasks(execute_method, args=(2,))) \
        .enqueue(SyncTasks(execute_method, args=(3,))) \
        .enqueue(AsyncTasks(execute_method, args=(4,))) \
        .execute()
