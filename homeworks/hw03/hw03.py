from math import log


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <= 3:
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n <= 3:
        return n
    i = 1
    a, b, c = 1, 2, 3
    while i < n:
        a, b, c = b, c, 3 * a + 2 * b + c
        i += 1
    return a


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    num, oper = 0, 1
    for k in range(1, n+1):
        num += oper
        if k % 7 == 0 or '7' in str(k):
            oper = - oper
    return num

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def get_coin_nums(amount):
    if amount == 0:
        return 0
    return int(log(amount, 2)) + 1


def get_greatest_denomination(n):
    return 2 ** (n - 1)


def count_change_with_coins(amount, used_coin):
    """
    >>> count_change_with_coins(20 ,5)
    60
    """

    if amount == 0:
        return 1
    if used_coin == 1:
        return 1
    free_change_amount = amount - get_greatest_denomination(used_coin)
    coins = min(get_coin_nums(free_change_amount), used_coin)
    return count_change_with_coins(free_change_amount, coins) + count_change_with_coins(amount, used_coin - 1)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    assert amount > 0, "amount should be positive"
    return count_change_with_coins(amount, get_coin_nums(amount))


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """

    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"

    if n == 1:
        return print_move(start, end)
    mid_rod = 6 - start - end
    move_stack(n - 1, start, mid_rod)
    move_stack(1, start, end)
    move_stack(n - 1, mid_rod, end)



from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'

