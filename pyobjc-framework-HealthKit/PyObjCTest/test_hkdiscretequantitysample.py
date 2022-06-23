from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKDiscreteQuantitySample(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathMin, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathAverage, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathMax, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathMostRecent, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathMostRecentStartDate, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathMostRecentEndDate, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathMostRecentDuration, str)
