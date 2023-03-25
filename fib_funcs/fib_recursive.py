def fib_recursive(n):
    if n in {0, 1}:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == '__main__':
    print(fib_recursive(10))
