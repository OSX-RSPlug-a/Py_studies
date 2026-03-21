from functools import lru_cache

@lru_cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


result = fib(50)
print(f"O resultado Fibonacci: {result}")
