import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBCentral(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertHasAttr(CoreBluetooth, "CBCentral")
        self.assertIsInstance(CoreBluetooth.CBCentral, objc.objc_class)
