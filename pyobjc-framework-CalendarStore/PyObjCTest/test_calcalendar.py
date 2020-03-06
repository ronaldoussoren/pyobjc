import CalendarStore
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCalCalendar(TestCase):
    def testConstants(self):
        self.assertIsInstance(CalendarStore.CalCalendarTypeBirthday, str)
        self.assertIsInstance(CalendarStore.CalCalendarTypeCalDAV, str)
        self.assertIsInstance(CalendarStore.CalCalendarTypeLocal, str)
        self.assertIsInstance(CalendarStore.CalCalendarTypeSubscription, str)
        self.assertIsInstance(CalendarStore.CalCalendarTypeIMAP, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(CalendarStore.CalCalendarTypeExchange, str)

    def testMethods(self):
        self.assertResultIsBOOL(CalendarStore.CalCalendar.isEditable)
