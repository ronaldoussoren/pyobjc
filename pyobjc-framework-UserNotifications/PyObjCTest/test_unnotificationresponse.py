from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import UserNotifications

    class TestUNNotificationResponse (TestCase):
        def test_constants(self):
            self.assertEqual(UserNotifications.UNNotificationDefaultActionIdentifier, unicode)
            self.assertEqual(UserNotifications.UNNotificationDismissActionIdentifier, unicode)

if __name__ == "__main__":
    main()
