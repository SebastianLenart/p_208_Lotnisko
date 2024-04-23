"""
The last function I’ll discuss, itertools.groupby(iter, key_func=None), is the most complicated. key_func(elem) is a
 function that can compute a key value for each element returned by the iterable. If you don’t supply a key function,
 the key is simply each element itself.

groupby() collects all the consecutive elements from the underlying iterable that have the same key value, and returns a
stream of 2-tuples containing a key value and an iterator for the elements with that key.

city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
             ('Anchorage', 'AK'), ('Nome', 'AK'),
             ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
             ...
            ]

def get_state(city_state):
    return city_state[1]

itertools.groupby(city_list, get_state) =>
  ('AL', iterator-1),
  ('AK', iterator-2),
  ('AZ', iterator-3), ...

where
iterator-1 =>
  ('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')
iterator-2 =>
  ('Anchorage', 'AK'), ('Nome', 'AK')
iterator-3 =>
  ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')
groupby() assumes that the underlying iterable’s contents will already be sorted based on the key. Note that the
returned iterators also use the underlying iterable, so you have to consume the results of iterator-1 before requesting
iterator-2 and its corresponding key.


"""