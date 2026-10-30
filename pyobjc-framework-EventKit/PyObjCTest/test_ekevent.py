from PyObjCTools.TestSupport import TestCase
import EventKit


class TestEKEvent(TestCase):
    def test_enums(self):
        self.assertIsEnumType(EventKit.EKEventAvailability)
        self.assertEqual(EventKit.EKEventAvailabilityNotSupported, -1)
        self.assertEqual(EventKit.EKEventAvailabilityBusy, 0)
        self.assertEqual(EventKit.EKEventAvailabilityFree, 1)
        self.assertEqual(EventKit.EKEventAvailabilityTentative, 2)
        self.assertEqual(EventKit.EKEventAvailabilityUnavailable, 3)

        self.assertIsEnumType(EventKit.EKEventStatus)
        self.assertEqual(EventKit.EKEventStatusNone, 0)
        self.assertEqual(EventKit.EKEventStatusConfirmed, 1)
        self.assertEqual(EventKit.EKEventStatusTentative, 2)
        self.assertEqual(EventKit.EKEventStatusCanceled, 3)

    def test_methods(self):
        self.assertResultIsBOOL(EventKit.EKEvent.isAllDay)
        self.assertResultIsBOOL(EventKit.EKEvent.isDetached)
        self.assertResultIsBOOL(EventKit.EKEvent.refresh)
