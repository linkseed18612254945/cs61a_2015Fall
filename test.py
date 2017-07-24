from  math import gcd
from math import sqrt


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
    sum_square_u


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


class Account:
    interest = 0.02

    def __init__(self, holder):
        self.holder = holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Not enough money'
        self.balance -= amount
        return self.balance


class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


class SavingAccount(Account):
    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)


class AsSeenOnTVAccount(SavingAccount, CheckingAccount):
    def __init__(self, holder):
        self.holder = holder
        self.balance = 1


class Bank:
    """ Bank has counts"""

    def __init__(self):
        self.accounts = []

    def open_count(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.balance * account.interest)


class Ratio:
    def __init__(self, n, d):
        self.gcd = gcd(n, d)
        self._n = n // self.gcd
        self._d = d // self.gcd

    @property
    def numer(self):
        return self._n * self.gcd

    @numer.setter
    def numer(self, other):
        self.gcd = other // self._n

    @property
    def denumer(self):
        return self._d * self.gcd

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self._n, self._d)

    def __str__(self):
        return '{0}/{1}'.format(self._n, self._d)

    def __add__(self, other):
        if isinstance(other, int):
            n = self._n + self._d * other
            d = self._d
        elif isinstance(other, type(self)):
            n = self._n * other._d + self._d * other._n
            d = self._d * other._d
        elif isinstance(other, float):
            return float(self) + other
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    def __float__(self):
        return self._n / self._d

    __radd__ = __add__


class Link:
    empty = ()

    def __init__(self, value, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.value = value
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.value
        else:
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link {0}{1}'.format(self.value, rest_str)

    def __add__(self, other):
        if self == Link.empty:
            return other
        elif self.rest == Link.empty:
            return Link(self.value, other)
        else:
            return Link(self.value, self.rest + other)


odd = lambda x: x % 2 == 1


def extend(s, t):
    if s == Link.empty:
        return t
    else:
        return Link(s.value, extend(s.rest, t))


def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.value), map_link(f, s.rest))


def filter_link(f, s):
    if s is Link.empty:
        return s
    elif f(s.value):
        return Link(s.value, filter_link(f, s.rest))
    else:
        return filter_link(f, s.rest)


def join_link(s, separator):
    if s is Link.empty:
        return ''
    elif s.rest is Link.empty:
        return str(s.value)
    else:
        return str(s.value) + separator + join_link(s.rest, separator)


def count(f):
    def counted(*args):
        counted.call += 1
        return f(*args)

    counted.call = 0
    return counted


def count_frames(f):
    def counted(n):
        counted.open_count += 1
        print(counted.open_count)
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1
        return result

    counted.open_count = 0
    counted.max_count = 0
    return counted


@count
def divide(k, n):
    return n % k == 0


def factor_slow(n):
    total = 0
    for k in range(1, n + 1):
        if divide(k, n):
            total += 1
    return total


def factor_fast(n):
    k, total = 1, 0
    while k < sqrt(n):
        if divide(k, n):
            total += 2
        k += 1
    if k ** 2 == n:
        total += 1
    return total


@count_frames
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


@count
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n - 1)


@count
def exp_better(b, n):
    if n == 0:
        return 1
    elif odd(n):
        return b * exp_better(b, n - 1)
    else:
        return square(exp_better(b, n / 2))


# set

def empty(s):
    return s is Link.empty


def set_contains(s, v):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> set_contains(s, 2)
    True
    """
    if empty(s):
        return False
    elif s.value == v:
        return True
    else:
        return set_contains(s.rest, v)


def adjoin_set(s, v):
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)


def keep_if(s, f):
    if empty(s):
        return s
    elif f(s.value):
        return Link(s.value, keep_if(s.rest, f))
    else:
        return keep_if(s.rest, f)


def intersect_set(set1, set2):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> b = Link(2, Link(3, Link(5)))
    >>> intersect_set(s, b)
    Link 2, Link 3
    """
    in_set2 = lambda v: set_contains(set2, v)
    return keep_if(set1, in_set2)

    # order ?
    # if empty(set1) or empty(set2):
    #     return Link.empty
    # elif set1.value == set2.value:
    #     return Link(set1.value, intersect_set(set1.rest, set2.rest))
    # elif set1.value < set2.value:
    #     return intersect_set(set1.rest, set2)
    # else:
    #     return intersect_set(set1, set2.rest)


def union_set(set1, set2):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> b = Link(2, Link(3, Link(4)))
    >>> union_set(s, b)
    Link 4, Link 1, Link 2, Link 3
    """
    # use extend method
    not_in_set1 = lambda v: not set_contains(set1, v)
    return extend(keep_if(set2, not_in_set1), set1)

    # use adjoin method
    # if empty(set2):
    #     return set1
    # else:
    #     return union_set(adjoin_set(set1, set2.value), set2.rest)


# BinaryTree

class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def is_leaf(self):
        return not self.branches

    def tree_sum(self):
        return self.entry + sum([subtree.tree_sum() for subtree in self.branches])

    def cumulative(self):
        if self.is_leaf():
            return self
        else:
            return Tree(self.tree_sum(), [subtree.cumulative() for subtree in self.branches])


class BinaryTree(Tree):
    empty = Tree(None)
    empty.is_empty = True

    def __init__(self, entry, left=empty, right=empty):
        Tree.__init__(self, entry, (left, right))
        self.is_empty = False

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def set_contains(self, v):
        if self.is_empty:
            return False
        elif self.entry == v:
            return True
        elif self.entry < v:
            return self.right.set_contains(v)
        else:
            return self.left.set_contains(v)


def set_binary_contains(s, v):
    if s.is_empty:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_binary_contains(s.right, v)
    else:
        return set_binary_contains(s.left, v)


def adjoin_binary_set(s, v):
    if set_binary_contains(s, v):
        return s
    elif s.is_empty:
        return BinaryTree(v)
    elif s.entry < v:
        return BinaryTree(s.entry, s.left, adjoin_binary_set(s.right, v))
    else:
        return BinaryTree(s.entry, adjoin_binary_set(s.left, v), s.right)


t = BinaryTree(3, BinaryTree(1),
               BinaryTree(7, BinaryTree(5),
                          BinaryTree(9, BinaryTree.empty,
                                     BinaryTree(11))))

abcde = {'a': '.-', 'b': '-...', 'c': '-.-', 'd': '-..', 'e': '.'}


def morse(code):
    root = Tree(None)
    for letter, signals in sorted(code.items()):
        tree = root
        for s in signals:
            match = [b for b in tree.branches if b.entry == s]
            if match:
                tree = match[0]
            else:
                branch = Tree(s)
                tree.branches.append(branch)
                tree = branch
        tree.branches.append(Tree(letter))


def decode(signals, tree):
    """
    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:
        tree = [b for b in tree.braches if b.entry == signal][0]
    leaves = [b for b in tree.braches if b.is_leaf()]
    assert len(leaves) == 1
    return leaves[0].entry


def invert_safe(x):
    try:
        y = 1 / x
        return y
    except ZeroDivisionError as exc:
        print(str(exc))
        return 0


mul = lambda a, b: a * b


def our_reduce(f, s, initial):
    if not s:
        return initial
    else:
        return our_reduce(f, s[1:], f(initial, s[0]))


from operator import truediv


def divide_all(n, ds):
    try:
        return our_reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')


#############################

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __len__(self):
        return max(0, self.end - self.start)

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        elif index < 0:
            return self[len(self) + index]
        else:
            return self.start + index

    def __repr__(self):
        return 'Range({0}, {1})'.format(self.start, self.end)

    def __iter__(self):
        return RangeIter(self.start, self.end)


class RangeIter:
    def __init__(self, start, end):
        self.next = start
        self.end = end

    def __next__(self):
        if self.next >= self.end:
            raise StopIteration
        else:
            result = self.next
            self.next += 1
            return result


def next_letter(letter):
    return chr(ord(letter) + 1)


class Letters:
    @staticmethod
    def letter_generator(letter, end_letter):
        while letter < end_letter:
            yield letter
            letter = next_letter(letter)

    def __init__(self, start='a', end='{'):
        self.start = start
        self.end = end

    def __len__(self):
        return max(0, ord(self.end) - ord(self.start))

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError
        elif index < 0:
            return self[len(self) + index]
        else:
            return chr(ord(self.start) + index)

    def __repr__(self):
        return 'Letters({0}, {1})'.format(self.start, self.end)

    def __iter__(self):
        return Letters.letter_generator(self.start, self.end)


##############
class FibIter:
    def __init__(self):
        self._next = 0
        self._addend = 1

    def __next__(self):
        result = self._next
        self._next, self._addend = self._addend, self._addend + self._nexttt
        return result

    @property
    def __iter__(self):
        return self

def tessss(start, end):
    while start < end:
        yield start
        start += 1
        yield 3
a = tessss(1, 22)
print(type(a))
for i in a: print(i)