from time import perf_counter, sleep
from functools import wraps
import random


def profiler(fn):
    """
    Implementing profiler this way takes more time to read and write.
    Use class instead.
    """
    _counter = 0
    _elapsed = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal _counter
        nonlocal _elapsed
        _counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()

        _elapsed = end - start
        return result

    def counter():
        """This func allows you to access to _counter even after its change
        """
        return _counter

    def avg_time():
        """This func allows you to access to _avg_time even after its change
        """
        return _elapsed / _counter

    # this is the approach when you create generic single dispatch
    inner.counter = counter
    inner.avg_time = avg_time

    return inner


@profiler
def func1():
    _time = random.random()
    print(f'func1 _time: {_time}')
    sleep(_time)


class ProfilerClassImplementation:
    """Much more readable&easier way of writing decorator"""

    def __init__(self, fn):
        self.counter = 0
        self.total_elapsed = 0
        self.fn = fn

    def __call__(self, *args, **kwargs):
        self.counter += 1
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        end = perf_counter()
        self.total_elapsed += (end - start)
        return result

    @property
    def avg_time(self):
        return self.total_elapsed / self.counter


@ProfilerClassImplementation
def func2():
    _time = random.random()
    print(f'func2 _time: {_time}')
    sleep(_time)


if __name__ == '__main__':
    func1()
    print(func1.avg_time())
    print(func1.counter())

    func2()
    print(func2.avg_time)
    print(func2.counter)

    func2()
    print(func2.avg_time)
    print(func2.counter)
