from PyObjCTools.TestSupport import TestCase
import UserNotifications


class TestUNNotificationTrigger(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(UserNotifications.UNNotificationTrigger.repeats)
        self.assertArgIsBOOL(
            UserNotifications.UNTimeIntervalNotificationTrigger.triggerWithTimeInterval_repeats_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            UserNotifications.UNCalendarNotificationTrigger.triggerWithDateMatchingComponents_repeats_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            UserNotifications.UNLocationNotificationTrigger.triggerWithRegion_repeats_,
            1,
        )
