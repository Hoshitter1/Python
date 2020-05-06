"""
This scripts shows how to solve the issue of descriptor_3


"""


class IntegerValue:
    def __init__(self, name):
        self.storage_name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)


class Point1D:
    x = IntegerValue('x')


class Point2D:
    # [Problem1]this approach works but x and y is very repetitive
    # [Problem2]__slot__ does not work
    # [Problem3]user can access to _x and not sure how to define(someone might try _x when defining)
    # [Problem4]instance may not be hashable
    x = IntegerValue('x')
    y = IntegerValue('y')


if __name__ == '__main__':
    p1 = Point1D()
    p2 = Point1D()
    p1.x = 10
    p2.x = 20
    print(p1.x, p2.x)

    p1 = Point2D()
    p2 = Point2D()
    p1.x = 10
    p1.y = 11
    p2.x = 20
    p2.y = 21
    print(p1.x, p1.y)
    print(p2.x, p2.y)
