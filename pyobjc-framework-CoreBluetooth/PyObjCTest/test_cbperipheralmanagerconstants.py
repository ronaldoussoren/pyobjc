import CoreBluetooth
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBAdvertisementData(TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(
            CoreBluetooth.CBPeripheralManagerOptionShowPowerAlertKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBPeripheralManagerOptionRestoreIdentifierKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBPeripheralManagerRestoredStateServicesKey, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBPeripheralManagerRestoredStateServicesKey, str
        )
