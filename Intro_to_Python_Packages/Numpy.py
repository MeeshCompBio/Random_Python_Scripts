# General examples of using numpy

import numpy as np

base_Array = [0, 1, 2, 3]
# creating our first numpy array
np_Array = np.array([0, 1, 2, 3])

# numpy arrays also has built in functions that are faster
# Say that we want to calculate the mean of the array

# This would be the normal python way
sum(base_Array)/len(base_Array)
# 625 ns to run command

# This is the numpy built in function
Array.mean()
# 12.6 µs to run command, way faster

# 2D array
TwoD = np.array([[0, 1, 2], [3, 4, 5]]) 
TwoD.dim
TwoD.shape

# Index the array
TwoD[:1]
TwoD[1:]

# Select a specific column
TwoD[:,[1]]

# Generating data for arrays
# produce a sequence of numbers from 0 up to 5 at spacing 0.2
test = np.arange(0, 5, 0.2)

# produce a sequence of numbers from 0 to 100 at spacing 0.1
a = np.arange(0,100,0.1)

# make an empty matrix
Zeros = np.zeros([100,100]) 


x = np.random.randn(10,10)

#creates a 10x10 matrix of uniformly distributed
x = np.random.normal(10,2.5,[10,10])
# operations on arrays

TwoD = np.array([[0, 1, 2], [3, 4, 5]]) 
plusone = TwoD + 1
squared = TwoD**2
TwoD[:1] = TwoD[:1]+10