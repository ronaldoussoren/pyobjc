from PyObjCTools.TestSupport import TestCase
import UserNotifications


class TestUNNotificationServiceExtension(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            UserNotifications.UNNotificationServiceExtension.didReceiveNotificationRequest_withContentHandler_,  # noqa: B950
            1,
            b"v@",
        )
