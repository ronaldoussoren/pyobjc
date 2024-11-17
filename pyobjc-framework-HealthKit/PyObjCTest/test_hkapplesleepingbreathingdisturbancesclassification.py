from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKAppleSleepingBreathingDisturbancesClassification(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            HealthKit.HKAppleSleepingBreathingDisturbancesClassification
        )
        self.assertEqual(
            HealthKit.HKAppleSleepingBreathingDisturbancesClassificationNotElevated, 0
        )
        self.assertEqual(
            HealthKit.HKAppleSleepingBreathingDisturbancesClassificationElevated, 1
        )

    @min_os_level("15.0")
    def test_functions15_0(self):
        HealthKit.HKAppleSleepingBreathingDisturbancesMinimumQuantityForClassification
        HealthKit.HKAppleSleepingBreathingDisturbancesClassificationForQuantity
