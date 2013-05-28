import zope.component
import zope.interface
import zope.schema

from persistent import Persistent
from zope.annotation import factory, IAttributeAnnotatable
from zope.container.contained import Contained

from pmr2.idgen.interfaces import IIdGenerator
from pmr2.idgen.interfaces import IAutoinc, IAutoincHex

from pmr2.idgen.base import BaseIdGenerator


class AutoincAnnotation(Persistent, Contained, BaseIdGenerator):
    """
    A naive implementation of an autoincrement counter.
    """

    zope.interface.implements(IAutoinc)
    zope.component.adapts(IAttributeAnnotatable)

    value = zope.schema.fieldproperty.FieldProperty(IAutoinc['value'])

    def next(self):
        self.value = self.value + 1
        return str(self.value)

Autoinc = factory(AutoincAnnotation)


class AutoincHexAnnotation(AutoincAnnotation):
    """
    Same as Autoinc, but returns hex instead of int.
    """

    zope.interface.implements(IAutoincHex)

    value = zope.schema.fieldproperty.FieldProperty(IAutoincHex['value'])

    def next(self):
        super(AutoincHexAnnotation, self).next()
        return '%x' % self.value

AutoincHex = factory(AutoincHexAnnotation)
