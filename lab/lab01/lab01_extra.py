"""Coding practice for Lab 1."""

# While Loops

def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    while n > 0:
        if 20 % n == 0:
            print(n)
        n -= 1



def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    total = 1
    if not k:
        return 1
    else:
        while k > 0:
            total = total * n
            n -= 1
            k -= 1
        return total


