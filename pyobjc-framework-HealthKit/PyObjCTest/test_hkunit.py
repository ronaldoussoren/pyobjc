from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKUnit(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKMetricPrefix)

        self.assertEqual(HealthKit.HKMetricPrefixNone, 0)
        self.assertEqual(HealthKit.HKMetricPrefixFemto, 13)
        self.assertEqual(HealthKit.HKMetricPrefixPico, 1)
        self.assertEqual(HealthKit.HKMetricPrefixNano, 2)
        self.assertEqual(HealthKit.HKMetricPrefixMicro, 3)
        self.assertEqual(HealthKit.HKMetricPrefixMilli, 4)
        self.assertEqual(HealthKit.HKMetricPrefixCenti, 5)
        self.assertEqual(HealthKit.HKMetricPrefixDeci, 6)
        self.assertEqual(HealthKit.HKMetricPrefixDeca, 7)
        self.assertEqual(HealthKit.HKMetricPrefixHecto, 8)
        self.assertEqual(HealthKit.HKMetricPrefixKilo, 9)
        self.assertEqual(HealthKit.HKMetricPrefixMega, 10)
        self.assertEqual(HealthKit.HKMetricPrefixGiga, 11)
        self.assertEqual(HealthKit.HKMetricPrefixTera, 12)

        self.assertEqual(HealthKit.HKUnitMolarMassBloodGlucose, 180.15588000005408)
