"""
How built in method property work
"""


class Person:
    """This is a Person object"""

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('name has to be string')
        if len(name) < 5:
            raise ValueError('name is too short. It can not be that short')
        self._name = name

    def get_name(self):
        """Implement getter and setter so interface will not be affected
        When additional stuff added

        Returns:

        """
        return getattr(self, '_name', None)

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError('name has to be string')
        if len(value) < 5:
            raise ValueError('name is too short. It can not be that short')
        self._name = value

    def del_name(self):
        del self._name

    name = property(fset=set_name, fget=get_name, fdel=del_name, doc="The person's name")


if __name__ == '__main__':
    person = Person('Hoshito')
    print(f'{person.__dict__}')

    del person.name
    print(f'{person.__dict__}')

    if person.name is None:
        person.name = 'Hoshito'
    print(f'{person.__dict__}')

    try:
        person.name = 123
    except TypeError as e:
        print(e)
