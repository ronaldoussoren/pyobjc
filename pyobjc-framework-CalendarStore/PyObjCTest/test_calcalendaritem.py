import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalCalendarItem(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CalendarStore.CalCalendarItem.hasAlarm)
