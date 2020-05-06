class PersonDict:
    pass


def manipulate_dict():
    p = PersonDict()
    p.name = 'Hoshito'
    print(p.name)
    del p.name


class PersonSlot:
    """you cannot monkey patch later this way
    and causes difficulties in multiple inheritance
    """
    __slots__ = ('name',)


def manipulate_slot():
    p = PersonSlot()
    p.name = 'Hoshito'
    print(p.name)
    del p.name


if __name__ == '__main__':
    from time import perf_counter

    start = perf_counter()
    manipulate_dict()
    end = perf_counter()
    elapsed = end - start
    print(f'elapsed: {elapsed}')

    print('More efficiently works')
    start = perf_counter()
    manipulate_slot()
    end = perf_counter()
    elapsed = end - start
    print(f'elapsed: {elapsed}')
