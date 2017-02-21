from math import *

def wears_jacket(temp, raining):
    """
    >>> rain = False
    >>> wears_jacket(90, rain)
    False
    >>> wears_jacket(40, rain)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining

def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow.
    >>> handle_overflow(35, 29)
    1 spot left in Section 2.
    >>> handle_overflow(20, 32)
    10 spots left in Section 1.
    >>> handle_overflow(35, 30)
    No space left in either section.
    """
    if s1 <= 30 and s2 <= 30:
        print('No overflow.')
    elif s1 >= 30 and s2 >= 30:
        print('No space left in either section.')
    elif s1 > 30:
        left_spot = 30 - s2
        if left_spot == 1:
            muilt = ''
        else:
            muilt = 's'
        print('{0} spot{1} left in Section 2.'.format(left_spot, muilt))
    else:
        left_spot = 30 - s1
        if left_spot == 1:
            muilt = ''
        else:
            muilt = 's'
        print('{0} spot{1} left in Section 1.'.format(left_spot, muilt))

def is_prime(n):
    """
    >>> is_prime(17)
    True
    >>> is_prime(15)
    False
    >>> is_prime(3)
    True
    """
    if n == 1 or n == 2:
        return False
    k = int(sqrt(n))
    while k > 1:
        if n % k == 0:
            return False
        k -= 1
    return True


def fact(a, b):
    assert a >= b, 'a need larger than b!'
    if a == b:
        return a
    else:
        return a * fact(a - 1, b)


def choose(n, k):
    """
    >>> choose(5, 2)
    10
    >>> choose(20, 6)
    38760
    """
    return fact(n, n - k + 1) // fact(k, 1)

def is_even(x):
    return x % 2 == 0

def keep_ints(cond, n):
    """
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n + 1):
        if cond(i):
            print(i)

def keep_ints_fn(n):
    """
    >>> keep_ints_fn(7)(is_even)
    2
    4
    6
    """
    def keep(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
    return keep
