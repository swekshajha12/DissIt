from functools import reduce


def sum(a, b): return a + b


print(reduce(sum, [4, 3, 2, 1]))
