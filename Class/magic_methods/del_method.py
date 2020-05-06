import ctypes


def ref_count(addr):
    return ctypes.c_long.from_address(addr).value


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'

    def __del__(self):
        """this is very difficult to guarantee that this will run"""
        print(f'__del__ called for {self}.....')

    def gen_exception(self):
        raise ValueError('Something went bump...')


if __name__ == '__main__':
    p = Person('Hoshito')
    print('Change the reference so GC(Garvage Collector will destroy it)')
    p_a = None

    print('Lets see the id')
    p_1 = Person('Hoshito')
    p_id = id(p_1)
    print('id:', ref_count(p_id))

    try:
        p_1.gen_exception()
    except ValueError as err:
        ex = err
        print('see err:', err)
    print('out of scope:', ex)

    print('k v of f_locals')
    # Copy needs to be added because it would modify itself as you iterate
    for k, v in ex.__traceback__.tb_frame.f_locals.copy().items():
        if isinstance(v, Person):
            # we have person objects inside of stacktrace
            print(f'key:{k}, value:{v}, id: {id(v)}')
    print('p will be deleted')
    del p
    print('p_1 should be deleted but it does not get deleted')
    print('Especially in jupyter notebook we do not have controls of calling del,'
          'and it goes to standard errro')
    del p_1
    print('end')
