import CalendarStore
import objc
from PyObjCTools.TestSupport import TestCase


class TestCalendarStore(TestCase):
    def testClasses(self):
        self.assertHasAttr(CalendarStore, "CalAlarm")
        self.assertIsInstance(CalendarStore.CalAlarm, objc.objc_class)
        self.assertHasAttr(CalendarStore, "CalNthWeekDay")
        self.assertIsInstance(CalendarStore.CalNthWeekDay, objc.objc_class)
