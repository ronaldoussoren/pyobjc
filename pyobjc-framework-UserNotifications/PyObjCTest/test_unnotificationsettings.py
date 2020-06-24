from PyObjCTools.TestSupport import TestCase
import UserNotifications


class TestUNNotificationSettings(TestCase):
    def test_constants(self):
        self.assertEqual(UserNotifications.UNAuthorizationStatusNotDetermined, 0)
        self.assertEqual(UserNotifications.UNAuthorizationStatusDenied, 1)
        self.assertEqual(UserNotifications.UNAuthorizationStatusAuthorized, 2)
        self.assertEqual(UserNotifications.UNAuthorizationStatusProvisional, 3)

        self.assertEqual(UserNotifications.UNShowPreviewsSettingAlways, 0)
        self.assertEqual(UserNotifications.UNShowPreviewsSettingWhenAuthenticated, 1)
        self.assertEqual(UserNotifications.UNShowPreviewsSettingNever, 2)

        self.assertEqual(UserNotifications.UNNotificationSettingNotSupported, 0)
        self.assertEqual(UserNotifications.UNNotificationSettingDisabled, 1)
        self.assertEqual(UserNotifications.UNNotificationSettingEnabled, 2)

        self.assertEqual(UserNotifications.UNAlertStyleNone, 0)
        self.assertEqual(UserNotifications.UNAlertStyleBanner, 1)
        self.assertEqual(UserNotifications.UNAlertStyleAlert, 2)

    def test_methods(self):
        self.assertResultIsBOOL(
            UserNotifications.UNNotificationSettings.providesAppNotificationSettings
        )
