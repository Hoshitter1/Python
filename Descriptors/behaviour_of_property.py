class Person:

    def get_age(self):
        return getattr(self, '_age')

    def set_age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be integer')
        if value < 0:
            raise ValueError('age must be positive number')
        self._age = value

    age = property(fget=get_age, fset=set_age)


if __name__ == '__main__':
    p = Person()
    print(p.__dict__)
    p.age = 10
    print(p.__dict__)
    p.__dict__['age'] = 100
    print(p.__dict__)
    print('p.age refers to the value of _age instead of age in p.__dict__')
    print(p.age)
