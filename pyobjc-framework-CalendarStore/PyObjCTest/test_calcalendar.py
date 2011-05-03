
from PyObjCTools.TestSupport import *
from CalendarStore import *

class TestCalCalendar (TestCase):
    def testConstants(self):
        self.assertIsInstance(CalCalendarTypeBirthday, unicode)
        self.assertIsInstance(CalCalendarTypeCalDAV, unicode)
        self.assertIsInstance(CalCalendarTypeLocal, unicode)
        self.assertIsInstance(CalCalendarTypeSubscription, unicode)
        self.assertIsInstance(CalCalendarTypeIMAP, unicode)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(CalCalendarTypeExchange, unicode)



if __name__ == "__main__":
    main()
