import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBCentralManager (TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertHasAttr(CoreBluetooth, "CBCentralManager")
        self.assertIsInstance(CoreBluetooth.CBCentralManager, objc.objc_class)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnknown, 0)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateResetting, 1)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnsupported, 2)
        self.assertEqual(CoreBluetooth.CBCentralManagerStateUnauthorized, 3)
        self.assertEqual(CoreBluetooth.CBCentralManagerStatePoweredOff, 4)
        self.assertEqual(CoreBluetooth.CBCentralManagerStatePoweredOn, 5)

    @min_os_level("10.9")
    def testProtocols(self):
        self.assertIsInstance(objc.protocolNamed("CBCentralManagerDelegate"), objc.formal_protocol)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertResultIsBOOL(CoreBluetooth.CBCentralManager.isScanning)

if __name__ == "__main__":
    main()
