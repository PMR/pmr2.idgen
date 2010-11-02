from unittest import TestSuite, makeSuite

import zope.component

from pmr2.autoinc.interfaces import *
from pmr2.autoinc.tests.base import TestCase


class TestProductInstall(TestCase):

    def test_000_CounterInstalled(self):
        u = zope.component.getUtility(ICounter)
        self.assert_(ICounter.providedBy(u))

    def test_001_CounterUsable(self):
        u = zope.component.getUtility(ICounter)
        count = u.next()
        self.assertEqual(count, 1)
        count = u.next()
        self.assertEqual(count, 2)

    def test_002_CounterLast(self):
        u = zope.component.getUtility(ICounter)
        u.next()
        u.next()
        u = zope.component.getUtility(ICounter)
        count = u.last()
        self.assertEqual(count, 2)


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    return suite
