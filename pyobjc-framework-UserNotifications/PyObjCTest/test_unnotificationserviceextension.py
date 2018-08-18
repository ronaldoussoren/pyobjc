from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import UserNotifications

    class TestUNNotificationServiceExtension (TestCase):
        def test_methods(self):
            self.assertArgIsBlock(UserNotifications.UNNotificationServiceExtension.didReceiveNotificationRequest_withContentHandler_, 1, b'v@')

if __name__ == "__main__":
    main()
