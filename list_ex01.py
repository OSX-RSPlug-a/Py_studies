from itertools import chain


numbers = [[1], [2, 3], [4, [5, 6, [7, 8, [9, [10, 11, 12]]]]]]


list(chain.from_iterable(numbers))


def flatten(numbers):
    for num in numbers:
        if isinstance(num, int):
            yield num
        else:
            yield from flatten(num)
            
        
print(flatten(numbers))
print(list(flatten(numbers)))
print(sum(flatten(numbers)))