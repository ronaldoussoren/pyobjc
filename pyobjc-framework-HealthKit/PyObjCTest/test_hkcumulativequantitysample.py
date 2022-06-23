from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKCumulativeQuantitySample(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathSum, str)
