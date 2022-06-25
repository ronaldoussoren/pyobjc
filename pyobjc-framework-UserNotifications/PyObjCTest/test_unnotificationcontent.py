from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level
import UserNotifications


class TestUNNotificationContent(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(UserNotifications.UNNotificationInterruptionLevel)

    def test_constants(self):
        self.assertEqual(UserNotifications.UNNotificationInterruptionLevelPassive, 0)
        self.assertEqual(UserNotifications.UNNotificationInterruptionLevelActive, 1)
        self.assertEqual(
            UserNotifications.UNNotificationInterruptionLevelTimeSensitive, 2
        )
        self.assertEqual(UserNotifications.UNNotificationInterruptionLevelCritical, 3)

    @min_sdk_level("12.0")
    def test_protocols12_0(self):
        self.assertProtocolExists("UNNotificationContentProviding")

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsOut(
            UserNotifications.UNNotificationContent.contentByUpdatingWithProvider_error_,
            1,
        )
