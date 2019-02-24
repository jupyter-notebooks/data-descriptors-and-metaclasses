"""My docstring is there and long enough.
"""

import re


class NoDocString(Exception):
    """Raised if there is no docstring.
    """


def is_special_method(name, regex=re.compile(r'^__[a-zA-Z\d]+__$')):
    """Find out if method is special, i.e.  __xxx__.
    """
    if regex.match(name):
        return True
    return False


class DocChecked(type):
    """Check for docstring.
    """

    def __init__(cls, name, bases, cdict):
        for name, value in cdict.items():
            if (hasattr(value, '__call__') and
                not is_special_method(name)):
                doc_string = value.__doc__
                if doc_string:
                    doc_len = len(doc_string.strip())
                    if doc_len < 5:
                        print name
                        msg = 'Docstring is too short. '
                        msg += 'Found %d characters.\n' % doc_len
                        msg += 'The minimum lenght is 5 characters.'
                        raise NoDocString(msg)
                else:
                    raise NoDocString('No docstring for %s.' % name)
        super(DocChecked, cls).__init__(name, bases, cdict)

if __name__ == '__main__':

    class Test:
        """Test class other meta class than type.
        """
        __metaclass__ = DocChecked

        def meth1(self):
            """Nice docstring.
            """
            pass

        def meth2(self):
            """void_xx
            """
            pass

        def meth3(self):
            """xxx
            """
            pass

        #def meth4(self):
        #    pass

        #def __add__(self):
        #    pass
