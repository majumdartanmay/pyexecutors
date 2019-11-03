from pyexecutors.Executors.Executors import Executors
from pyexecutors.Holders.Tasks import AsyncTasks


def test():
    print('Hello world')


Executors().enqueue(AsyncTasks(test));

