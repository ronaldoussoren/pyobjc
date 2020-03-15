import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBService(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBService, objc.objc_class)
        self.assertIsInstance(CoreBluetooth.CBMutableService, objc.objc_class)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(CoreBluetooth.CBService.isPrimary)
        self.assertResultIsBOOL(CoreBluetooth.CBMutableService.isPrimary)
        self.assertArgIsBOOL(CoreBluetooth.CBMutableService.initWithType_primary_, 1)
