"""
This scripts shows how to solve the issue of descriptor_4

but problem still remains

[Problem]instance may not be hashable
[problem]even if you deleted p1, values still exists
"""


class IntegerValue:
    def __init__(self):
        self.value = {}

    def __set__(self, instance, value):
        self.value[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value.get(instance, None)


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


if __name__ == '__main__':
    p1 = Point2D()
    p2 = Point2D()
    p1.x = 10
    p1.y = 11
    p2.x = 20
    p2.y = 21
    print(p1.x, p1.y)
    print(p2.x, p2.y)
    del p1
    print('[problem]even if you deleted p1, values still exists cuz p2 still has strong reference to the object')
    print(Point2D.x.value, Point2D.y.value)
