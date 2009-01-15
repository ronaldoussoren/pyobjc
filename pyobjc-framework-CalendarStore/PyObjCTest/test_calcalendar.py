
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalCalendar (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(CalCalendarTypeBirthday, unicode)
        self.failUnlessIsInstance(CalCalendarTypeCalDAV, unicode)
        self.failUnlessIsInstance(CalCalendarTypeLocal, unicode)
        self.failUnlessIsInstance(CalCalendarTypeSubscription, unicode)
        self.failUnlessIsInstance(CalCalendarTypeIMAP, unicode)


if __name__ == "__main__":
    main()
