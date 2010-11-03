import zope.interface

from pmr2.idgen.interfaces import IIdGenerator


class BaseIdGenerator(object):
    """\
    Base counter
    """

    zope.interface.implements(IIdGenerator)

    def next(self):
        return NotImplementedError
