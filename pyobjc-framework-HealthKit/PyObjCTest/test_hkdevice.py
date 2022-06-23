from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKDevice(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKDevicePropertyKeyName, str)
        self.assertIsInstance(HealthKit.HKDevicePropertyKeyManufacturer, str)
        self.assertIsInstance(HealthKit.HKDevicePropertyKeyModel, str)
        self.assertIsInstance(HealthKit.HKDevicePropertyKeyHardwareVersion, str)
        self.assertIsInstance(HealthKit.HKDevicePropertyKeyFirmwareVersion, str)
        self.assertIsInstance(HealthKit.HKDevicePropertyKeySoftwareVersion, str)
        self.assertIsInstance(HealthKit.HKDevicePropertyKeyLocalIdentifier, str)
        self.assertIsInstance(HealthKit.HKDevicePropertyKeyUDIDeviceIdentifier, str)
