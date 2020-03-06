import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalRecurrenceRule(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CalendarStore.CalRecurrenceEnd.usesEndDate)

    def testConstants(self):
        self.assertEqual(CalendarStore.CalRecurrenceDaily, 0)
        self.assertEqual(CalendarStore.CalRecurrenceWeekly, 1)
        self.assertEqual(CalendarStore.CalRecurrenceMonthly, 2)
        self.assertEqual(CalendarStore.CalRecurrenceYearly, 3)

        self.assertIsInstance(CalendarStore.CalDefaultRecurrenceInterval, int)
