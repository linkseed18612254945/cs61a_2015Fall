from lab07 import *

# Q5
def cumulative_sum(t):
    """Return a new Tree, where each entry is the sum of all entries in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    if t.is_leaf():
        return t
    else:
        return Tree(t.tree_sum(), [cumulative_sum(subtree) for subtree in t.branches])


# Q6
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    """
    if not lst:
        return Link.empty
    else:
        return Link(lst[0], list_to_link(lst[1:]))




# Q7
def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    if link == Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)



# Q8
def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> new = reverse(link)
    >>> print_link(new)
    <4 3 2 1>
    >>> print_link(link)
    <1 2 3 4>
    """
    if link == Link.empty:
        return Link.empty
    elif link.rest == Link.empty:
        return link
    else:
        return reverse(link.rest).link_append(link.first)

    # Iter Version

    # if link == Link.empty:
    #     return link
    # new = Link(link.first)
    # while link.rest != Link.empty:
    #     link = link.rest
    #     new = Link(link.first, new)
    # return new


# Q9
def deep_map(f, link):
    """Return a Link with the same structure as link but with fn mapped over
    its elements. If an element is an instance of a linked list, recursively
    apply f inside that linked list as well.

    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print_link(deep_map(lambda x: x * x, s))
    <1 <4 9> 16>
    >>> print_link(s) # unchanged
    <1 <2 3> 4>
    >>> print_link(deep_map(lambda x: 2 * x, Link(s, Link(Link(Link(5))))))
    <<2 <4 6> 8> <<10>>>
    """
    if link is Link.empty:
        return link
    if isinstance(link.first, Link):
        first = deep_map(f, link.first)
    else:
        first = f(link.first)
    return Link(first, deep_map(f, link.rest))

# Q10
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    links = set()
    while link != Link.empty:
        if link in links:
            return True
        else:
            links.add(link)
            link = link.rest
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"

