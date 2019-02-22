# coding: utf-8

"""A descriptor works only in a class.

Storing attribute data in `instance.__dict__` can be a solution.
Creating a unique attribute name with the help of `uuid` and
using name mangling with the `__` prefix make things more robust.
"""

from __future__ import print_function

import uuid


class DescriptorInstanceStorage(object):
    """Descriptor that stores attribute data in instances.
    """

    def __init__(self, default=None):
        # unique name with uuid
        self.hidden_name = '__' + uuid.uuid4().hex
        self.default = default

    def __get__(self, instance, owner):
        return getattr(instance, self.hidden_name, self.default)

    def __set__(self, instance, value):
        setattr(instance, self.hidden_name, value)


if __name__ == '__main__':
    class StoreInstance(object):
        """All instances have own `attr`.
        """
        attr = DescriptorInstanceStorage(10)

    store1 = StoreInstance()
    store2 = StoreInstance()
    print('store1', store1.attr)
    print('store2', store2.attr)
    print('Setting store1 only.')
    store1.attr = 100
    print('store1', store1.attr)
    print('store2', store2.attr)
