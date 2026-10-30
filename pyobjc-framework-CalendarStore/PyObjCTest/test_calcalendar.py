import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalCalendar(TestCase):
    def test_constants(self):
        self.assertIsInstance(CalendarStore.CalCalendarTypeBirthday, str)
        self.assertIsInstance(CalendarStore.CalCalendarTypeCalDAV, str)
        self.assertIsInstance(CalendarStore.CalCalendarTypeLocal, str)
        self.assertIsInstance(CalendarStore.CalCalendarTypeSubscription, str)
        self.assertIsInstance(CalendarStore.CalCalendarTypeIMAP, str)

        self.assertIsInstance(CalendarStore.CalCalendarTypeExchange, str)

    def test_methods(self):
        self.assertResultIsBOOL(CalendarStore.CalCalendar.isEditable)
