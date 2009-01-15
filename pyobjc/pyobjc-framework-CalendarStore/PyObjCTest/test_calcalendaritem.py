
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalCalendarItem (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(CalCalendarItem.hasAlarm)

if __name__ == "__main__":
    main()
