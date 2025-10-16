import timeit

nums = list(range(1_000_000))
num_set = set(nums)
x = 999_999

list_time = timeit.timeit("x in nums", globals=globals(), number=1000)
set_time = timeit.timeit("x in num_set", globals=globals(), number=1000)

print(f"list lookup: {list_time:.5f} sec")
print(f"set lookup: {list_time:.5f} sec")