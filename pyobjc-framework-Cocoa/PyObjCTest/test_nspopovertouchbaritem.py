import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPopoverTouchBarItem(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSPopoverTouchBarItem.showsCloseButton)
        self.assertArgIsBOOL(AppKit.NSPopoverTouchBarItem.setShowsCloseButton_, 0)
