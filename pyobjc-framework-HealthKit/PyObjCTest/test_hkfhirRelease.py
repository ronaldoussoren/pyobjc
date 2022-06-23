from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKFHIRRelease(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(HealthKit.HKFHIRRelease, str)
        self.assertIsInstance(HealthKit.HKFHIRReleaseDSTU2, str)
        self.assertIsInstance(HealthKit.HKFHIRReleaseR4, str)
        self.assertIsInstance(HealthKit.HKFHIRReleaseUnknown, str)
