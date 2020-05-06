class MyList:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        """
        if bool is not implemented when bool is called,
        python will look for len instead.
        """
        print('len called')
        return self.length

    def __bool__(self):
        print('bool called')
        return self.length > 0


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        return bool(self.x or self.y)


if __name__ == '__main__':
    ml = MyList(1)
    print(bool(ml))

    p1 = Point(0, 0)
    print(f'p1: {bool(p1)}')

    p2 = Point(1, 1)
    print(f'p2: {bool(p2)}')

    p3 = Point(0, 1)
    print(f'p3: {bool(p3)}')
