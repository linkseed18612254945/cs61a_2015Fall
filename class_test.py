from math import pi, sqrt, pow
def luhn_digit(n):
    double_n = n * 2
    if double_n > 9:
        return double_n - 9
    else:
        return double_n


def luhn_sum(n):
    if n < 10:
        return n
    else:
        rest_of_last, last = split(n)
        return last + luhn_double_sum(rest_of_last)


def luhn_double_sum(n):
    rest_of_last, last = split(n)
    if n < 10:
        return luhn_digit(last)
    else:

        return luhn_digit(last) + luhn_sum(rest_of_last)


def luhn_check(n):
    if luhn_sum(n) % 10 == 0:
        return True
    else:
        return False


def cascad(n):
    print(n)
    if n < 10:
        return
    else:
        cascad(n // 10)
        print(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

shrink = lambda n: f_then_g(print, shrink, n // 10)
grow = lambda n: f_then_g(grow, print, n // 10)


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def count_partitions(n, m):
    if m > n:
        m = n
    if n == 0 or m == 1:
        return 1
    return count_partitions(n - m, m) + count_partitions(n, m - 1)


def trace_simple(fn):
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced


def double(fn):
    def doubled(x):
        return fn(x) * 2
    return doubled

@double
def sum_square_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total


def sum_square_up_to_recursion(n):
    if n == 1:
        return 1
    else:
        return sum_square_up_to_recursion(n - 1) + square(n)


def square(n):
    return n * n

########### Data Abstraction ##############

# Constructor and selectors


def rational(n, d):
    """ Construct the rational number"""
    def select(name):
        if name == 'n':
            return n
        if name == 'd':
            return d
    return select


def numer(x):
    return x('n')

def denom(x):
    return x('d')


################## tree ################

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not bool(branches(tree))


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        r = root(left) + root(right)
    return tree(r, [left, right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

def leaves(tree):
    if is_leaf(tree):
        return tree
    return sum([leaves(b) for b in branches(tree)], [])


def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif n < 0:
        return tree(False)
    elif m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])

def make_withdraw(balance):
    def withdraw(money):
        return balance - money
    return withdraw

withdraw = make_withdraw(100)
withdraw()
withdraw()




