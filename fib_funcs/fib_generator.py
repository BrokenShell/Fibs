def fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def fib_generator(n):
    fib = fibs()
    for _ in range(n-1):
        next(fib)
    return next(fib)


if __name__ == '__main__':
    print(fib_generator(40))
