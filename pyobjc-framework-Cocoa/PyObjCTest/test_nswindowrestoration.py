from PyObjCTools.TestSupport import *

import AppKit

try:
    unicode
except NameError:
    unicode = str

class RestorationHelper (AppKit.NSObject):
    def restoreWindowWithIdentifier_state_completionHandler_(self, a, b, c): pass


class TestNSWindowRestoration (TestCase):
    @min_os_level('10.7')
    @expectedFailure
    def testProtocol10_7(self):
        self.assertArgIsBlock(RestorationHelper.restoreWindowWithIdentifier_state_completionHandler_, 2, b'v@@')

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSApplication.restoreWindowWithIdentifier_state_completionHandler_)
        self.assertArgIsBlock(AppKit.NSApplication.restoreWindowWithIdentifier_state_completionHandler_, 2, b'v@@')

        self.assertArgIsBOOL(AppKit.NSWindow.setRestorable_, 0)
        self.assertResultIsBOOL(AppKit.NSWindow.isRestorable)

        self.assertArgIsBlock(AppKit.NSDocument.restoreDocumentWindowWithIdentifier_state_completionHandler_, 2, b'v@@')

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSApplicationDidFinishRestoringWindowsNotification,unicode)

if __name__ == "__main__":
    main()
