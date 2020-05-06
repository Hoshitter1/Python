class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f'Person(name={self.name})'


if __name__ == '__main__':
    person1 = Person('hoshito')
    person2 = Person('hoshito')
    print(person1 == person2)
    print(hash(person1), hash(person2))

    # Now you can put person instance into dict as key
    # because it's hashable
    d1 = {person1: 'hoshito'}
    print(d1)
