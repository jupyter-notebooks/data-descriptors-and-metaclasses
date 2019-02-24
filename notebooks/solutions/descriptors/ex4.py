"""A prices with VAT.
"""


class Total(object):
    """Allow only positive values.
    """

    def __init__(self, rate=1.19):
        self.rate = rate

    def __get__(self, instance, cls):
        return round(instance.net * self.rate, 2)

    def __set__(self, instance, value):
        raise NotImplementedError('Cannot change value.')


class Price(object):
    """A price with VAT.
    """
    total = Total()

    def __init__(self, net):
        self.net = net


class PriceDenmark(object):
    """A price with VAT.
    """
    total = Total(1.25)

    def __init__(self, net):
        self.net = net
        
if __name__ == '__main__':

    def test():
        """Demonstrate how it works.
        """
        price = Price(110)
        print 'Germany', price.total

        price = PriceDenmark(110)
        print 'Denmark', price.total

        # Try to set it.
        price.total = 120

    test()
