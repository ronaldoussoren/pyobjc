
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalEvent (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(CalEvent.isAllDay)
        self.failUnlessArgIsBOOL(CalEvent.setIsAllDay_, 0)

        self.failUnlessResultIsBOOL(CalEvent.isDetached)

if __name__ == "__main__":
    main()
