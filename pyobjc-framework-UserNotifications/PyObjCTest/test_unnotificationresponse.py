from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import UserNotifications

    class TestUNNotificationResponse (TestCase):
        def test_constants(self):
            self.assertIsInstance(UserNotifications.UNNotificationDefaultActionIdentifier, unicode)
            self.assertIsInstance(UserNotifications.UNNotificationDismissActionIdentifier, unicode)

if __name__ == "__main__":
    main()
