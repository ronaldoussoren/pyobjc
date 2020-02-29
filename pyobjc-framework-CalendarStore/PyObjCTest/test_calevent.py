from CalendarStore import *
from PyObjCTools.TestSupport import *


class TestCalEvent(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CalEvent.isAllDay)
        self.assertArgIsBOOL(CalEvent.setIsAllDay_, 0)

        self.assertResultIsBOOL(CalEvent.isDetached)


if __name__ == "__main__":
    main()
