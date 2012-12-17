import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2**32:
    import EventKit

    class TestEKCalendar (TestCase):
        @min_os_level('10.8')
        def testBasic(self):
            self.assertTrue(hasattr(EventKit, "EKCalendar"))

        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertResultIsBOOL(EventKit.EKCalendar.allowsContentModifications)
            self.assertResultIsBOOL(EventKit.EKCalendar.isImmutable)
            self.assertResultIsBOOL(EventKit.EKCalendar.isSubscribed)

        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertEqual(EventKit.EKCalendarTypeLocal, 0)
            self.assertEqual(EventKit.EKCalendarTypeCalDAV, 1)
            self.assertEqual(EventKit.EKCalendarTypeExchange, 2)
            self.assertEqual(EventKit.EKCalendarTypeSubscription, 3)
            self.assertEqual(EventKit.EKCalendarTypeBirthday, 4)

            self.assertEqual(EventKit.EKCalendarEventAvailabilityNone, 0)
            self.assertEqual(EventKit.EKCalendarEventAvailabilityBusy, 1<<0)
            self.assertEqual(EventKit.EKCalendarEventAvailabilityFree, 1<<1)
            self.assertEqual(EventKit.EKCalendarEventAvailabilityTentative, 1<<2)
            self.assertEqual(EventKit.EKCalendarEventAvailabilityUnavailable, 1<<3)


if __name__ == '__main__':
    main()
