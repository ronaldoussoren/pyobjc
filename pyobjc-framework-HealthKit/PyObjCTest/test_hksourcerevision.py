from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKSourceRevision(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKSourceRevisionAnyVersion, str)
        self.assertIsInstance(HealthKit.HKSourceRevisionAnyProductType, str)

        self.assertIsInstance(
            HealthKit.HKSourceRevisionAnyOperatingSystem,
            HealthKit.NSOperatingSystemVersion,
        )
