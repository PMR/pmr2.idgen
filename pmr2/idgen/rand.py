from random import getrandbits

from pmr2.idgen.base import BaseIdGenerator


class Hex128bit(BaseIdGenerator):
    """
    Random 128 bit hex string
    """

    def next(self):
        return '%032x' % getrandbits(128)
