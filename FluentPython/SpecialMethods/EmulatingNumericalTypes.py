
from math import hypot

# There are several special methods that can respond to operators (+.-,*,/)


class Vector(object):
    """docstring for Vector"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        # This is used to get string representation of the object
        # %r is to obtain the standard representation
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

        #We will get false if magnitude of the vector zero
    def __bool__(self):
        return bool(abs(self))

        # add and mul return new instances and do not modify original
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Some commands that you can use
a = Vector(3, 4)
a
a.x
a.y
# see how the operators work?????
a * 3
b = Vector(1, 2)
a + b
