import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestFinderSync(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertHasAttr(CoreBluetooth, "CBATTRequest")
        self.assertIsInstance(CoreBluetooth.CBATTRequest, objc.objc_class)
