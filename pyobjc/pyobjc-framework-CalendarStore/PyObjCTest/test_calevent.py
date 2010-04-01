
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalEvent (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CalEvent.isAllDay)
        self.assertArgIsBOOL(CalEvent.setIsAllDay_, 0)

        self.assertResultIsBOOL(CalEvent.isDetached)

if __name__ == "__main__":
    main()
