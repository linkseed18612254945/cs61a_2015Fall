from lab04 import *

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    if not lst:
        return []
    elif type(lst[0]) is not list:
        return [lst[0]] + flatten(lst[1:])
    else:
        return flatten(lst[0]) + flatten(lst[1:])




# Q13
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    new_lst = []

    while lst1 and lst2:
        if lst1[0] > lst2[0]:
            new_lst.append(lst2[0])
            lst2 = lst2[1:]
        else:
            new_lst.append(lst1[0])
            lst1 = lst1[1:]
    if lst1:
        new_lst += lst1
    else:
        new_lst += lst2
    return new_lst


