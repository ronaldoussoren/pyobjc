
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalCalendarItem (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CalCalendarItem.hasAlarm)

if __name__ == "__main__":
    main()
