"""Requirements
We want values of Point to be always integer.
For that, we need validator, but we do not want to repeat setter and getter
"""

from random import seed, choices


class Choices:
    """
    read only data cuz __set__ is not implemented
    same as
    @property
    def hoge():
        return choices(self.choices)
    """

    def __init__(self, *choices_):
        self.choices = choices_

    def __get__(self, instance, owner):
        return choices(self.choices)


class Deck:
    suit = Choices('Diamond', 'Heart', 'Spade', 'Club')
    card = Choices(*'23456789JQKA', '10')


class Dice:
    d_1 = Choices(*'123456')
    d_2 = Choices(*'123456')
    d_3 = Choices(*'123456')


if __name__ == '__main__':
    seed(0)
    d = Deck()
    print('start')
    for _ in range(10):
        print(d.card, d.suit)
    print('end')

    print('lets roll dice')
    dice = Dice()
    print('start')
    for _ in range(3):
        print(dice.d_1, dice.d_2, dice.d_3)
    print('end')
