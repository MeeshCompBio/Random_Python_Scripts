import numpy as np
from math import exp 
from libc.math cimport exp as c_exp
from cython.parallel import prange

'''example of normal function across array
    cython c function across array
    multithreaded example using openmp
```

# standard numpy example
def array_f(X):
    Y = np.zeros(X.shape)
    index = X > 0.5
    Y[index] = np.exp(X[index])
    return Y

# using cfunction with cython
def c_array_f(double[:] X):
    # declare vars just like in C
    cdef int N = X.shape[0]
    cdef double[:] Y = np.zeros(N)
    cdef int i

    for i in range(N):
        if X[i] > 0.5:
            Y[i] = c_exp(X[i])
        else:
            Y[i] = 0
    return Y

# using openmp and pranges
def c_array_f_multi(double[:] X):
    cdef int N = X.shape[0]
    cdef double[:] Y = np.zeros(N)
    cdef int i
    # use prange for multithreading
    for i in prange(N, nogil=True):
        if X[i] > 0.5:
            Y[i] = c_exp(X[i])
        else:
            Y[i] = 0

    return Y
