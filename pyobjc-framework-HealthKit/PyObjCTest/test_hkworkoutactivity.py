from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKWorkoutActivity(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutActivityType, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutActivityDuration, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutActivityStartDate, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutActivityEndDate, str)
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathWorkoutActivitySumQuantity, str
        )
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathWorkoutActivityMinimumQuantity, str
        )
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathWorkoutActivityMaximumQuantity, str
        )
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathWorkoutActivityAverageQuantity, str
        )
