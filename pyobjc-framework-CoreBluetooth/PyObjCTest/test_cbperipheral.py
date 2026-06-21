import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBPeripheral(TestCase):
    @min_os_level("10.9")
    def test_constants(self):
        self.assertIsEnumType(CoreBluetooth.CBPeripheralState)
        self.assertEqual(CoreBluetooth.CBPeripheralStateDisconnected, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralStateConnecting, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralStateConnected, 2)
        self.assertEqual(CoreBluetooth.CBPeripheralStateDisconnecting, 3)

        self.assertIsEnumType(CoreBluetooth.CBCharacteristicWriteType)
        self.assertEqual(CoreBluetooth.CBCharacteristicWriteWithResponse, 0)
        self.assertEqual(CoreBluetooth.CBCharacteristicWriteWithoutResponse, 1)

    @min_os_level("10.9")
    def test_classes(self):
        self.assertIsInstance(CoreBluetooth.CBPeripheral, objc.objc_class)

    @min_os_level("10.9")
    def test_methods(self):
        self.assertArgIsBOOL(
            CoreBluetooth.CBPeripheral.setNotifyValue_forCharacteristic_, 0
        )

    @min_os_level("10.9")
    def test_methods2(self):
        self.assertResultIsBOOL(CoreBluetooth.CBPeripheral.isConnected)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(CoreBluetooth.CBPeripheral.canSendWriteWithoutResponse)

    @min_os_level("10.9")
    def test_protocols(self):
        self.assertProtocolExists("CBPeripheralDelegate", CoreBluetooth)
