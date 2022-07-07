from PyObjCTools.TestSupport import TestCase, min_os_level
import UserNotifications
import objc


class TestUNUserNotificationCenterHelper(UserNotifications.NSObject):
    def userNotificationCenter_willPresentNotification_withCompletionHandler_(
        self, a, b, c
    ):
        pass

    def userNotificationCenter_didReceiveNotificationResponse_withCompletionHandler_(
        self, a, b, c
    ):
        pass

    def userNotificationCenter_openSettingsForNotification_(self, a, b):
        pass


class TestUNUserNotificationCenter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(UserNotifications.UNAuthorizationOptions)
        self.assertIsEnumType(UserNotifications.UNNotificationPresentationOptions)

    def test_constants(self):
        self.assertEqual(UserNotifications.UNAuthorizationOptionBadge, 1 << 0)
        self.assertEqual(UserNotifications.UNAuthorizationOptionSound, 1 << 1)
        self.assertEqual(UserNotifications.UNAuthorizationOptionAlert, 1 << 2)
        self.assertEqual(UserNotifications.UNAuthorizationOptionCarPlay, 1 << 3)
        self.assertEqual(UserNotifications.UNAuthorizationOptionCriticalAlert, 1 << 4)
        self.assertEqual(
            UserNotifications.UNAuthorizationOptionProvidesAppNotificationSettings,
            1 << 5,
        )
        self.assertEqual(UserNotifications.UNAuthorizationOptionProvisional, 1 << 6)
        self.assertEqual(UserNotifications.UNAuthorizationOptionNone, 0)

        self.assertEqual(
            UserNotifications.UNNotificationPresentationOptionBadge, 1 << 0
        )
        self.assertEqual(
            UserNotifications.UNNotificationPresentationOptionSound, 1 << 1
        )
        self.assertEqual(
            UserNotifications.UNNotificationPresentationOptionAlert, 1 << 2
        )
        self.assertEqual(UserNotifications.UNNotificationPresentationOptionList, 1 << 3)
        self.assertEqual(
            UserNotifications.UNNotificationPresentationOptionBanner, 1 << 4
        )
        self.assertEqual(UserNotifications.UNNotificationPresentationOptionNone, 0)

    def test_methods(self):
        self.assertResultIsBOOL(
            UserNotifications.UNUserNotificationCenter.supportsContentExtensions
        )
        self.assertArgIsBlock(
            UserNotifications.UNUserNotificationCenter.requestAuthorizationWithOptions_completionHandler_,  # noqa: B950
            1,
            b"vZ@",
        )
        self.assertArgIsBlock(
            UserNotifications.UNUserNotificationCenter.getNotificationCategoriesWithCompletionHandler_,  # noqa: B950
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            UserNotifications.UNUserNotificationCenter.getNotificationSettingsWithCompletionHandler_,  # noqa: B950
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            UserNotifications.UNUserNotificationCenter.addNotificationRequest_withCompletionHandler_,  # noqa: B950
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            UserNotifications.UNUserNotificationCenter.getPendingNotificationRequestsWithCompletionHandler_,  # noqa: B950
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            UserNotifications.UNUserNotificationCenter.getDeliveredNotificationsWithCompletionHandler_,  # noqa: B950
            0,
            b"v@",
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            UserNotifications.UNUserNotificationCenter.setBadgeCount_withCompletionHandler_,
            1,
            b"v@",
        )

    def test_protocols(self):
        self.assertProtocolExists("UNUserNotificationCenterDelegate")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestUNUserNotificationCenterHelper.userNotificationCenter_willPresentNotification_withCompletionHandler_,  # noqa: B950
            2,
            b"v" + objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            TestUNUserNotificationCenterHelper.userNotificationCenter_didReceiveNotificationResponse_withCompletionHandler_,  # noqa: B950
            2,
            b"v",
        )
