'''General examples of using matplotlib'''

import matplotlib.pyplot as plt
import numpy as np

# simple figure
#Set up x,y values
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#label the y axis
plt.ylabel('some numbers')
# show the plot
plt.show()

# Add some decoration
# ro stands for red circles
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# set the axis you want to see
plt.axis([0, 6, 0, 20])
plt.show()


# plot three items as a time
# generate data from to to 5 with 0.2 values increments
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# Histogram
x = np.random.randn(100000)
# data, number of bins, color
fig = plt.hist(x, 200,  facecolor="g")
plt.show()


# Barplot 
# Plot a barplot showing nucleotide frequencies
bases = ["A","G","C","T"]
# y_pos needs to be a numpy array
y_pos = np.arange(len(bases))
freqs = np.array([0.1, 0.4, 0.25, 0.25])
plt.bar(bases,freqs,align="center")
plt.show()

