"""
How str and repl work
"""


class Foo:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        print('repl called....')
        return f'{self.__class__.__name__}(name={self.name},value={self.value})'

    def __str__(self):
        return self.name


class Hoge:
    pass


if __name__ == '__main__':
    foo = Foo('hoshito', 'bar')
    print(repr(foo))
    print(foo)

    hoge = Hoge()
    print(hoge)
    print(repr(hoge))
