import zope.component
import zope.interface
import zope.schema

from persistent import Persistent
from zope.annotation import factory, IAttributeAnnotatable
from zope.app.container.contained import Contained

from pmr2.autoinc.interfaces import ICounter


class CounterAnnotation(Persistent, Contained):
    """
    A naive implementation of an autoincrement counter.
    """

    zope.interface.implements(ICounter)
    zope.component.adapts(IAttributeAnnotatable)

    value = zope.schema.fieldproperty.FieldProperty(ICounter['value'])

    def next(self):
        self.value = self.value + 1
        return self.value

    def last(self):
        return self.value

Counter = factory(CounterAnnotation)
