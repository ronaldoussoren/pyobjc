import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalAlarm(TestCase):
    def test_constants(self):
        self.assertIsInstance(CalendarStore.CalAlarmActionDisplay, str)
        self.assertIsInstance(CalendarStore.CalAlarmActionEmail, str)
        self.assertIsInstance(CalendarStore.CalAlarmActionProcedure, str)
        self.assertIsInstance(CalendarStore.CalAlarmActionSound, str)
