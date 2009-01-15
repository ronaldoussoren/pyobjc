
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalRecurrenceRule (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(CalRecurrenceEnd.usesEndDate)

    def testConstants(self):
        self.failUnlessEqual(CalRecurrenceDaily, 0)
        self.failUnlessEqual(CalRecurrenceWeekly, 1)
        self.failUnlessEqual(CalRecurrenceMonthly, 2)
        self.failUnlessEqual(CalRecurrenceYearly, 3)

        self.failUnlessIsInstance(CalDefaultRecurrenceInterval, (int, long))

if __name__ == "__main__":
    main()
