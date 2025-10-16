from collections import deque
import time

n = 1_000_000
lst = list(range(n))
dq = deque(range(n))

start = time.perf_counter()
lst = lst[-1:] + lst[:-1]
print("List slice: ", time.perf_counter() - start)


start = time.perf_counter()
dq.rotate(1)
print("Deque rotate: ", time.perf_counter() - start)
