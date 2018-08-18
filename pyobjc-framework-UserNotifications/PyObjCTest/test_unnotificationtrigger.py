from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import UserNotifications

    class TestUNNotificationTrigger (TestCase):
        def test_methods(self):
            self.assertResultIsBOOL(UserNotifications.UNNotificationTrigger.repeats)
            self.assertArgIsBOOL(UserNotifications.UNTimeIntervalNotificationTrigger.triggerWithTimeInterval_repeats_, 1)
            self.assertArgIsBOOL(UserNotifications.UNCalendarNotificationTrigger.triggerWithDateMatchingComponents_repeats_, 1)
            self.assertArgIsBOOL(UserNotifications.UNLocationNotificationTrigger.triggerWithRegion_repeats_, 1)

if __name__ == "__main__":
    main()
