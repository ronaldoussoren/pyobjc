import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBManager (TestCase):
    def testConstants(self):
        self.assertEqual(CoreBluetooth.CBManagerStateUnknown, 0)
        self.assertEqual(CoreBluetooth.CBManagerStateResetting, 1)
        self.assertEqual(CoreBluetooth.CBManagerStateUnsupported, 2)
        self.assertEqual(CoreBluetooth.CBManagerStateUnauthorized, 3)
        self.assertEqual(CoreBluetooth.CBManagerStatePoweredOff, 4)
        self.assertEqual(CoreBluetooth.CBManagerStatePoweredOn, 5)

if __name__ == "__main__":
    main()
