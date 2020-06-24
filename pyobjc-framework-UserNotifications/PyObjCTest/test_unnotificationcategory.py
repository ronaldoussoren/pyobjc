from PyObjCTools.TestSupport import TestCase
import UserNotifications


class TestUNNotificationCategory(TestCase):
    def test_constants(self):
        self.assertEqual(
            UserNotifications.UNNotificationCategoryOptionCustomDismissAction, 1 << 0
        )
        self.assertEqual(
            UserNotifications.UNNotificationCategoryOptionAllowInCarPlay, 1 << 1
        )
        self.assertEqual(
            UserNotifications.UNNotificationCategoryOptionHiddenPreviewsShowTitle,
            1 << 2,
        )
        self.assertEqual(
            UserNotifications.UNNotificationCategoryOptionHiddenPreviewsShowSubtitle,
            1 << 3,
        )
        self.assertEqual(UserNotifications.UNNotificationCategoryOptionNone, 0)
