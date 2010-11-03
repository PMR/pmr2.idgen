import zope.component
import zope.interface
import zope.schema

from persistent import Persistent
from zope.annotation import factory, IAttributeAnnotatable
from zope.app.container.contained import Contained

from pmr2.counter.interfaces import ICounter
from pmr2.counter.interfaces import IAutoinc

from pmr2.counter.counter import BaseCounter


class AutoincAnnotation(Persistent, Contained, BaseCounter):
    """
    A naive implementation of an autoincrement counter.
    """

    zope.interface.implements(IAutoinc)
    zope.component.adapts(IAttributeAnnotatable)

    value = zope.schema.fieldproperty.FieldProperty(IAutoinc['value'])

    def next(self):
        self.value = self.value + 1
        return self.value

Autoinc = factory(AutoincAnnotation)
