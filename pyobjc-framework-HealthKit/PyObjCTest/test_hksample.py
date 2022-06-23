from PyObjCTools.TestSupport import TestCase
import HealthKit


class TetstHKSample(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKSampleSortIdentifierStartDate, str)
        self.assertIsInstance(HealthKit.HKSampleSortIdentifierEndDate, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathStartDate, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathEndDate, str)

    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKSample.hasUndeterminedDuration)
