# challenge.greplin.com

from itertools import count
from math import ceil, sqrt


def fib(n):
    if n in [1, 2]:
        return 1

    i, j = 1, 1
    for _ in xrange(n - 2):
        i, j = j, i + j

    return j


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for odd in xrange(3, int(ceil(sqrt(n))), 2):
        if n % odd == 0:
            return False

    return True


def prime_factors(n):
    two = []
    if n % 2 == 0:
        two = [2]

    return two + [i for i in xrange(3, n, 2) if n % i == 0 and is_prime(i)]


if __name__ == '__main__':
    for i in count(3):
        candidate = fib(i)
        if candidate > 227000 and is_prime(candidate):
            print candidate + 1
            print prime_factors(candidate + 1)
            print sum(prime_factors(candidate + 1))
            break
