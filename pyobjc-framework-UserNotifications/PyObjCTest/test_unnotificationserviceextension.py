import sys


if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import TestCase
    import UserNotifications

    class TestUNNotificationServiceExtension(TestCase):
        def test_methods(self):
            self.assertArgIsBlock(
                UserNotifications.UNNotificationServiceExtension.didReceiveNotificationRequest_withContentHandler_,  # noqa: B950
                1,
                b"v@",
            )
