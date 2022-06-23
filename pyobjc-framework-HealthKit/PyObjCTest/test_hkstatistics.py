from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKStatistics(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKStatisticsOptions)
        self.assertEqual(HealthKit.HKStatisticsOptionNone, 0)
        self.assertEqual(HealthKit.HKStatisticsOptionSeparateBySource, 1 << 0)
        self.assertEqual(HealthKit.HKStatisticsOptionDiscreteAverage, 1 << 1)
        self.assertEqual(HealthKit.HKStatisticsOptionDiscreteMin, 1 << 2)
        self.assertEqual(HealthKit.HKStatisticsOptionDiscreteMax, 1 << 3)
        self.assertEqual(HealthKit.HKStatisticsOptionCumulativeSum, 1 << 4)
        self.assertEqual(HealthKit.HKStatisticsOptionMostRecent, 1 << 5)
        self.assertEqual(
            HealthKit.HKStatisticsOptionDiscreteMostRecent,
            HealthKit.HKStatisticsOptionMostRecent,
        )
        self.assertEqual(HealthKit.HKStatisticsOptionDuration, 1 << 6)
