import CoreBluetooth
from PyObjCTools.TestSupport import TestCase


class TestCBAdvertisementData(TestCase):
    def test_constants(self):
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
