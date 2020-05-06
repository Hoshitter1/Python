"""
this script shows the problem of sharing the same object
"""


class CountDown:
    def __init__(self, count):
        self.count = count + 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.count -= 1
        return self.count


class Rocket:
    count = CountDown(10)


if __name__ == '__main__':
    rocket1 = Rocket()
    rocket2 = Rocket()
    print(rocket1.count)
    print(rocket2.count)
