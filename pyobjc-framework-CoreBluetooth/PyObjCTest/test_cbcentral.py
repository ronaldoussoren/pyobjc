import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase


class TestCBCentral(TestCase):
    def test_classes(self):
        self.assertHasAttr(CoreBluetooth, "CBCentral")
        self.assertIsInstance(CoreBluetooth.CBCentral, objc.objc_class)
