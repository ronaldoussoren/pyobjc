
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalCalendar (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(CalCalendarTypeBirthday, unicode)
        self.failUnlessIsInstance(CalCalendarTypeCalDAV, unicode)
        self.failUnlessIsInstance(CalCalendarTypeLocal, unicode)
        self.failUnlessIsInstance(CalCalendarTypeSubscription, unicode)
        self.failUnlessIsInstance(CalCalendarTypeIMAP, unicode)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(CalCalendarTypeExchange, unicode)



if __name__ == "__main__":
    main()
