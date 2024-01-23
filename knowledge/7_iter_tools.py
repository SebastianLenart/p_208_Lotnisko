"""
itertools.count(start, step)
itertools.count(10, 5) =>
  10, 15, 20, 25, 30, 35, 40, 45, 50, 55, ...
---------------------------------------------------------
itertools.cycle(iter) saves a copy of the contents of a provided iterable and returns a new iterator that returns
its elements from first to last. The new iterator will repeat these elements infinitely.

itertools.cycle([1, 2, 3, 4, 5]) =>
  1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
---------------------------------------------------------
itertools.repeat(elem, [n]) returns the provided element n times, or returns the element endlessly if n is not provided.

itertools.repeat('abc') =>
  abc, abc, abc, abc, abc, abc, abc, abc, abc, abc, ...
itertools.repeat('abc', 5) =>
  abc, abc, abc, abc, abc
---------------------------------------------------------
itertools.chain(iterA, iterB, ...) takes an arbitrary number of iterables as input, and returns all the elements of
the first iterator, then all the elements of the second, and so on, until all of the iterables have been exhausted.
itertools.chain(['a', 'b', 'c'], (1, 2, 3)) =>
  a, b, c, 1, 2, 3
---------------------------------------------------------
itertools.islice(iter, [start], stop, [step]) returns a stream that’s a slice of the iterator.
With a single stop argument, it will return the first stop elements. If you supply a starting index, you’ll get
stop-start elements, and if you supply a value for step, elements will be skipped accordingly. Unlike Python’s string
and list slicing, you can’t use negative values for start, stop, or step.

itertools.islice(range(10), 8) =>
  0, 1, 2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8) =>
  2, 3, 4, 5, 6, 7
itertools.islice(range(10), 2, 8, 2) =>
  2, 4, 6
---------------------------------------------------------
itertools.tee(iter, [n]) replicates an iterator; it returns n independent iterators that will all return
the contents of the source iterator. If you don’t supply a value for n, the default is 2. Replicating iterators
requires saving some of the contents of the source iterator, so this can consume significant memory if the iterator is
large and one of the new iterators is consumed more than the others.

itertools.tee( itertools.count() ) =>
   iterA, iterB

where iterA ->
   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...

and   iterB ->
   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
---------------------------------------------------------

itertools.combinations([1, 2, 3, 4, 5], 2) =>
  (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 3), (2, 4), (2, 5),
  (3, 4), (3, 5),
  (4, 5)
---------------------------------------------------------
itertools.combinations_with_replacement([1, 2, 3, 4, 5], 2) =>
  (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 2), (2, 3), (2, 4), (2, 5),
  (3, 3), (3, 4), (3, 5),
  (4, 4), (4, 5),
  (5, 5)
---------------------------------------------------------
itertools.permutations([1, 2, 3, 4, 5], 2) =>
  (1, 2), (1, 3), (1, 4), (1, 5),
  (2, 1), (2, 3), (2, 4), (2, 5),
  (3, 1), (3, 2), (3, 4), (3, 5),
  (4, 1), (4, 2), (4, 3), (4, 5),
  (5, 1), (5, 2), (5, 3), (5, 4)
---------------------------------------------------------
















"""
