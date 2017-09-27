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

### Tupules are not just immutable lists
Tuples hold records, each item in the tuple hold the data for one field and the postions of the item gives its meaning