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

    def expression(self):
        if not self.rest:
            return ''
        else:
            expr = str(self.value) + ' ' + self.rest.expression()
        return expr.strip()

class Exp(object):
    """A call expression in Calculator."""
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return '({0} {1})'.format(self.operator, self.operand.expression())


