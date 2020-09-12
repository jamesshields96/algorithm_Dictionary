from math import *


def eulicidAlgorithm(x, y, verbose=True):
    if x < y:  # We are trying to make sure x >=y
        return eulicidAlgorithm(y, x, verbose=True)
    print()
    while y != 0:
        if verbose:
            print('%s = %s * %s + %s' % (x, floor(x/y), y, x % y))
        (x, y) = (y, x % y)

    if verbose: print('gcd is %s' % x)
    return x


eulicidAlgorithm(300,600)
eulicidAlgorithm(105,304)
eulicidAlgorithm(1,80)
eulicidAlgorithm(123,432)