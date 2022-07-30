from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKObject(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathUUID, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathSource, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathMetadata, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathCorrelation, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkout, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathDevice, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathSourceRevision, str)
