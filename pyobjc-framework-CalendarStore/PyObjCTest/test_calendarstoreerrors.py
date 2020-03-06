import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalendarStoreErrors(TestCase):
    def testConstants(self):
        self.assertEqual(CalendarStore.CalCalendarNotEditableError, 1025)
        self.assertEqual(CalendarStore.CalDateInvalidError, 1026)
        self.assertEqual(CalendarStore.CalCalendarNotInRepository, 1027)
        self.assertEqual(CalendarStore.CalCalendarTitleNotUniqueError, 1028)
