from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKQuantityAggregationStyle(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKQuantityAggregationStyle)
        self.assertEqual(HealthKit.HKQuantityAggregationStyleCumulative, 0)
        self.assertEqual(HealthKit.HKQuantityAggregationStyleDiscreteArithmetic, 1)
        self.assertEqual(
            HealthKit.HKQuantityAggregationStyleDiscrete,
            HealthKit.HKQuantityAggregationStyleDiscreteArithmetic,
        )
        self.assertEqual(
            HealthKit.HKQuantityAggregationStyleDiscreteTemporallyWeighted, 2
        )
        self.assertEqual(
            HealthKit.HKQuantityAggregationStyleDiscreteEquivalentContinuousLevel, 3
        )
