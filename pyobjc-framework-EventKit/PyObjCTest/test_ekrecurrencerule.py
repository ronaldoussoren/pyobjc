from PyObjCTools.TestSupport import TestCase
import EventKit


class TestEKRecurrenceRule(TestCase):
    def test_enums(self):
        self.assertIsEnumType(EventKit.EKRecurrenceFrequency)
        self.assertEqual(EventKit.EKRecurrenceFrequencyDaily, 0)
        self.assertEqual(EventKit.EKRecurrenceFrequencyWeekly, 1)
        self.assertEqual(EventKit.EKRecurrenceFrequencyMonthly, 2)
        self.assertEqual(EventKit.EKRecurrenceFrequencyYearly, 3)

        self.assertIsEnumType(EventKit.EKWeekday)
        self.assertEqual(EventKit.EKWeekdaySunday, 1)
        self.assertEqual(EventKit.EKWeekdayMonday, 2)
        self.assertEqual(EventKit.EKWeekdayTuesday, 3)
        self.assertEqual(EventKit.EKWeekdayWednesday, 4)
        self.assertEqual(EventKit.EKWeekdayThursday, 5)
        self.assertEqual(EventKit.EKWeekdayFriday, 6)
        self.assertEqual(EventKit.EKWeekdaySaturday, 7)
        self.assertEqual(EventKit.EKSunday, EventKit.EKWeekdaySunday)
        self.assertEqual(EventKit.EKMonday, EventKit.EKWeekdayMonday)
        self.assertEqual(EventKit.EKTuesday, EventKit.EKWeekdayTuesday)
        self.assertEqual(EventKit.EKWednesday, EventKit.EKWeekdayWednesday)
        self.assertEqual(EventKit.EKThursday, EventKit.EKWeekdayThursday)
        self.assertEqual(EventKit.EKFriday, EventKit.EKWeekdayFriday)
        self.assertEqual(EventKit.EKSaturday, EventKit.EKWeekdaySaturday)
