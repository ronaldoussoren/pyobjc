from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKActivitySummary(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathDateComponents, str)

    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKActivitySummary.isPaused)
        self.assertArgIsBOOL(HealthKit.HKActivitySummary.setPaused_, 0)
