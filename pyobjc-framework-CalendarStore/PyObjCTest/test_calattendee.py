import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalAttendee(TestCase):
    def test_constants(self):
        self.assertIsInstance(CalendarStore.CalAttendeeStatusNeedsAction, str)
        self.assertIsInstance(CalendarStore.CalAttendeeStatusAccepted, str)
        self.assertIsInstance(CalendarStore.CalAttendeeStatusDeclined, str)
        self.assertIsInstance(CalendarStore.CalAttendeeStatusTentative, str)
