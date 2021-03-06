# Q1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    if n < 1:
        return 0
    return n + skip_add(n - 2)


# Q2
def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    if n == 0:
        return
    count_up(n - 1)
    print(n)
    return


# Q3
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    return n * skip_mul(n - 2)

# Q4
def factorial(n):
    """Return n * (n - 1) * (n - 2) * ... * 1.

    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    return n * factorial(n-1)


# Q5
def print_up_to(n):
    """Print every natural number up to n, inclusive.

    >>> print_up_to(5)
    1
    2
    3
    4
    5
    """
    if n == 0:
        return
    print_up_to(n - 1)
    print(n)
    return


# Q6
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if a % b == 0:
        return b
    return gcd(b, a % b)


# Q7
def is_even(n):
    return n % 2 == 0


def next_number(n):
    if is_even(n):
        return n // 2
    else:
        return 3 * n + 1


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    return 1 + hailstone(next_number(n))


# Q8
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: x % 10 + 10 * y
    while x > 0:
        x, y = x // 10, f()
    return y == n

