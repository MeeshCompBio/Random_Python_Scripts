'''General examples of using scipy'''
import numpy as np

#You can't just import scipy, you need to specify a module
from scipy import stats


a = np.array([ 0.7972,  0.0767,  0.4383,  0.7866,  0.8091,
               0.1954, 0.6307, 0.6599,  0.1065,  0.0508])

#check the mean of a to see what z-score of 0 would be
a.mean()

# convert to z-scores
stats.zscore(a)

