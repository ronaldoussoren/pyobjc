from PyObjCTools.TestSupport import TestCase
import EventKit


class TestEKReminder(TestCase):
    def test_enums(self):
        self.assertIsEnumType(EventKit.EKReminderPriority)
        self.assertEqual(EventKit.EKReminderPriorityNone, 0)
        self.assertEqual(EventKit.EKReminderPriorityHigh, 1)
        self.assertEqual(EventKit.EKReminderPriorityMedium, 5)
        self.assertEqual(EventKit.EKReminderPriorityLow, 9)

    def test_methods(self):
        self.assertResultIsBOOL(EventKit.EKReminder.isCompleted)
        self.assertArgIsBOOL(EventKit.EKReminder.setCompleted_, 0)
