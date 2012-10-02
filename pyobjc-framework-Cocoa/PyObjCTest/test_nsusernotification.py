from PyObjCTools.TestSupport import *

import Foundation

try:
    unicode
except NameError:
    unicode = str

class UserNotificationHelper (Foundation.NSObject):
    def userNotificationCenter_shouldPresentNotification_(self, a, b): pass


class TestNSUserNotification (TestCase):
    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(Foundation.NSUserNotificationActivationTypeNone, 0)
        self.assertEqual(Foundation.NSUserNotificationActivationTypeContentsClicked, 1)
        self.assertEqual(Foundation.NSUserNotificationActivationTypeActionButtonClicked, 2)

        self.assertIsInstance(Foundation.NSUserNotificationDefaultSoundName, unicode)

    @min_os_level('10.8')
    def testMethods10_8(self):
        obj = Foundation.NSUserNotification.alloc().init()
        self.assertResultIsBOOL(obj.isPresented)
        self.assertResultIsBOOL(obj.isRemote)
        self.assertResultIsBOOL(obj.hasActionButton)
        self.assertArgIsBOOL(obj.setHasActionButton_, 0)

    @min_os_level('10.8')
    def testProtocol10_8(self):
        self.assertResultIsBOOL(UserNotificationHelper.userNotificationCenter_shouldPresentNotification_)

if __name__ == "__main__":
    main()
