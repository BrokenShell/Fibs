import pickle
from functools import cache


class FunctionCache:
    """ Function Cache Decorator Class """

    def __init__(self, function):
        self.cache = {}
        self.function = function
        self.__doc__ = function.__doc__

    def __call__(self, *args, **kwargs):
        key = (pickle.dumps(args), pickle.dumps(kwargs))
        if key in self.cache:
            result = self.cache[key]
        else:
            result = self.cache[key] = self.function(*args, **kwargs)
        return result


@FunctionCache
def fib_class_cache(n):
    if n in {0, 1}:
        return n
    else:
        return fib_class_cache(n - 1) + fib_class_cache(n - 2)


def fib_func_memo(n):
    if not hasattr(fib_func_memo, 'memo'):
        fib_func_memo.memo = {0: 0, 1: 1}
    if n not in fib_func_memo.memo:
        fib_func_memo.memo[n] = fib_func_memo(n - 1) + fib_func_memo(n - 2)
    return fib_func_memo.memo[n]


@cache
def fib_cache(n):
    if n in {0, 1}:
        return n
    else:
        return fib_cache(n - 1) + fib_cache(n - 2)
