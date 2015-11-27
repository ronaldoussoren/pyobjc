
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalRecurrenceRule (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CalRecurrenceEnd.usesEndDate)

    def testConstants(self):
        self.assertEqual(CalRecurrenceDaily, 0)
        self.assertEqual(CalRecurrenceWeekly, 1)
        self.assertEqual(CalRecurrenceMonthly, 2)
        self.assertEqual(CalRecurrenceYearly, 3)

        self.assertIsInstance(CalDefaultRecurrenceInterval, (int, long))

if __name__ == "__main__":
    main()
