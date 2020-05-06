from datetime import datetime


class TimeUTC:
    def __get__(self, instance, owner):
        print(f'__get__ called. self={self}, instance={instance}, owner_class={owner}')
        return datetime.utcnow().isoformat()


class Logger1:
    current_time = TimeUTC()


class Logger2:
    current_time = TimeUTC()


class PropertyLikeTimeUTC:
    def __get__(self, instance, owner):
        if instance is None:
            """More consistent to property this way"""
            return self
        return datetime.utcnow().isoformat()


class Logger3:
    current_time = PropertyLikeTimeUTC()


class Logger4:
    @property
    def current_time(self):
        return datetime.utcnow().isoformat()


if __name__ == '__main__':
    print('instance will be None because it is called before instantiating')
    print('owner class should be logger1', getattr(Logger1, 'current_time'))
    print('owner class should be logger2', getattr(Logger2, 'current_time'))

    print('instance will NOT be None because it is instantiated')
    l1 = Logger1()
    l2 = Logger2()
    print('owner class should be logger1', l1.current_time)
    print('owner class should be logger2', l2.current_time)

    print('PropertyLikeTimeUTC')
    print('Logger3.current_time(not instance)', Logger3.current_time)
    print('Logger4.current_time(not instance)', Logger4.current_time)

    print('Logger3().current_time(instance)', Logger3().current_time)
    print('Logger4().current_time(instance)', Logger4().current_time)
