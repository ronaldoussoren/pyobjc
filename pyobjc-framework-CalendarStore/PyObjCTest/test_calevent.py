import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalEvent(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CalendarStore.CalEvent.isAllDay)
        self.assertArgIsBOOL(CalendarStore.CalEvent.setIsAllDay_, 0)

        self.assertResultIsBOOL(CalendarStore.CalEvent.isDetached)
