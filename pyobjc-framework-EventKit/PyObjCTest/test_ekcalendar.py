from PyObjCTools.TestSupport import TestCase, min_os_level

import EventKit


class TestEKCalendar(TestCase):
    @min_os_level("10.8")
    def test_basic(self):
        self.assertTrue(hasattr(EventKit, "EKCalendar"))

    @min_os_level("10.8")
    def test_methods10_8(self):
        self.assertResultIsBOOL(EventKit.EKCalendar.allowsContentModifications)
        self.assertResultIsBOOL(EventKit.EKCalendar.isImmutable)
        self.assertResultIsBOOL(EventKit.EKCalendar.isSubscribed)

    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertEqual(EventKit.EKCalendarTypeLocal, 0)
        self.assertEqual(EventKit.EKCalendarTypeCalDAV, 1)
        self.assertEqual(EventKit.EKCalendarTypeExchange, 2)
        self.assertEqual(EventKit.EKCalendarTypeSubscription, 3)
        self.assertEqual(EventKit.EKCalendarTypeBirthday, 4)

        self.assertEqual(EventKit.EKCalendarEventAvailabilityNone, 0)
        self.assertEqual(EventKit.EKCalendarEventAvailabilityBusy, 1 << 0)
        self.assertEqual(EventKit.EKCalendarEventAvailabilityFree, 1 << 1)
        self.assertEqual(EventKit.EKCalendarEventAvailabilityTentative, 1 << 2)
        self.assertEqual(EventKit.EKCalendarEventAvailabilityUnavailable, 1 << 3)
