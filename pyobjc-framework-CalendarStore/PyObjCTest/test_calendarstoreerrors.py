
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalendarStoreErrors (TestCase):
    def testConstants(self):
        self.failUnlessEqual(CalCalendarNotEditableError, 1025)
        self.failUnlessEqual(CalDateInvalidError, 1026)
        self.failUnlessEqual(CalCalendarNotInRepository, 1027)
        self.failUnlessEqual(CalCalendarTitleNotUniqueError, 1028)

if __name__ == "__main__":
    main()
