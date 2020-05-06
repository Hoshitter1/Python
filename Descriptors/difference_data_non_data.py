class DataDescriptor:
    def __set__(self, instance, value):
        print('__set__ called')

    def __get__(self, instance, owner):
        print('__get__ called')


class NonDataDiscriptor:
    def __get__(self, instance, owner):
        print('__get__ called')


class DataTest:
    name = DataDescriptor()


class NonDataTest:
    name = NonDataDiscriptor()


if __name__ == '__main__':
    d1 = DataTest()
    print(f'd={d1.__dict__}')
    print(f'd1.name={d1.name}')
    d1.__dict__['name'] = 'Hello'
    print(f'd={d1.__dict__}')
    print(d1.name)

    print('*' * 3)
    d2 = NonDataTest()
    print(f'd={d2.__dict__}')
    print(f'd2.name={d2.name}')
    d2.__dict__['name'] = 'Hello'
    print(f'd={d2.__dict__}')
    print(d2.name)
    print('This way(non data descriptor) __get__ does not get called')
