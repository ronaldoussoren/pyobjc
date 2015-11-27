import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBAdvertisementData (TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusNotDetermined, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusRestricted, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusDenied, 2)
        self.assertEqual(CoreBluetooth.CBPeripheralAuthorizationStatusAuthorized, 3)

        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnknown, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateResetting, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnsupported, 2)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStateUnauthorized, 3)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStatePoweredOff, 4)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerStatePoweredOn, 5)

        self.assertEqual(CoreBluetooth.CBPeripheralManagerConnectionLatencyLow, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerConnectionLatencyMedium, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralManagerConnectionLatencyHigh, 2)

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBPeripheralManager, objc.objc_class)

    @min_os_level("10.9")
    def testProtocols(self):
        self.assertIsInstance(objc.protocolNamed("CBPeripheralManagerDelegate"), objc.formal_protocol)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(CoreBluetooth.CBPeripheralManager.isAdvertising)
        self.assertResultIsBOOL(CoreBluetooth.CBPeripheralManager.updateValue_forCharacteristic_onSubscribedCentrals_)

        # XXX: A number of methods have a dispatch_queue as their argument


if __name__ == "__main__":
    main()
