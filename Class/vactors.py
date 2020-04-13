from numbers import Real
from math import sqrt


class Vector:
    """This is a class to just see how arithmetic operators and sub work"""

    def __init__(self, *components):
        if len(components) < 1:
            raise ValueError('Component must not be empty')
        for comp in components:
            if not isinstance(comp, Real):
                raise ValueError(
                    'component in vector must be all real number.'
                    f'{comp} is not valid'
                )
        # Just to show it clearly (tuple to tuple)
        self._components = tuple(components)

    @property
    def components(self):
        return self._components

    @staticmethod
    def is_valid_type(vec):
        return isinstance(vec, Vector)

    def is_valid_dimension(self, vec):
        return len(vec) == len(self)

    def __len__(self):
        return len(self._components)

    def __repr__(self):
        return f'Vector({self._components})'

    def __add__(self, other):
        if not self.is_valid_type(other):
            raise NotImplementedError('')
        if not self.is_valid_dimension(other):
            raise NotImplementedError('')
        components = [x + y for x, y in zip(self._components, other.components)]
        return Vector(*components)

    def __sub__(self, other):
        if not self.is_valid_type(other):
            raise NotImplementedError('')
        if not self.is_valid_dimension(other):
            raise NotImplementedError('')
        components = [x - y for x, y in zip(self._components, other.components)]
        return Vector(*components)

    def __mul__(self, other):
        if not isinstance(other, Real):
            raise NotImplementedError('')
        components = [x * other for x in self._components]
        return Vector(*components)

    def __rmul__(self, other):
        """when other * self called..."""
        return self * other

    def __matmul__(self, other):
        print(f'matmul called....other: {other}')

    def __iadd__(self, other):
        """In place operand
        e.g
        l = [1,2]
        l += [2,4]
        not l = l + [2,4] (l will be stored in different memory this way)
        """
        if not self.is_valid_type(other):
            raise NotImplementedError('')
        if not self.is_valid_dimension(other):
            raise NotImplementedError('')
        components = [x + y for x, y in zip(self._components, other.components)]
        self._components = tuple(components)
        return self

    def __neg__(self):
        components = (-x for x in self._components)
        return Vector(*components)

    def __abs__(self):
        return sqrt(sum(x ** 2 for x in self.components))


if __name__ == '__main__':
    vec = Vector(1, 2, 3)
    vec_2 = Vector(5, 6, 9)

    print(vec + vec_2)

    print(vec - vec_2)

    print(vec * 10)

    print(vec.__mul__(10))

    # matmul
    vec @ 3

    # in place
    vec += vec_2
    print(vec)

    print(-vec)

    print(abs(vec))
