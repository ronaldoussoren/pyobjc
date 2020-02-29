from CalendarStore import *
from PyObjCTools.TestSupport import *


class TestCalCalendarItem(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CalCalendarItem.hasAlarm)


if __name__ == "__main__":
    main()
