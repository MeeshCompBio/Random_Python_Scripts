# Classic for loop
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
codes

# Using list comprehensions to make more compact
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
codes

# another example
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

# classic for loop
for size in sizes:
    print((color, size))

# rearrange order for sorting
tshirts = [(color, size) for size in sizes for color in colors]

# Generator expression
symbols = '$¢£¥€¤'

# If the generator expression is the single argument in a function call,
# there is no need to duplicate the enclosing parentheses.
tuple(ord(symbol) for symbol in symbols)

import array
# The array constructor takes two arguments, so the parentheses around the
# generator expression are mandatory. The first argument of the array constructor
# defines the storage type used for the numbers in the array
array.array('I', (ord(symbol) for symbol in symbols))


colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# This list is never built in memory the generator
# feeds the loop one item at a time
# This is super cool
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)