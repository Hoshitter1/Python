"""
Use __set_name__ which was introduced since Python3.6 has released.
This will solve all the problems of descriptor 5
"""


class ValidString:

    def __init__(self, min_length=None):
        self.min_length = min_length

    def __set_name__(self, owner, name):
        print(f'__set_name__: owner={owner}, name={name}')
        self.property_name = name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be string')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(
                f'length of {self.property_name} must be at least {self.min_length}'
            )
        # To avoid infinite recursion
        # or you can bypass by instance.__dict__[self.property] = value
        key = '_' + self.property_name
        setattr(instance, key, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        key = '_' + self.property_name
        return getattr(instance, key)


class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)


if __name__ == '__main__':
    p = Person()
    p.first_name = 'hoshito'
    p.last_name = 'furuno'
    print(p.__dict__)
    p.first_name = 'tanaka'
    p.last_name = 'taro'
    print(p.__dict__)

    try:
        p.first_name = ''
    except ValueError as e:
        print(e)
