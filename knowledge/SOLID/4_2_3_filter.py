def greater_than_100(x):
    return x > 100


list(filter(greater_than_100, [1, 111, 2, 222, 3, 333]))

# lambda:
list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333]))

# ----------------------------------------------
list(range(10))


def is_even(x):
    return x % 2 == 0


list(filter(is_even, range(10)))

list(filter(lambda x: x % 2 == 0, range(10)))
