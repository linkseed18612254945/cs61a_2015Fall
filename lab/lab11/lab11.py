#############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next = start

    def __next__(self):
        if self.next > self.end:
            raise StopIteration
        else:
            result = self.next
            self.next += 1
            return result

    def __iter__(self):
        return self.__init__(self.start, self.end)


# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    def __init__(self, string):
        self.string = string
        self.len = len(string)
        self.index = 0

    def __next__(self):
        if self.index >= self.len:
            raise StopIteration
        else:
            result = self.string[self.index]
            self.index += 1
            return result

    def __iter__(self):
        return self


##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    start = n
    while start >= 0:
        yield start
        start -= 1

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self, n):
        self.start = n

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        else:
            result = self.start
            self.start -= 1
            return result

    def __iter__(self):
        return self

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n > 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    yield n


