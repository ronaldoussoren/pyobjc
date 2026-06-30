from PyObjCTools.TestSupport import TestCase
import UserNotifications


class TestUNNotificationSettings(TestCase):
    def test_enums(self):
        self.assertIsEnumType(UserNotifications.UNAlertStyle)
        self.assertEqual(UserNotifications.UNAlertStyleNone, 0)
        self.assertEqual(UserNotifications.UNAlertStyleBanner, 1)
        self.assertEqual(UserNotifications.UNAlertStyleAlert, 2)

        self.assertIsEnumType(UserNotifications.UNAuthorizationStatus)
        self.assertEqual(UserNotifications.UNAuthorizationStatusNotDetermined, 0)
        self.assertEqual(UserNotifications.UNAuthorizationStatusDenied, 1)
        self.assertEqual(UserNotifications.UNAuthorizationStatusAuthorized, 2)
        self.assertEqual(UserNotifications.UNAuthorizationStatusProvisional, 3)

        self.assertIsEnumType(UserNotifications.UNNotificationSetting)
        self.assertEqual(UserNotifications.UNNotificationSettingNotSupported, 0)
        self.assertEqual(UserNotifications.UNNotificationSettingDisabled, 1)
        self.assertEqual(UserNotifications.UNNotificationSettingEnabled, 2)

        self.assertIsEnumType(UserNotifications.UNShowPreviewsSetting)
        self.assertEqual(UserNotifications.UNShowPreviewsSettingAlways, 0)
        self.assertEqual(UserNotifications.UNShowPreviewsSettingWhenAuthenticated, 1)
        self.assertEqual(UserNotifications.UNShowPreviewsSettingNever, 2)

    def test_methods(self):
        self.assertResultIsBOOL(
            UserNotifications.UNNotificationSettings.providesAppNotificationSettings
        )
