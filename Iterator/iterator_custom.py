class Cities:

    def __init__(self):
        self.cities = ['Tokyo', 'Osaka', 'Fukuoka']

    def __len__(self):
        return len(self.cities)

    def __iter__(self):
        # Create new instance of iterator so data won't be exhausted
        return self.CityIterator(self)

    def __getitem__(self, item):
        # For slicing
        return self.cities[item]

    class CityIterator:
        """List data will not be exhausted by implementing this"""

        def __init__(self, city_obj):
            self.city_obj_ = city_obj
            self.index = 0

        def __next__(self):
            if self.index >= len(self.city_obj_):
                raise StopIteration
            result = self.city_obj_.cities[self.index]
            self.index += 1
            return result

        def __iter__(self):
            return self


if __name__ == '__main__':

    cities = Cities()

    print('0')
    print(cities[0])

    print('1')
    for city in cities:
        print(city)

    # list will not be exhausted
    print('2')
    for city in cities:
        print(city)

    print('3')
    for city in cities:
        print(city)
