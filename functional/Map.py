# map
from functools import reduce
from logging import log


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


@log(msg="", level=0)
def name():
    print("print log")
    pass


name
print(name.__class__)
print(name.__name__)
print(name.__annotations__)
print(name.__code__)
