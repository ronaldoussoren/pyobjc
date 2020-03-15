import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBAdvertisementData(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBDescriptor, objc.objc_class)
        self.assertIsInstance(CoreBluetooth.CBMutableDescriptor, objc.objc_class)
