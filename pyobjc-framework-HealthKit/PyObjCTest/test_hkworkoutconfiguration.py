from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKWorkoutConfiguration(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKWorkoutSessionLocationType)
        self.assertEqual(HealthKit.HKWorkoutSessionLocationTypeUnknown, 1)
        self.assertEqual(HealthKit.HKWorkoutSessionLocationTypeIndoor, 2)
        self.assertEqual(HealthKit.HKWorkoutSessionLocationTypeOutdoor, 3)
