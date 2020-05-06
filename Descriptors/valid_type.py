class ValidType:
    def __init__(self, type_):
        self._type = type_

    def __set_name__(self, owner, name):
        self.property_name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{self.property_name} must be of type {self._type.__name__}')
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)


class Person:
    first_name = ValidType(str)
    last_name = ValidType(str)
    age = ValidType(int)
    height = ValidType(float)
    favourite_foods = ValidType(list)
    customized_data = ValidType(dict)


if __name__ == '__main__':
    p = Person()
    print(p.__dict__)
    try:
        p.first_name = 'hoshito'
    except ValueError as e:
        print(e)
    print(p.__dict__)
    print(p.age)
    print(p.last_name)
