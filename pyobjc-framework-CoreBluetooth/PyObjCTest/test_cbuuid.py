import CoreBluetooth
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCBUUID(TestCase):
    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(
            CoreBluetooth.CBUUIDCharacteristicExtendedPropertiesString, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBUUIDCharacteristicUserDescriptionString, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBUUIDClientCharacteristicConfigurationString, str
        )
        self.assertIsInstance(
            CoreBluetooth.CBUUIDServerCharacteristicConfigurationString, str
        )
        self.assertIsInstance(CoreBluetooth.CBUUIDCharacteristicFormatString, str)
        self.assertIsInstance(
            CoreBluetooth.CBUUIDCharacteristicAggregateFormatString, str
        )
        self.assertIsInstance(CoreBluetooth.CBUUIDGenericAccessProfileString, str)
        self.assertIsInstance(CoreBluetooth.CBUUIDGenericAttributeProfileString, str)
        self.assertIsInstance(CoreBluetooth.CBUUIDDeviceNameString, str)
        self.assertIsInstance(CoreBluetooth.CBUUIDAppearanceString, str)
        self.assertIsInstance(CoreBluetooth.CBUUIDPeripheralPrivacyFlagString, str)
        self.assertIsInstance(CoreBluetooth.CBUUIDReconnectionAddressString, str)
        self.assertIsInstance(
            CoreBluetooth.CBUUIDPeripheralPreferredConnectionParametersString, str
        )
        self.assertIsInstance(CoreBluetooth.CBUUIDServiceChangedString, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(CoreBluetooth.CBUUIDCharacteristicValidRangeString, str)
        self.assertIsInstance(CoreBluetooth.CBUUIDL2CAPPSMCharacteristicString, str)

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(CoreBluetooth.CBUUID, objc.objc_class)
