class NameException(Exception):
    """Raised if name is too long or too short.
    """


class NameChecked(type):
    """Check for too long method names.
    """

    def __init__(cls, name, bases, cdict):
        for name, value in cdict.items():
            if (hasattr(value, '__call__')):
                name_len = len(name)
                if name_len > 30:
                    msg = 'The name "%s" is too long.\n' % name
                    msg += 'Only 30 characters are allowed'
                    msg += ' but it is %d characters long.' % name_len
                    raise NameException(msg)
        super(NameChecked, cls).__init__(name, bases, cdict)


if __name__ == '__main__':

    class Test:
        """Test class other meta class than type.
        """
        __metaclass__ = NameChecked

        def meth1(self):
            """Test method with short name.
            """
            pass

        def method_with_a_very_long_name_that_is_not_allowed(self):
            """Test method with too long name.
            """
            pass
