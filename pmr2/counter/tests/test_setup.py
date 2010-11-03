from unittest import TestSuite, makeSuite

import zope.component

from pmr2.counter.interfaces import *
from pmr2.counter.tests.base import TestCase


class TestProductInstall(TestCase):

    def test_000_CounterInstalled(self):
        u = zope.component.getUtility(ICounter, 'autoinc')
        self.assert_(ICounter.providedBy(u))


class TestAutoinc(TestCase):

    def test_001_CounterUsable(self):
        u = zope.component.getUtility(ICounter, 'autoinc')
        self.assert_(IAutoinc.providedBy(u))
        count = u.next()
        self.assertEqual(count, 1)
        count = u.next()
        self.assertEqual(count, 2)

    def test_002_CounterLast(self):
        u = zope.component.getUtility(ICounter, 'autoinc')
        u.next()
        u.next()
        u = zope.component.getUtility(ICounter, 'autoinc')
        count = u.value
        self.assertEqual(count, 2)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    suite.addTest(makeSuite(TestAutoinc))
    return suite
