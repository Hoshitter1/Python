"""
How new method and built in type work
"""


class Squared(int):

    def __new__(cls, x):
        # calling object.__new__ is not preferred
        # since you will not inherit __new__ of the parent class
        return super().__new__(cls, x ** 2)

    # calling __init__ causes runtime error(TypeError)
    # lots of builtin method do not use __init__
    # def __init__(self, x):
    #     super.__init__(x)


if __name__ == '__main__':
    result = Squared(2)
    print(result)
