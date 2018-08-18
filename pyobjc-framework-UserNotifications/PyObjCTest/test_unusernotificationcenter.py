from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import UserNotifications

    class TestUNUserNotificationCenterHelper (UserNotifications.NSObject):
        def userNotificationCenter_willPresentNotification_withCompletionHandler_(self, a, b, c): pass
        def userNotificationCenter_didReceiveNotificationResponse_withCompletionHandler_(self, a, b, c): pass
        def userNotificationCenter_openSettingsForNotification_(self, a, b): pass

    class TestUNUserNotificationCenter (TestCase):
        def test_constants(self):
            self.assertEqual(UserNotifications.UNAuthorizationOptionBadge, 1 << 0)
            self.assertEqual(UserNotifications.UNAuthorizationOptionSound, 1 << 1)
            self.assertEqual(UserNotifications.UNAuthorizationOptionAlert, 1 << 2)
            self.assertEqual(UserNotifications.UNAuthorizationOptionCarPlay, 1 << 3)
            self.assertEqual(UserNotifications.UNAuthorizationOptionCriticalAlert, 1 << 4)
            self.assertEqual(UserNotifications.UNAuthorizationOptionProvidesAppNotificationSettings, 1 << 5)
            self.assertEqual(UserNotifications.UNAuthorizationOptionProvisional, 1 << 6)
            self.assertEqual(UserNotifications.UNAuthorizationOptionNone, 0)

            self.assertEqual(UserNotifications.UNNotificationPresentationOptionBadge, 1 << 0)
            self.assertEqual(UserNotifications.UNNotificationPresentationOptionSound, 1 << 1)
            self.assertEqual(UserNotifications.UNNotificationPresentationOptionAlert, 1 << 2)
            self.assertEqual(UserNotifications.UNNotificationPresentationOptionNone, 0)

        def test_methods(self):
            self.assertResultIsBOOL(UserNotifications.UNUserNotificationCenter.supportsContentExtensions)
            self.assertArgIsBlock(UserNotifications.UNUserNotificationCenter.requestAuthorizationWithOptions_completionHandler_, 1, b'vZ@')
            self.assertArgIsBlock(UserNotifications.UNUserNotificationCenter.getNotificationCategoriesWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(UserNotifications.UNUserNotificationCenter.getNotificationSettingsWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(UserNotifications.UNUserNotificationCenter.addNotificationRequest_withCompletionHandler_, 1, b'v@')
            self.assertArgIsBlock(UserNotifications.UNUserNotificationCenter.getPendingNotificationRequestsWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(UserNotifications.UNUserNotificationCenter.getDeliveredNotificationsWithCompletionHandler_, 0, b'v@')

            self.assertArgIsBlock(TestUNUserNotificationCenterHelper.userNotificationCenter_willPresentNotification_withCompletionHandler_, 2, b'v' + objc._C_NSUInteger)
            self.assertArgIsBlock(TestUNUserNotificationCenterHelper.userNotificationCenter_didReceiveNotificationResponse_withCompletionHandler_, 2, b'v')

        def test_protocols(self):
            objc.protocolNamed('UNUserNotificationCenterDelegate')

if __name__ == "__main__":
    main()
