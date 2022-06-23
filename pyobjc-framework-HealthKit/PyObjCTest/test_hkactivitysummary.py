from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKActivitySummary(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathDateComponents, str)
