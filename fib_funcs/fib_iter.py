from functools import cache


def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_iter_memo(n):
    if not hasattr(fib_iter_memo, "memo"):
        fib_iter_memo.memo = {0: 0, 1: 1}
    if n not in fib_iter_memo.memo:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        fib_iter_memo.memo[n] = a
    return fib_iter_memo.memo[n]


@cache
def fib_iter_cache(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    print(fib_iter_cache(40))
