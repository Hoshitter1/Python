"""
In many cases, we can derive most of the rich comparisons from just two base ones: the __eq__ and one other one,
maybe __lt__, or __le__, etc.

For example, if == and < is defined, then:

a <= b is a == b or a < b
a > b is b < a
a >= b is a == b or b < a
a != b is not(a == b)
On the other hand if we define == and <=, then:

a < b is a <= b and not(a == b)
a >= b is b <= a
a > b is b <= a and not(b == a)
a != b is not(a == b)
"""

from functools import total_ordering


@total_ordering
class Number:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f'Number(x={self.x})'

    def __eq__(self, other):
        print('eq called....')
        if isinstance(other, tuple):
            other = Number(*other)
        if isinstance(other, Number):
            return self.x == other.x
        return NotImplementedError

    def __lt__(self, other):
        print('__lt__ called...')
        if isinstance(other, Number):
            return self.x < other.x
        return NotImplementedError


if __name__ == '__main__':
    v1 = Number(0)
    v2 = Number(0)
    v3 = Number(10)
    print(v1 == v2)
    print(v1 == (0,))
    print(v1 == (1,))
