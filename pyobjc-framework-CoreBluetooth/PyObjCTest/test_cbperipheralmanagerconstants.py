import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBAdvertisementData (TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(CoreBluetooth.CBPeripheralManagerOptionShowPowerAlertKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBPeripheralManagerOptionRestoreIdentifierKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBPeripheralManagerRestoredStateServicesKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBPeripheralManagerRestoredStateServicesKey, unicode)

if __name__ == "__main__":
    main()
