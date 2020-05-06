"""
1. Useful for creating function-like objects that need to maintain state
2. Useful for creating decorator classes
"""


class Partial:
    """
    partial from functools like class that calls func of input when called.
    """

    def __init__(self, func, *args):
        self._func = func
        self._args = args

    def __call__(self, *args):
        print(self._args, *args)
        return self._func(*self._args, *args)


def some_func(a, b, c):
    return a, b, c


class NotCallable:
    pass


if __name__ == '__main__':
    partial = Partial(some_func, 1, 2)
    print(partial(3))
    print('all true because Partial has __call__')
    print(f'Partial: {callable(Partial)}')
    print(f'callable(partial): {callable(partial)}')

    not_callable_instance = NotCallable()
    print('instance not true because it has no __call__')
    print(f'NotCallable(): {callable(NotCallable)}')
    print(f'not_callable_instance: {callable(not_callable_instance)}')
