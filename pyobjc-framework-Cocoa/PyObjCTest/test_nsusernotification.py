import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class UserNotificationHelper(Foundation.NSObject):
    def userNotificationCenter_shouldPresentNotification_(self, a, b):
        pass


class TestNSUserNotification(TestCase):
    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSUserNotificationActivationTypeNone, 0)
        self.assertEqual(Foundation.NSUserNotificationActivationTypeContentsClicked, 1)
        self.assertEqual(
            Foundation.NSUserNotificationActivationTypeActionButtonClicked, 2
        )
        self.assertEqual(Foundation.NSUserNotificationActivationTypeReplied, 3)
        self.assertEqual(
            Foundation.NSUserNotificationActivationTypeAdditionalActionClicked, 4
        )

        self.assertIsInstance(Foundation.NSUserNotificationDefaultSoundName, str)

    @min_os_level("10.8")
    def testMethods10_8(self):
        obj = Foundation.NSUserNotification.alloc().init()
        self.assertResultIsBOOL(obj.isPresented)
        self.assertResultIsBOOL(obj.isRemote)
        self.assertResultIsBOOL(obj.hasActionButton)
        self.assertArgIsBOOL(obj.setHasActionButton_, 0)

    @min_os_level("10.9")
    def testMethods10_9(self):
        obj = Foundation.NSUserNotification.alloc().init()
        self.assertResultIsBOOL(obj.hasReplyButton)
        self.assertArgIsBOOL(obj.setHasReplyButton_, 0)

    @min_os_level("10.8")
    def testProtocol10_8(self):
        self.assertResultIsBOOL(
            UserNotificationHelper.userNotificationCenter_shouldPresentNotification_
        )

    @min_os_level("10.10")
    def testProtocolsObjects(self):
        objc.protocolNamed("NSUserNotificationCenterDelegate")
