class Product:

    def __init__(self, name, created):
        self.name = name
        self.created = created

    def __repr__(self):
        print('__repl__ called')
        return f'Product(name={self.name}, created={self.created})'

    def __str__(self):
        print('__str__ called')
        return f'Product(name={self.name})'

    def __format__(self, format_spec):
        print('__format__ called')
        created = format(self.created, format_spec)
        return f'Product(name={self.name}, created={created})'


if __name__ == '__main__':
    # e.g 1
    float_var = 0.12
    print(format(float_var, '.20f'))
    # e.g 2
    from datetime import datetime, date

    now = datetime.utcnow()
    print(now)
    print(format(now, '%a %Y-%m-%d %I:%M %p'))

    product = Product('Hoshito', date(1995, 5, 25))
    print('str(product):', str(product))
    print('str(product)', repr(product))
    print('format(product)', format(product, '%B %d %Y'))
