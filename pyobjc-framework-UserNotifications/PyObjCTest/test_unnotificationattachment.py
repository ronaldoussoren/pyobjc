from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import UserNotifications

    class TestUNNotificationAttachment (TestCase):
        def test_constants(self):
            self.assertIsInstance(UserNotifications.UNNotificationAttachmentOptionsTypeHintKey, unicode)
            self.assertIsInstance(UserNotifications.UNNotificationAttachmentOptionsThumbnailHiddenKey, unicode)
            self.assertIsInstance(UserNotifications.UNNotificationAttachmentOptionsThumbnailClippingRectKey, unicode)
            self.assertIsInstance(UserNotifications.UNNotificationAttachmentOptionsThumbnailTimeKey, unicode)

        def test_methods(self):
            self.assertArgIsOut(UserNotifications.UNNotificationAttachment.attachmentWithIdentifier_URL_options_error_, 3)

if __name__ == "__main__":
    main()
