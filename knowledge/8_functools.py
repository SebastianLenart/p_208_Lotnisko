"""
This technique is useful when you want to create specialized versions of a function with some parameters pre-set,
making it more convenient to use in specific contexts. In this case, server_log is a version of log where the subsystem
is always set to 'server'.
----PARTIAL------
import functools

def log(message, subsystem):
    "Write the contents of 'message' to the specified subsystem."
    print('%s: %s' % (subsystem, message))
    ...

server_log = functools.partial(log, subsystem='server')
server_log('Unable to open socket

------------------------------------------------------------------------------------
------reduce------
functools.reduce(func, iter, [initial_value]) cumulatively performs an operation on all the iterable’s elements and,
therefore, can’t be applied to infinite iterables. func must be a function that takes two elements and returns a single
value. functools.reduce() takes the first two elements A and B returned by the iterator and calculates func(A, B).
It then requests the third element, C, calculates func(func(A, B), C), combines this result with the fourth element
returned, and continues until the iterable is exhausted. If the iterable returns no values at all, a TypeError exception
is raised. If the initial value is supplied, it’s used as a starting point and func(initial_value, A) is the first calculation.


import operator, functools
functools.reduce(operator.concat, ['A', 'BB', 'C'])
'ABBC'
functools.reduce(operator.concat, [])
Traceback (most recent call last):
  ...
TypeError: reduce() of empty sequence with no initial value
functools.reduce(operator.mul, [1, 2, 3], 1)
6
functools.reduce(operator.mul, [], 1)
1

"""