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

if __name__ == "__main__":
    main()
