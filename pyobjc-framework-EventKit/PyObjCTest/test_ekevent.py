from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKEvent(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(EventKit.EKEventAvailability)
        self.assertIsEnumType(EventKit.EKEventStatus)

    @min_os_level("10.8")
    def testBasic(self):
        self.assertTrue(hasattr(EventKit, "EKEvent"))

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(EventKit.EKEvent.isAllDay)
        self.assertResultIsBOOL(EventKit.EKEvent.isDetached)
        self.assertResultIsBOOL(EventKit.EKEvent.refresh)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(EventKit.EKEventAvailabilityNotSupported, -1)
        self.assertEqual(EventKit.EKEventAvailabilityBusy, 0)
        self.assertEqual(EventKit.EKEventAvailabilityFree, 1)
        self.assertEqual(EventKit.EKEventAvailabilityTentative, 2)
        self.assertEqual(EventKit.EKEventAvailabilityUnavailable, 3)

        self.assertEqual(EventKit.EKEventStatusNone, 0)
        self.assertEqual(EventKit.EKEventStatusConfirmed, 1)
        self.assertEqual(EventKit.EKEventStatusTentative, 2)
        self.assertEqual(EventKit.EKEventStatusCanceled, 3)
