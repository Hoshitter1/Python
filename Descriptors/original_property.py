"""
Meaning of property method:
* Allows you to implement validation when calling or setting attribute like this hoge.age = 10
but there is a problem
* when there is attributes that have to be validated in the same way, you have to write property repeatedly
Solution:
*Create your original property!
"""


class MyProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner, name):
        """this is called when a name in a class is assigned to this class"""
        print('__set_name__ called')
        self.property_name = name

    def __get__(self, instance, owner):
        print('__get__ called')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.property_name} is not readable')
        return self.fget(instance)

    def __set__(self, instance, value):
        print('__set__ called')
        """Add validation here"""
        if self.fset is None:
            raise AttributeError('{}')
        self.fset(instance, value)

    def setter(self, fset):
        self.fset = fset
        return self


class Person:

    def get_age(self):
        return getattr(self, '_age')

    def set_age(self, value):
        self._age = value

    age = MyProperty(fget=get_age, fset=set_age)


class Person2:

    @MyProperty
    def age(self):
        return getattr(self, '_age')

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    p = Person()
    print(p.__dict__)
    p.age = 10
    print(p.__dict__)
    p.__dict__['age'] = 100
    print(p.age)

    p2 = Person2()
    print(p2.__dict__)
    p2.age = 10
    print(p2.__dict__)
    p2.__dict__['age'] = 100
    print(p2.age)
