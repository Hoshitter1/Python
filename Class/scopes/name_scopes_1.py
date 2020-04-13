"""
Scopes of global, class, methods.
"""

name = 'Hoshito'


class Foo:
    name = 'Tanaka'
    list_1 = [name] * 3
    list_2 = [name for i in range(3)]


if __name__ == '__main__':
    # Calls name inside of class
    print(Foo.list_1)
    # Calls name from global scope because comprehension is a function
    print(Foo.list_2)
