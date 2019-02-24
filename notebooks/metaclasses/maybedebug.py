# file: maybedebug.py

"""Test autometa.
"""

import sys


if sys.version_info[0] == 2:
    import autometa_python2 as autometa
else:
    import autometa_python3 as autometa


class MaybeDebug(object):
    """Class that may have a different metaclass.
    """
    pass
