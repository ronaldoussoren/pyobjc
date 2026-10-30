import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase


class TestCBAdvertisementData(TestCase):
    def test_classes(self):
        self.assertIsInstance(CoreBluetooth.CBDescriptor, objc.objc_class)
        self.assertIsInstance(CoreBluetooth.CBMutableDescriptor, objc.objc_class)
