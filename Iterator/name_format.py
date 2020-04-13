from collections import namedtuple
from typing import List

Person = namedtuple('Name', 'last first')


class PersonNames:

    def __init__(self, persons: List[Person]):
        self._persons = [
            person.last + ' ' + person.first
            for person in persons
        ]

    def __iter__(self):
        return iter(self._persons)


if __name__ == '__main__':
    li = [
        Person('Hoshito', 'Furuno'),
        Person('Tanaka', 'Taro')
    ]
    person_names = PersonNames(li)

    # Now we can user 'for' because person_names is iterable
    for name in person_names:
        print(name)
