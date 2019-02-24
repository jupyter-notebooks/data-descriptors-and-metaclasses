"""Example usage of a metaclass.

We change the metaclass of classes that in
"""

import sys

try:
    import __builtin__ as builtins
except ImportError:
    import builtins

# Set this to False to deactive DebugMeta.
DEBUG = True

if DEBUG:
    class DebugMeta(type):
        names = []
        counter = 0
        def __init__(cls, name, bases, cdict):
            DebugMeta.names.append('%s.%s' % (cls.__module__, name))
            DebugMeta.counter += 1
            print('Debug metaclass in action. %d' % DebugMeta.counter)
            print(DebugMeta.names)
            super(DebugMeta, cls).__init__(name, bases, cdict)
    # Python 3
    class new_object(metaclass=DebugMeta):
        pass
    # Python 2
    #class new_object:
    #    __metaclass__ = DebugMeta

    builtins.object = new_object

class SomeClass1(object):
    pass

class SomeClass2(object):
    pass

class SomeClass3():
    pass

print(SomeClass1.__bases__[0] is SomeClass2.__bases__[0])