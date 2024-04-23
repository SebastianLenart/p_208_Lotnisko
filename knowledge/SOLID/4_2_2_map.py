"""
But remember, map() doesn’t return a list. It returns an iterator called a map object. To obtain the values from the
iterator, you need to either iterate over it or use list():


"""

animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(lambda s: s[::-1], animals)
list(iterator)
['tac', 'god', 'gohegdeh', 'okceg']

# Combining it all into one line:
list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", "gecko"]))
['tac', 'god', 'gohegdeh', 'okceg']

# ---------------------------------------------
strings = []
for i in [1, 2, 3, 4, 5]:
    strings.append(str(i))

strings
['1', '2', '3', '4', '5']
"+".join(strings)
'1+2+3+4+5'

"+".join(map(str, [1, 2, 3, 4, 5]))
'1+2+3+4+5'


# ------MUTLIPLE----------------------------
def f(a, b, c):
    return a + b + c


list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300]))
[111, 222, 333]


# LAMBDA
list(
    map(
        (lambda a, b, c: a + b + c),
        [1, 2, 3],
        [10, 20, 30],
        [100, 200, 300]
    )
)
