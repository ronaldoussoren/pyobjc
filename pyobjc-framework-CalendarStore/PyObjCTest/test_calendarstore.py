'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import CalendarStore
from PyObjCTools.TestSupport import *

class TestCalendarStore (TestCase):
    def testClasses(self):
        self.assert_( hasattr(CalendarStore, 'CalAlarm') )
        self.assert_( isinstance(CalendarStore.CalAlarm, objc.objc_class) )
        self.assert_( hasattr(CalendarStore, 'CalNthWeekDay') )
        self.assert_( isinstance(CalendarStore.CalNthWeekDay, objc.objc_class) )

if __name__ == "__main__":
    main()

