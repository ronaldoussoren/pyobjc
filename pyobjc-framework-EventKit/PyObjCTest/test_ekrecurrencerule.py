from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKRecurrenceRule(TestCase):
    @min_os_level("10.8")
    def testBasic(self):
        self.assertTrue(hasattr(EventKit, "EKRecurrenceRule"))

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(EventKit.EKRecurrenceFrequencyDaily, 0)
        self.assertEqual(EventKit.EKRecurrenceFrequencyWeekly, 1)
        self.assertEqual(EventKit.EKRecurrenceFrequencyMonthly, 2)
        self.assertEqual(EventKit.EKRecurrenceFrequencyYearly, 3)

        self.assertEqual(EventKit.EKSunday, 1)
        self.assertEqual(EventKit.EKMonday, 2)
        self.assertEqual(EventKit.EKTuesday, 3)
        self.assertEqual(EventKit.EKWednesday, 4)
        self.assertEqual(EventKit.EKThursday, 5)
        self.assertEqual(EventKit.EKFriday, 6)
        self.assertEqual(EventKit.EKSaturday, 7)
