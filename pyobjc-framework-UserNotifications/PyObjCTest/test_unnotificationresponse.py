import sys


if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import TestCase
    import UserNotifications

    class TestUNNotificationResponse(TestCase):
        def test_constants(self):
            self.assertIsInstance(
                UserNotifications.UNNotificationDefaultActionIdentifier, str
            )
            self.assertIsInstance(
                UserNotifications.UNNotificationDismissActionIdentifier, str
            )
