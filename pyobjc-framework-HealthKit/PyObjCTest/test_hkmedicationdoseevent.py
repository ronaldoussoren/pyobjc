from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKMedicationDoseEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKMedicationDoseEventLogStatus)
        self.assertEqual(HealthKit.HKMedicationDoseEventLogStatusNotInteracted, 1)
        self.assertEqual(HealthKit.HKMedicationDoseEventLogStatusNotificationNotSent, 2)
        self.assertEqual(HealthKit.HKMedicationDoseEventLogStatusSnoozed, 3)
        self.assertEqual(HealthKit.HKMedicationDoseEventLogStatusTaken, 4)
        self.assertEqual(HealthKit.HKMedicationDoseEventLogStatusSkipped, 5)
        self.assertEqual(HealthKit.HKMedicationDoseEventLogStatusNotLogged, 6)

        self.assertIsEnumType(HealthKit.HKMedicationDoseEventScheduleType)
        self.assertEqual(HealthKit.HKMedicationDoseEventScheduleTypeAsNeeded, 1)
        self.assertEqual(HealthKit.HKMedicationDoseEventScheduleTypeSchedule, 2)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(HealthKit.HKPredicateKeyPathStatus, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathLogOrigin, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathScheduledDate, str)
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathMedicationConceptIdentifier, str
        )
