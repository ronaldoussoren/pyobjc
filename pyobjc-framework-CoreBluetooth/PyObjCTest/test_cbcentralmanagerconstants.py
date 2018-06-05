import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBCentral (TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(CoreBluetooth.CBCentralManagerOptionShowPowerAlertKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBCentralManagerScanOptionAllowDuplicatesKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBCentralManagerScanOptionSolicitedServiceUUIDsKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBConnectPeripheralOptionNotifyOnDisconnectionKey, unicode)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(CoreBluetooth.CBCentralManagerOptionRestoreIdentifierKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBConnectPeripheralOptionNotifyOnConnectionKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBConnectPeripheralOptionNotifyOnNotificationKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBCentralManagerRestoredStatePeripheralsKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBCentralManagerRestoredStateScanServicesKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBCentralManagerRestoredStateScanOptionsKey, unicode)


    @min_os_level("10.14")
    def testConstants10_14(self):
        # XXX: This is currently documented as a 10.13 constant, but isn't available there
        self.assertIsInstance(CoreBluetooth.CBConnectPeripheralOptionStartDelayKey, unicode)

if __name__ == "__main__":
    main()
