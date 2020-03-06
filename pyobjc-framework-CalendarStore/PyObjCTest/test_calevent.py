import CalendarStore
from PyObjCTools.TestSupport import TestCase


class TestCalEvent(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(CalendarStore.CalEvent.isAllDay)
        self.assertArgIsBOOL(CalendarStore.CalEvent.setIsAllDay_, 0)

        self.assertResultIsBOOL(CalendarStore.CalEvent.isDetached)
