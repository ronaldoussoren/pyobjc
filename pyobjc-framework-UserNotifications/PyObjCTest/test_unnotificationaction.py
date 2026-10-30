from PyObjCTools.TestSupport import TestCase
import UserNotifications


class TestUNNotificationAction(TestCase):
    def test_enums(self):
        self.assertIsEnumType(UserNotifications.UNNotificationActionOptions)
        self.assertEqual(UserNotifications.UNNotificationActionOptionNone, 0)
        self.assertEqual(
            UserNotifications.UNNotificationActionOptionAuthenticationRequired, 1 << 0
        )
        self.assertEqual(
            UserNotifications.UNNotificationActionOptionDestructive, 1 << 1
        )
        self.assertEqual(UserNotifications.UNNotificationActionOptionForeground, 1 << 2)
