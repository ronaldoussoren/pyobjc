from PyObjCTools.TestSupport import TestCase
import UserNotifications


class TestUNNotificationAttachment(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            UserNotifications.UNNotificationAttachmentOptionsTypeHintKey, str
        )
        self.assertIsInstance(
            UserNotifications.UNNotificationAttachmentOptionsThumbnailHiddenKey, str
        )
        self.assertIsInstance(
            UserNotifications.UNNotificationAttachmentOptionsThumbnailClippingRectKey,
            str,
        )
        self.assertIsInstance(
            UserNotifications.UNNotificationAttachmentOptionsThumbnailTimeKey, str
        )

    def test_methods(self):
        self.assertArgIsOut(
            UserNotifications.UNNotificationAttachment.attachmentWithIdentifier_URL_options_error_,  # noqa: B950
            3,
        )
