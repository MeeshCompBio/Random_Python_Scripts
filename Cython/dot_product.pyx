import numpy as np
from math import exp 
from libc.math cimport exp as c_exp
from cython.parallel import prange

# normal numpy method
def array_f(X):
    Y = np.zeros(X.shape)
    index = X > 0.5
    Y[index] = np.exp(X[index])
    return Y

#using C libraries
def c_array_f(double[:] X):
    # declare variables just like in C
    cdef int N = X.shape[0]
    cdef double[:] Y = np.zeros(N)
    cdef int i

    for i in range(N):
        if X[i] > 0.5:
            # call c library
            Y[i] = c_exp(X[i])
        else:
            Y[i] = 0

    return Y


# using open MP to escape the GIL
def c_array_f_multi(double[:] X):
    cdef int N = X.shape[0]
    cdef double[:] Y = np.zeros(N)
    cdef int i

    # use the prange function here
    for i in prange(N, nogil=True):
        if X[i] > 0.5:
            Y[i] = c_exp(X[i])
        else:
            Y[i] = 0

    return Y
