"""
numbers = [1, 2, 3, 4, 5]

list(map(str, numbers))


def custom_map(function, iterable):
    from functools import reduce

    return reduce(
        lambda items, value: items + [function(value)],
        iterable,
        [],
    )

list(custom_map(str, numbers))
-------------------------------------------------------------------
numbers = list(range(10))
numbers


def is_even(x):
    return x % 2 == 0


list(filter(is_even, numbers))


def custom_filter(function, iterable):
    from functools import reduce

    return reduce(
        lambda items, value: items + [value] if function(value) else items,
        iterable,
        []
    )

list(custom_filter(is_even, numbers))




"""