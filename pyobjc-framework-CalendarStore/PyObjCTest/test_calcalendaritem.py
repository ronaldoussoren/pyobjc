import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalCalendarItem(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CalendarStore.CalCalendarItem.hasAlarm)
