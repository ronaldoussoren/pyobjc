import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase


class TestCBService(TestCase):
    def test_classes(self):
        self.assertIsInstance(CoreBluetooth.CBService, objc.objc_class)
        self.assertIsInstance(CoreBluetooth.CBMutableService, objc.objc_class)

    def test_methods(self):
        self.assertResultIsBOOL(CoreBluetooth.CBService.isPrimary)
        self.assertResultIsBOOL(CoreBluetooth.CBMutableService.isPrimary)
        self.assertArgIsBOOL(CoreBluetooth.CBMutableService.setIsPrimary_, 0)
        self.assertArgIsBOOL(CoreBluetooth.CBMutableService.initWithType_primary_, 1)
