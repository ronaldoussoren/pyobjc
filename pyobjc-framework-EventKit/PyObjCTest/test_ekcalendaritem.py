import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2**32:
    import EventKit

    class TestEKCalendarItem (TestCase):
        @min_os_level('10.8')
        def testBasic(self):
            self.assertTrue(hasattr(EventKit, "EKCalendarItem"))

        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertResultIsBOOL(EventKit.EKCalendarItem.hasAlarms)
            self.assertResultIsBOOL(EventKit.EKCalendarItem.hasAttendees)
            self.assertResultIsBOOL(EventKit.EKCalendarItem.hasNotes)
            self.assertResultIsBOOL(EventKit.EKCalendarItem.hasRecurrenceRules)


if __name__ == '__main__':
    main()
