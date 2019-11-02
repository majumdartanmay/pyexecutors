class Tasks:
    def __init__(self, f, callback, *args, **kwargs):
        assert f is not None, 'Function cannot be null'
        self.f = f
        self.args = args
        self.kwargs = kwargs
        self.callback = callback


class SyncTasks(Tasks):
    pass


class AsyncTasks(Tasks):
    pass
