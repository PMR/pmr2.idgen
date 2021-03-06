from unittest import TestSuite, makeSuite
from Testing import ZopeTestCase as ztc

import zope.component

from pmr2.idgen.interfaces import *

from Zope2.App import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup, onteardown


@onsetup
def setup():
    import pmr2.idgen
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', pmr2.idgen)
    fiveconfigure.debug_mode = False
    ztc.installPackage('pmr2.idgen')

@onteardown
def teardown():
    pass

setup()
teardown()
ptc.setupPloneSite(products=('pmr2.idgen',))


class TestCase(ptc.PloneTestCase):
    pass
