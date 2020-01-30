# PyExecutors - A simple multi-threading task management library




![Travis Passing](https://travis-ci.com/tanmay23235616/pyexecutors.svg?branch=master) 
[![PyPI version](https://badge.fury.io/py/pyexecutors.svg)](https://badge.fury.io/py/pyexecutors) 
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyexecutors)](https://badge.fury.io/py/pyexecutors)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
 [![Downloads](https://pepy.tech/badge/pyexecutors)](https://pepy.tech/project/pyexecutors)



*Are you great with multi-threading?*

[![](https://api.gh-polls.com/poll/01DZM6ZQJE9TQYRE5YS86JAH1S/Yes)](https://api.gh-polls.com/poll/01DZM6ZQJE9TQYRE5YS86JAH1S/Yes/vote)
[![](https://api.gh-polls.com/poll/01DZM6ZQJE9TQYRE5YS86JAH1S/No)](https://api.gh-polls.com/poll/01DZM6ZQJE9TQYRE5YS86JAH1S/No/vote)
 
PyExecutors is a utility module which provides straight-forward, powerful functions for working with asynchronous python functions.
 
This runs an array of functions in series. You can program the functions to run synchronously or asynchronously in the order you desire. 


## Installation

`pip install pyexecutors`

Then, from a python interpreter 

```
from pyexecutors.executors.Executors import SyncTasks, AsyncTasks, Executors

def execute_method(exec_thread_number):
    // your function

Executors() \
    .enqueue(AsyncTasks(execute_method, args=(1,))) \
    .enqueue(AsyncTasks(execute_method, args=(2,))) \
    .enqueue(SyncTasks(execute_method, args=(3,))) \
    .enqueue(AsyncTasks(execute_method, args=(4,))) \
    .execute()

```

### How does it work

**Synchronous Functions**
> A synchronous functions runs by encapsulation itself with [RLocks](https://docs.python.org/2.0/lib/rlock-objects.html)
. The lock is released after the functions' execution is complete


**Asynchronous Functions**
> Asynchronous takes the help of [Barriers](https://docs.python.org/3/library/threading.html). The idea is to create a barrier with limit being the number of consecutive async functions.
> A new barrier is created when a Sync function comes in between. 

### Running Tests

```buildoutcfg
pip install pytest
pytest
```
The [test function](https://raw.githubusercontent.com/tanmay23235616/pyexecutors/master/pyexecutors/tests/test_executors.py) simply matches the thread number with the argument passed to the functions. 
The argument has been given to match the order of thread execution


### License

This project is licensed under the MIT License - see the LICENSE.md file for details



