# Overview of built in sequences

## Sequence types in standard library
* Container sequences (can hold more than one type)
    * list, tuple, and collections.deque
* Flat sequences (hold items of one type)
    * str, bytes, bytearray, memoryview, and array array

* Mutable sequences
    * list, bytearray, array.array, collections.deque and memoryview
* Immutable
    * tuple, str and bytes

## List comprehensions
### Generator expressions
gen exp saves more memory because it yeilds items one by one

## Tupules are not just immutable lists
* Tuples hold records, each item in the tuple hold the data for one field and the postions of the item gives its meaning
* Tuples support all list methods that do not involve adding or removing items (no __reversed__ method)
### Tuple unpacking
* Most visible form of tuple unpacking is parallel assignment, that is, assigning items from an iterable to a tuple of variables

```python
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates

# you can also prefix the argument with a star
divmod(20, 8)
quotient, remainder = divmod(*t)


# Or use a dummy variable
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
filename
# returns: 'idrsa.pub'

# Use a star to grab excess items
one, two, *everythingelse = range(5)
everythingelse
# returns: [2,3,4]

```

### Named Tuples
* You can use the collections.namedtuple function to produce subclasses of tuple enhanced iwth field and class name
```python
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo.population
# Output: 36.933

tokyo.coordinates
# Output: (35.689722, 139.691667)