import Foundation
from PyObjCTools.TestSupport import TestCase


class UserNotificationHelper(Foundation.NSObject):
    def userNotificationCenter_shouldPresentNotification_(self, a, b):
        pass


class TestNSUserNotification(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSUserNotificationActivationType)
        self.assertEqual(Foundation.NSUserNotificationActivationTypeNone, 0)
        self.assertEqual(Foundation.NSUserNotificationActivationTypeContentsClicked, 1)
        self.assertEqual(
            Foundation.NSUserNotificationActivationTypeActionButtonClicked, 2
        )
        self.assertEqual(Foundation.NSUserNotificationActivationTypeReplied, 3)
        self.assertEqual(
            Foundation.NSUserNotificationActivationTypeAdditionalActionClicked, 4
        )

    def test_constants(self):
        self.assertIsInstance(Foundation.NSUserNotificationDefaultSoundName, str)

    def test_methods(self):
        obj = Foundation.NSUserNotification.alloc().init()
        self.assertResultIsBOOL(obj.isPresented)
        self.assertResultIsBOOL(obj.isRemote)
        self.assertResultIsBOOL(obj.hasActionButton)
        self.assertArgIsBOOL(obj.setHasActionButton_, 0)

        obj = Foundation.NSUserNotification.alloc().init()
        self.assertResultIsBOOL(obj.hasReplyButton)
        self.assertArgIsBOOL(obj.setHasReplyButton_, 0)

    def test_protocols(self):
        self.assertProtocolExists("NSUserNotificationCenterDelegate", Foundation)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            UserNotificationHelper.userNotificationCenter_shouldPresentNotification_
        )
