from PyObjCTools.TestSupport import TestCase

import UserNotificationsUI
import objc


class TestUNNotificationContentExtensionHelper(UserNotificationsUI.NSObject):
    def didReceiveNotificationResponse_completionHandler_(self, a, b):
        pass

    def mediaPlayPauseButtonType(self):
        return 1

    def mediaPlayPauseButtonFrame(self):
        return 1


class TestUNNotificationContentExtension(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(
            UserNotificationsUI.UNNotificationContentExtensionMediaPlayPauseButtonType
        )
        self.assertIsEnumType(
            UserNotificationsUI.UNNotificationContentExtensionResponseOption
        )

    def test_constants(self):
        self.assertEqual(
            UserNotificationsUI.UNNotificationContentExtensionMediaPlayPauseButtonTypeNone,
            0,
        )
        self.assertEqual(
            UserNotificationsUI.UNNotificationContentExtensionMediaPlayPauseButtonTypeDefault,
            1,
        )
        self.assertEqual(
            UserNotificationsUI.UNNotificationContentExtensionMediaPlayPauseButtonTypeOverlay,
            2,
        )

        self.assertEqual(
            UserNotificationsUI.UNNotificationContentExtensionResponseOptionDoNotDismiss,
            0,
        )
        self.assertEqual(
            UserNotificationsUI.UNNotificationContentExtensionResponseOptionDismiss, 1
        )
        self.assertEqual(
            UserNotificationsUI.UNNotificationContentExtensionResponseOptionDismissAndForwardAction,
            2,
        )

    def test_protocols(self):
        objc.protocolNamed("UNNotificationContentExtension")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestUNNotificationContentExtensionHelper.didReceiveNotificationResponse_completionHandler_,
            1,
            b"v" + objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestUNNotificationContentExtensionHelper.mediaPlayPauseButtonType,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestUNNotificationContentExtensionHelper.mediaPlayPauseButtonFrame,
            UserNotificationsUI.NSRect.__typestr__,
        )
