from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKQuery(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKQueryOptions)
        self.assertEqual(HealthKit.HKQueryOptionNone, 0)
        self.assertEqual(HealthKit.HKQueryOptionStrictStartDate, 1 << 0)
        self.assertEqual(HealthKit.HKQueryOptionStrictEndDate, 1 << 1)
