from MonkeyScope import timer
from fib_funcs.fib_lambda_calc import fib_lambda_calc
from fib_funcs.fib_recursive import fib_recursive
from fib_funcs.fib_generator import fib_generator
from fib_funcs.fib_cache import fib_class_cache, fib_func_memo, fib_cache
from fib_funcs.fib_iterative import fib_iter, fib_iter_cache, fib_iter_memo
from fib_funcs.fib_matrix import fib_matrix_exponentiation


N = 100
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

print(f"\n{fib_matrix_exponentiation(N) = }")
timer(fib_matrix_exponentiation, N)
