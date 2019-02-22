"""Example usage of a metaclass.

Version for Python 3.
"""

import builtins

# Set this to False to deactive DebugMeta.
DEBUG = True
import sys


if DEBUG:
    class DebugMeta(type):
        """New metaclass.
        """
        names = []
        counter = 0

        def __init__(cls, name, bases, cdict):
            DebugMeta.names.append('%s.%s' % (cls.__module__, name))
            DebugMeta.counter += 1
            print('Debug metaclass in action. %d' % DebugMeta.counter)
            print(DebugMeta.names)
            super(DebugMeta, cls).__init__(name, bases, cdict)

    class new_object(metaclass=DebugMeta):
        """Python 3 class with metaclass keyword argument.
        """
        pass

    builtins.object = new_object
    builtins.type = DebugMeta


class SomeClass1(object):
    """Test class.
    """
    pass


class SomeClass2(object):
    """Test class.
    """
    pass



class SomeClass3():
    """Test class. Does NOT inherit from object.
    """
    pass

