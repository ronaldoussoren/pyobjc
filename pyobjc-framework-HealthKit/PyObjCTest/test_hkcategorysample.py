from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKCategorySample(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathCategoryValue, str)
