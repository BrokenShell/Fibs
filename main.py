from MonkeyScope import timer
from fib_funcs import (fib_class_cache,
                       fib_func_memo,
                       fib_cache,
                       fib_generator,
                       fib_iter,
                       fib_iter_cache,
                       fib_iter_memo,
                       fib_lambda_calc,
                       fib_recursive)

N = 10
print(f"Fib Benchmarks for {N = }")

print(f"\n{fib_lambda_calc(N) = }")
timer(fib_lambda_calc, N)

print(f"\n{fib_recursive(N) = }")
timer(fib_recursive, N)

print(f"\n{fib_generator(N) = }")
timer(fib_generator, N)

print(f"\n{fib_class_cache(N) = }")
timer(fib_class_cache, N)

print(f"\n{fib_iter(N) = }")
timer(fib_iter, N)

print(f"\n{fib_iter_memo(N) = }")
timer(fib_iter_memo, N)

print(f"\n{fib_func_memo(N) = }")
timer(fib_func_memo, N)

print(f"\n{fib_cache(N) = }")
timer(fib_cache, N)

print(f"\n{fib_iter_cache(N) = }")
timer(fib_iter_cache, N)
