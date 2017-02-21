## Recursive Objects ##

# Q2
def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print_link(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print_link(link)
    <9001 1 100 2 3>
    """
    assert 0 <= index <= len(link) - 1, IndexError
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    else:
        insert(link.rest, value, index - 1)


# Q4
def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape if they have the same number of branches and each of their
    children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(7)])
    >>> same_shape(t, s)
    False
    """
    if len(t1.branches) != len(t2.branches):
        return False
    else:
        return all([same_shape(subtree1, subtree2)for subtree1, subtree2 in zip(t1.branches, t2.branches)])


# Linked List Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first=0, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def link_to_list(self):
        if self == Link.empty:
            return []
        elif self.rest == Link.empty:
            return [self.first]
        else:
            return [self.first] + self.rest.link_to_list()

    def link_append(self, value):
        if self == Link.empty:
            return Link(value)
        elif self.rest == Link.empty:
            return Link(self.first, Link(value))
        else:
            return Link(self.first, self.rest.link_append(value))

    def deep_map(self, f):
        if self is Link.empty:
            return self
        if isinstance(self.first, Link):
            first = self.fisrt.deep_map(f)
        else:
            first = f(self.first)
        if self.rest is Link.empty:
            return Link(first)
        return Link(first, self.rest.deep_map(f))

    def has_cycle(self):
        base_link = self
        links_set = set()
        while base_link != Link.empty:
            if base_link in links_set:
                return True
            else:
                links_set.add(base_link)
                base_link = base_link.rest
        return False

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

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

