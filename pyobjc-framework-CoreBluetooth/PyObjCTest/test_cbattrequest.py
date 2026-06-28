import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase


class TestFinderSync(TestCase):
    def test_classes(self):
        self.assertHasAttr(CoreBluetooth, "CBATTRequest")
        self.assertIsInstance(CoreBluetooth.CBATTRequest, objc.objc_class)
