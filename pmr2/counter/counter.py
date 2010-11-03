import zope.interface

from pmr2.counter.interfaces import ICounter


class BaseCounter(object):
    """\
    Base counter
    """

    zope.interface.implements(ICounter)

    def next(self):
        return NotImplementedError
