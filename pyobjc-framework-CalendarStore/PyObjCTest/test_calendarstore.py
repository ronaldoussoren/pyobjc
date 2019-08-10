"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
import CalendarStore
from PyObjCTools.TestSupport import *


class TestCalendarStore(TestCase):
    def testClasses(self):
        self.assertHasAttr(CalendarStore, "CalAlarm")
        self.assertIsInstance(CalendarStore.CalAlarm, objc.objc_class)
        self.assertHasAttr(CalendarStore, "CalNthWeekDay")
        self.assertIsInstance(CalendarStore.CalNthWeekDay, objc.objc_class)


if __name__ == "__main__":
    main()
