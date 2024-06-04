"""
--------REDUCE-------
reduce() applies a function to the items in an iterable two at a time, progressively combining them to produce a single result
reduce(<f>, <iterable>, <init>) uses <f>, which must be a function that takes exactly two arguments, to progressively
combine the elements in <iterable>. To start, reduce() invokes <f> on the first two elements of <iterable>.
That result is then combined with the third element, then that result with the fourth, and so on until the list is
exhausted. Then reduce() returns the final result.

def f(x, y):
    return x + y


from functools import reduce
reduce(f, [1, 2, 3, 4, 5])

---------------------------------------------------------------
--- lambda ----
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

reduce(lambda x, y: x + y, ["foo", "bar", "baz", "quz"])


def factorial(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, range(1, n + 1))

factorial(4)

factorial(6)


reduce((lambda x, y: x if x > y else y), [23, 49, 6, 32])
---------------------------------------------------------------
reduce(f, ["cat", "dog", "hedgehog", "gecko"])
"".join(["cat", "dog", "hedgehog", "gecko"])
---------------------------------------------------------------
def multiply(x, y):
    return x * y


def factorial(n):
    from functools import reduce
    return reduce(multiply, range(1, n + 1))


factorial(4)  # 1 * 2 * 3 * 4

factorial(6)  # 1 * 2 * 3 * 4 * 5 * 6
---------------------------------------------------------------
max([23, 49, 6, 32])


def greater(x, y):
    return x if x > y else y


from functools import reduce
reduce(greater, [23, 49, 6, 32])
---------------------------------------------------------------
----- init ------
def f(x, y):
    return x + y


from functools import reduce
reduce(f, [1, 2, 3, 4, 5], 100)  # (100 + 1 + 2 + 3 + 4 + 5)


# Using lambda:
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)
---------------------------------------------------------------




























"""