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
