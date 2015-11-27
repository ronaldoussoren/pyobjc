import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBAdvertisementData (TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBCharacteristic, objc.objc_class)
        self.assertIsInstance(CoreBluetooth.CBMutableCharacteristic, objc.objc_class)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyBroadcast, 0x01)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyRead, 0x02)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyWriteWithoutResponse, 0x04)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyWrite, 0x08)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyNotify, 0x10)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyIndicate, 0x20)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyAuthenticatedSignedWrites, 0x40)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyExtendedProperties,  0x80)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyNotifyEncryptionRequired, 0x100)
        self.assertEqual(CoreBluetooth.CBCharacteristicPropertyIndicateEncryptionRequired, 0x200)

        self.assertEqual(CoreBluetooth.CBAttributePermissionsReadable,0x01)
        self.assertEqual(CoreBluetooth.CBAttributePermissionsWriteable,0x02)
        self.assertEqual(CoreBluetooth.CBAttributePermissionsReadEncryptionRequired,0x04)
        self.assertEqual(CoreBluetooth.CBAttributePermissionsWriteEncryptionRequired,0x08)


    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(CoreBluetooth.CBCharacteristic.isBroadcasted)
        self.assertResultIsBOOL(CoreBluetooth.CBCharacteristic.isNotifying)

if __name__ == "__main__":
    main()
