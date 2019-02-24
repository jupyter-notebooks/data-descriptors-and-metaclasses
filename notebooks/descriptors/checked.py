# coding: utf-8

"""Example for descriptor that checks conditions on attributes.
"""
from __future__ import print_function

import uuid


class Checked(object):
    """Descriptor that checks with a user-supplied check function
    if an attribute is valid.
    """

    def __init__(self, checker=None, default=None):
        if checker:
            # checker must be a callable
            checker(default)
        self.hidden_name = '__' + uuid.uuid4().hex
        self.checker = checker
        self.default = default

    def __get__(self, instance, owner):
        return getattr(instance, self.hidden_name, self.default)

    def __set__(self, instance, value):
        if self.checker:
            self.checker(value)
        setattr(instance, self.hidden_name, value)

if __name__ == '__main__':

    def is_int(value):
        """Check if value is and integer.
        """
        if not isinstance(value, int):
            raise ValueError('Int required {} found'.format(type(value)))

    class Restricted(object):
        """Use checked attributes.
        """
        attr1 = Checked(checker=is_int, default=10)
        attr2 = Checked(default=12.5)
        # Setting the default to float, `is_int` raises a `ValueError`.
        try:
            attr3 = Checked(checker=is_int, default=12.5)
        except ValueError:
            print('Cannot set default to float, must be int.')
            attr3 = Checked(checker=is_int, default=12)

    restricted = Restricted()
    print('attr1', restricted.attr1)
    restricted.attr1 = 100
    print('attr1', restricted.attr1)
    try:
        restricted.attr1 = 200.12
    except ValueError:
        print('Cannot set attr1 to float, must be int.')
        restricted.attr1 = 200
