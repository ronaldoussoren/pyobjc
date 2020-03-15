import CoreBluetooth
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBAdvertisementData(TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataLocalNameKey, str)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataTxPowerLevelKey, str)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataServiceUUIDsKey, str)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataServiceDataKey, str)
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataManufacturerDataKey, str)
        self.assertIsInstance(
            CoreBluetooth.CBAdvertisementDataOverflowServiceUUIDsKey, str
        )
        self.assertIsInstance(CoreBluetooth.CBAdvertisementDataIsConnectable, str)
        self.assertIsInstance(
            CoreBluetooth.CBAdvertisementDataSolicitedServiceUUIDsKey, str
        )
