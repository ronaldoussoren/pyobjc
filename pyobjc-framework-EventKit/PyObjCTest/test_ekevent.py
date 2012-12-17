import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2**32:
    import EventKit

    class TestEKEvent (TestCase):
        @min_os_level('10.8')
        def testBasic(self):
            self.assertTrue(hasattr(EventKit, "EKEvent"))

        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertResultIsBOOL(EventKit.EKEvent.isAllDay)
            self.assertResultIsBOOL(EventKit.EKEvent.isDetached)
            self.assertResultIsBOOL(EventKit.EKEvent.refresh)

        @min_os_level('10.8')
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

if __name__ == '__main__':
    main()
