from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import UserNotifications

    class TestUNError (TestCase):
        def test_constants(self):
            self.assertEqual(UserNotifications.UNErrorCodeNotificationsNotAllowed, 1)
            self.assertEqual(UserNotifications.UNErrorCodeAttachmentInvalidURL, 100)
            self.assertEqual(UserNotifications.UNErrorCodeAttachmentUnrecognizedType, 101)
            self.assertEqual(UserNotifications.UNErrorCodeAttachmentInvalidFileSize, 102)
            self.assertEqual(UserNotifications.UNErrorCodeAttachmentNotInDataStore, 103)
            self.assertEqual(UserNotifications.UNErrorCodeAttachmentMoveIntoDataStoreFailed, 104)
            self.assertEqual(UserNotifications.UNErrorCodeAttachmentCorrupt, 105)
            self.assertEqual(UserNotifications.UNErrorCodeNotificationInvalidNoDate, 1400)
            self.assertEqual(UserNotifications.UNErrorCodeNotificationInvalidNoContent, 1401)

if __name__ == "__main__":
    main()
