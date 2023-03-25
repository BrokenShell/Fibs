def recurse(tree):

    def limb(left):
        return lambda right: left(left)(right)

    def branch(leaf):
        return tree(limb(leaf))

    return branch(branch)


def fib_lambda_calc(n):
    def fib_worker(fib):
        return lambda a: 1 if a <= 2 else fib(a - 1) + fib(a - 2)
    return recurse(fib_worker)(n)
