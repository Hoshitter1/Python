class IntegerField:
    def __set_name__(self, owner, name):
        print(f'owner: {owner}')
        print(f'name: {name}')
        self.name = name

    def __get__(self, instance, owner):
        print('__get__ called')
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        print('__set__ called')
        if not isinstance(value, int):
            raise TypeError('value must be integer')
        instance.__dict__[self.name] = value


class Point:
    x = IntegerField()
    y = IntegerField()

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    point = Point(1, 2)
    print(f'point.x:{point.x}, point.y{point.y}')
