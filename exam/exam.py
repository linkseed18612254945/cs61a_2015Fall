##############
#### MT1 #####
##############


def find_digit(n, d):
    """
    >>> find_digit(567, 7)
    0
    >>> find_digit(567, 5)
    2
    >>> find_digit(567, 9)
    False
    >>> find_digit(568789, 8)
    3
    """
    i, k = 0, False
    while n:
        n, last = n // 10, n % 10
        if last == d:
            k = i
        i += 1
    return k

def luhn_sum(n):
    """Return the Luhn sum of n
    >>> luhn_sum(135)
    12
    >>> luhn_sum(185)
    13
    >>> luhn_sum(138743)
    30
    """
    def luhn_digit(digit):
        x = digit * multiplier
        return (x // 10) + (x % 10)

    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total += luhn_digit(last)
        multiplier = 3 - multiplier
    return total


def check_digit(n):
    """Add a digit to the end of n so that the result has a valid Luhn sum
    >>> check_digit(153)
    1537
    >>> check_digit(13874)
    138743
    """
    if luhn_sum(n) % 10 == 0:
        return n
    else:
        return n * 10 + 10 - luhn_sum(n * 10) % 10



def decompose1(f, h):
    """Return g such that h(x) equals f(g(x)) for any non-negative integer x.
    >>> add_one = lambda x: x + 1
    >>> square_then_add_one = lambda x: x * x + 1
    >>> g = decompose1(add_one, square_then_add_one)
    >>> g(5)
    25
    >>> g(10)
    100
    """
    def g(x):
        def r(y):
            if h(x) == f(y):
                return y
            else:
                return r(y + 1)
        return r(0)
    return g


def make_adder(n):
    def adder(k):
        return k + n
    return adder


def square(n):
    return n * n


def compose1(f, g):
    """ Return a function h that compose f and g
    >>> compose1(square, make_adder(2))(3)
    25
    """
    def h(x):
        return f(g(x))
    return h

e = make_adder(1)
print(decompose1(e, compose1(square, e))(3) + 2000)


""" y = 2, 3, 4, 5"""
f = lambda x: find_digit(234567, x)
for i in range(1, 10):
    if compose1(f, f)(i) == i:
        print(i)


########### Data Structure #########
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


##############
#### MT2 #####
##############


def complete(t, d, k):
    """Return whether t is d-k-complete
    >>> complete(Tree(1), 0 ,5)
    True
    >>> u = Tree(1, [Tree(1), Tree(1), Tree(1)])
    >>> [complete(u, 1, 3), complete(u, 1, 2), complete(u, 2, 3)]
    [True, False, False]
    >>> complete(Tree(1, [u, u , u]), 2, 3)
    True
    """
    if t.is_leaf() and d == 0:
        return True
    return len(t.branches) == k and all([complete(subtree, d-1, k) for subtree in t.branches])


def list2num(lst):
    """ return the digit number of list
    >>> list2num([1,3,4,5])
    1345
    """
    reversed_list_iter = reversed(lst)
    total, multiplier = 0, 1
    for num in reversed_list_iter:
        total += num * multiplier
        multiplier *= 10
    return total


def num2list(num):
    """ Return the num to list"""
    lst = []
    while num:
        num, last = num // 10, num % 10
        lst.append(last)
    lst = lst[::-1]
    return lst


def adder(x, y):
    """ Adds y into x for lists of digits x and y representing positive numbers.
    >>> a =[3, 4, 5]
    >>> adder(a, [5, 5])
    [4, 0, 0]
    >>> adder(a, [8, 3, 4])
    [1, 2, 3, 4]
    >>> adder(a, [3, 3, 3, 3, 3])
    [3, 4, 5, 6, 7]
    """
    carry, i = 0, len(x) - 1
    for d in reversed([0] + y):
        if i < 0:
            x.insert(0, 0)
            i = 0
        total = carry + x[i] + d
        carry, num = total // 10, total % 10
        x[i] = num
        i -= 1
    if x[0] == 0:
        x.remove(0)
    return x


# def multiples(k, s):
#     """Return a linked list of all multiples of k seletcted from digits in s
#     >>> odds = Link(1, Link(3, Link(5, Link(7, Link(9)))))
#     >>> multiples(5, odds)
#     Link(135, Link(15, Link(35)))
#     >>> multiples(7, odds)
#     Link(1379, Link(357, Link(35)))
#     >>> multiples(9, odds)
#     Link(1359m Link(135))
#     >>> multiples(2, odds)
#     ()
#     """
#     t = Link.empty
#     if s is Link.empty:
#         return Link.empty
#     else:
#
#     return t



#################
##### Final #####
#################

