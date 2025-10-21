from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKQuery(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKQueryOptions)
        self.assertEqual(HealthKit.HKQueryOptionNone, 0)
        self.assertEqual(HealthKit.HKQueryOptionStrictStartDate, 1 << 0)
        self.assertEqual(HealthKit.HKQueryOptionStrictEndDate, 1 << 1)

    @min_os_level("26.0")
    def test_methods(self):
        self.assertArgIsBOOL(
            HealthKit.HKQuery.predicateForUserAnnotatedMedicationsWithIsArchived_, 0
        )
        self.assertArgIsBOOL(
            HealthKit.HKQuery.predicateForUserAnnotatedMedicationsWithHasSchedule_, 0
        )
