class DefaultValue:
    def __init__(self, def_val):
        self._def_val = def_val
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f'self.count: {self.count}')
        return self._def_val


MISSING_COUNT = 0


def default_value():
    global MISSING_COUNT
    MISSING_COUNT += 1
    print(f'MISSING_COUNT: {MISSING_COUNT}')
    return None


if __name__ == '__main__':
    from collections import defaultdict

    print('when key is missing, a callable object will be called')

    print('function is originally callable')
    dd = defaultdict(default_value)
    print(dd['a'])
    print(dd['b'])

    print('class that has callable attribute')
    dv_2 = DefaultValue(None)
    dd_2 = defaultdict(dv_2)
    print(dd_2['a'])
    print(dd_2['b'])
    dd_2['b'] = 100
    print(dd_2['b'])
