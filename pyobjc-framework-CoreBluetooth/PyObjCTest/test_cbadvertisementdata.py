import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBAdvertisementData (TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataLocalNameKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataTxPowerLevelKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataServiceUUIDsKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataServiceDataKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataManufacturerDataKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataOverflowServiceUUIDsKey, unicode)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataIsConnectable, unicode)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataSolicitedServiceUUIDsKey, unicode)

if __name__ == "__main__":
    main()
