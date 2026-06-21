from PyObjCTools.TestSupport import TestCase, min_os_level
import EventKit


class TestEKReminder(TestCase):
    @min_os_level("10.8")
    def testBasic(self):
        self.assertTrue(hasattr(EventKit, "EKReminder"))

    @min_os_level("10.8")
    def test_methods10_8(self):
        self.assertResultIsBOOL(EventKit.EKReminder.isCompleted)
        self.assertArgIsBOOL(EventKit.EKReminder.setCompleted_, 0)

    def test_constants(self):
        self.assertEqual(EventKit.EKReminderPriorityNone, 0)
        self.assertEqual(EventKit.EKReminderPriorityHigh, 1)
        self.assertEqual(EventKit.EKReminderPriorityMedium, 5)
        self.assertEqual(EventKit.EKReminderPriorityLow, 9)
