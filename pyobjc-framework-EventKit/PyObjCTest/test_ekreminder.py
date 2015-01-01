import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2**32:
    import EventKit

    class TestEKReminder (TestCase):
        @min_os_level('10.8')
        def testBasic(self):
            self.assertTrue(hasattr(EventKit, "EKReminder"))

        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertResultIsBOOL(EventKit.EKReminder.isCompleted)
            self.assertArgIsBOOL(EventKit.EKReminder.setCompleted_, 0)

        def testConstants(self):
            self.assertEqual(EventKit.EKReminderPriorityNone, 0)
            self.assertEqual(EventKit.EKReminderPriorityHigh, 1)
            self.assertEqual(EventKit.EKReminderPriorityMedium, 5)
            self.assertEqual(EventKit.EKReminderPriorityLow, 9)

if __name__ == '__main__':
    main()
