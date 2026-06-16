from typing import Generator


def func() -> Generator[int, None, None]:
    breakpoint()
    for i in range(5):
        yield i


#func()
gen = func()
next(gen)


def test_func_yields_correct_range():
    result = list(func())
    
    assert result == [0, 1, 2, 3, 4]