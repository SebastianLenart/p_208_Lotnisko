"""
L = [1, 2, 3]
it = iter(L)
it
<...iterator object at ...>
it.__next__()  # same as next(it)
1
next(it)
2
next(it)
3
next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
-----------------------------------------------------------
L = [1, 2, 3]
iterator = iter(L)
t = tuple(iterator)
t
(1, 2, 3)
-----------------------------------------------------------


"""