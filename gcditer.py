def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    for i in range(a+1):
        if a % (a-i) == 0 and b % (a-i) == 0:
            return (a-i)

print(gcdIter(35, 77))