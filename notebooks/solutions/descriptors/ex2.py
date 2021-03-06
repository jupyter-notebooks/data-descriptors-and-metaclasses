"""A descriptor that allows only positive values.
"""


class PositiveOnly(object):
    """Allow only positive values.
    """

    def __init__(self):
        self.value = 0

    def __get__(self, instance, cls):
        return round(self.value, 2)

    def __set__(self, instance, value):
        # Use abs here because this requires a number.value
        # 'a' < 0 would work but we don't want this.
        # Numbers only please.
        if value != abs(value):
            raise ValueError('Only positive values are allowed. Got %s.'
                             % value)
        self.value = value


class Number(object):
    """Sample class that uses our descriptor.
    """
    value = PositiveOnly()


if __name__ == '__main__':

    def test():
        """Demonstrate how it works.
        """
        number = Number()
        print number.value
        # This works.
        number.value = 100.565757
        print number.value

    test()
