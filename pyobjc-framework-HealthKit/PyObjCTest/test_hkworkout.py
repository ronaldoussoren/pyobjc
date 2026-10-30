from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKWorkout(TestCase):
    def test_enums(self):
        self.assertIsEnumType(HealthKit.HKWorkoutEventType)
        self.assertEqual(HealthKit.HKWorkoutEventTypePause, 1)
        self.assertEqual(HealthKit.HKWorkoutEventTypeResume, 2)
        self.assertEqual(HealthKit.HKWorkoutEventTypeLap, 3)
        self.assertEqual(HealthKit.HKWorkoutEventTypeMarker, 4)
        self.assertEqual(HealthKit.HKWorkoutEventTypeMotionPaused, 5)
        self.assertEqual(HealthKit.HKWorkoutEventTypeMotionResumed, 6)
        self.assertEqual(HealthKit.HKWorkoutEventTypeSegment, 7)
        self.assertEqual(HealthKit.HKWorkoutEventTypePauseOrResumeRequest, 8)

    def test_constants(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutDuration, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutTotalDistance, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutTotalEnergyBurned, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutType, str)
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathWorkoutTotalSwimmingStrokeCount, str
        )
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathWorkoutTotalFlightsClimbed, str
        )
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutSumQuantity, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutMinimumQuantity, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutMaximumQuantity, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutAverageQuantity, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathWorkoutActivity, str)
        self.assertIsInstance(HealthKit.HKWorkoutSortIdentifierDuration, str)
        self.assertIsInstance(HealthKit.HKWorkoutSortIdentifierTotalDistance, str)
        self.assertIsInstance(HealthKit.HKWorkoutSortIdentifierTotalEnergyBurned, str)
        self.assertIsInstance(
            HealthKit.HKWorkoutSortIdentifierTotalSwimmingStrokeCount, str
        )
        self.assertIsInstance(HealthKit.HKWorkoutSortIdentifierTotalFlightsClimbed, str)
