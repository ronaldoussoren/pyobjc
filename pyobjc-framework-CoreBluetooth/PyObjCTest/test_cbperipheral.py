import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBPeripheral (TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(CoreBluetooth.CBPeripheralStateDisconnected, 0)
        self.assertEqual(CoreBluetooth.CBPeripheralStateConnecting, 1)
        self.assertEqual(CoreBluetooth.CBPeripheralStateConnected, 2)
        self.assertEqual(CoreBluetooth.CBPeripheralStateDisconnecting, 3)

        self.assertEqual(CoreBluetooth.CBCharacteristicWriteWithResponse, 0)
        self.assertEqual(CoreBluetooth.CBCharacteristicWriteWithoutResponse, 1)

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBPeripheral, objc.objc_class)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertArgIsBOOL(CoreBluetooth.CBPeripheral.setNotifyValue_forCharacteristic_, 0)

    @onlyOn64Bit
    @min_os_level("10.9")
    def testMethods2(self):
        self.assertResultIsBOOL(CoreBluetooth.CBPeripheral.isConnected)

    @onlyOn64Bit
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(CoreBluetooth.CBPeripheral.canSendWriteWithoutResponse)

    @min_os_level("10.9")
    def testProtocols(self):
        self.assertIsInstance(objc.protocolNamed("CBPeripheralDelegate"), objc.formal_protocol)


if __name__ == "__main__":
    main()
