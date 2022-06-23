from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKQuantitySample(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.KPredicateKeyPathQuantity, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathCount, str)
