# file: autometa_python2.py

"""Example usage of a metaclass.

We change the metaclass of classes that inherit form `object`.
"""

import __builtin__

# Set this to False to deactivate DebugMeta.
DEBUG = True

if DEBUG:
    class DebugMeta(type):
        """Metaclass to be used for debugging.

        """
        names = []
        counter = 0

        def __init__(cls, name, bases, cdict):
            """Store all class names and count how many classes are defined.
            """
            if DebugMeta.counter:
                DebugMeta.names.append('%s.%s' % (cls.__module__, name))
                print 'Debug metaclass in action. %d' % DebugMeta.counter
                print DebugMeta.names
                super(DebugMeta, cls).__init__(name, bases, cdict)
            DebugMeta.counter += 1

    class new_object(object):
        """Replacement for the builtint `object`.
        """
        __metaclass__ = DebugMeta

    # We actually change a builtin.
    # This is a very strong measure.
    __builtin__.object = new_object
    __builtin__.type = DebugMeta


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

import mod1

