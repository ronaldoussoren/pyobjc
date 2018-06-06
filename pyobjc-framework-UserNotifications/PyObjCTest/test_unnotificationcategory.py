from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import UserNotifications

    class TestUNNotificationCategory (TestCase):
        def test_constants(self):
            self.assertEqual(UserNotifications.UNNotificationCategoryOptionCustomDismissAction, 1 << 0)
            self.assertEqual(UserNotifications.UNNotificationCategoryOptionAllowInCarPlay, 1 << 1)
            self.assertEqual(UserNotifications.UNNotificationCategoryOptionHiddenPreviewsShowTitle, 1 << 2)
            self.assertEqual(UserNotifications.UNNotificationCategoryOptionHiddenPreviewsShowSubtitle, 1 << 3)
            self.assertEqual(UserNotifications.UNNotificationCategoryOptionNone, 0)

if __name__ == "__main__":
    main()
