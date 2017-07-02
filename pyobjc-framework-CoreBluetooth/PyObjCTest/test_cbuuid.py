import sys

from PyObjCTools.TestSupport import *
import CoreBluetooth

class TestCBUUID (TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(CoreBluetooth.CBUUIDCharacteristicExtendedPropertiesString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDCharacteristicUserDescriptionString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDClientCharacteristicConfigurationString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDServerCharacteristicConfigurationString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDCharacteristicFormatString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDCharacteristicAggregateFormatString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDGenericAccessProfileString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDGenericAttributeProfileString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDDeviceNameString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDAppearanceString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDPeripheralPrivacyFlagString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDReconnectionAddressString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDPeripheralPreferredConnectionParametersString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDServiceChangedString, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(CoreBluetooth.CBUUIDCharacteristicValidRangeString, unicode)
        self.assertIsInstance(CoreBluetooth.CBUUIDL2CAPPSMCharacteristicString, unicode)

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBUUID, objc.objc_class)

if __name__ == "__main__":
    main()
