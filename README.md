# PyExecutors - A simple multi-threading task management library

![Travis Passing](https://travis-ci.com/tanmay23235616/pyexecutors.svg?branch=master) 
[![PyPI version](https://badge.fury.io/py/pyexecutors.svg)](https://badge.fury.io/py/pyexecutors) 
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyexecutors)](https://badge.fury.io/py/pyexecutors)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
 [![Downloads](https://pepy.tech/badge/pyexecutors)](https://pepy.tech/project/pyexecutors)
 
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
### License

This project is licensed under the MIT License - see the LICENSE.md file for details



