from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKQuantityAggregationStyle(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKQuantityAggregationStyle)
        self.assertEqual(HealthKit.HKQuantityAggregationStyleCumulative, 1)
        self.assertEqual(HealthKit.HKQuantityAggregationStyleDiscreteArithmetic, 2)
        self.assertEqual(HealthKit.HKQuantityAggregationStyleDiscrete, 3)
        self.assertEqual(
            HealthKit.HKQuantityAggregationStyleDiscreteTemporallyWeighted, 4
        )
        self.assertEqual(
            HealthKit.HKQuantityAggregationStyleDiscreteEquivalentContinuousLevel, 5
        )
