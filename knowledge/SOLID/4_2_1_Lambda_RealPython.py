(lambda s: s[::-1])("I am a string")
'gnirts a ma I'

(lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6)


# SORTED -----------------------------------------
animals = ["ferret", "vole", "dog", "gecko"]

def reverse_len(s):
    return -len(s)

sorted(animals, key=reverse_len)


# Lambda --------------------------------------
animals = ["ferret", "vole", "dog", "gecko"]
sorted(animals, key=lambda s: -len(s))
['ferret', 'gecko', 'vole', 'dog']

# return tuple/list/dictionary ----------------------
(lambda x: (x, x ** 2, x ** 3))(3)

(lambda x: [x, x ** 2, x ** 3])(3)

(lambda x: {1: x, 2: x ** 2, 3: x ** 3})(3)