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
