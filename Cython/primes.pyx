def primes(int nb_primes):
    '''Returns the number of prime numbers you want'''
    # declare vars
    cdef int n, i, len_p
    cdef int p[1000]

    # limit the input number since this is just and example
    if nb_primes > 1000:
        nb_primes = 1000

    # set var equal to zero for incremental loop
    len_p = 0
    n = 2
    while len_p < nb_primes:
        # check if it is a prime num
        for i in p[:len_p]:
            if n % i == 0:
                break

        # If it can't divide then it is a prime num
        else:
            p[len_p] = n
            len_p += 1
        n += 1

    # Return python list
    result_as_list  = [prime for prime in p[:len_p]]
    return result_as_list
