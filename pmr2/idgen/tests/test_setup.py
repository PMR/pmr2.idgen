from unittest import TestSuite, makeSuite

import zope.component

from pmr2.idgen.interfaces import *
from pmr2.idgen.tests.base import TestCase


class TestProductInstall(TestCase):

    def test_000_IdGeneratorInstalled(self):
        u = zope.component.getUtility(IIdGenerator, 'autoinc')
        self.assert_(IIdGenerator.providedBy(u))


class TestAutoinc(TestCase):

    def test_001_basic(self):
        u = zope.component.getUtility(IIdGenerator, 'autoinc')
        self.assert_(IAutoinc.providedBy(u))
        count = u.next()
        self.assertEqual(count, '1')
        count = u.next()
        self.assertEqual(count, '2')

    def test_002_value_stored(self):
        u = zope.component.getUtility(IIdGenerator, 'autoinc')
        u.next()
        u.next()
        u = zope.component.getUtility(IIdGenerator, 'autoinc')
        count = u.value
        self.assertEqual(count, 2)


class TestAutoincHex(TestCase):

    def test_001_basic(self):
        u = zope.component.getUtility(IIdGenerator, 'autohex')
        self.assert_(IAutoinc.providedBy(u))
        for i in xrange(10):
            u.next()
        u = zope.component.getUtility(IIdGenerator, 'autohex')
        count = u.next()
        self.assertEqual(count, 'b')


def test_suite():
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    suite.addTest(makeSuite(TestAutoinc))
    suite.addTest(makeSuite(TestAutoincHex))
    return suite
