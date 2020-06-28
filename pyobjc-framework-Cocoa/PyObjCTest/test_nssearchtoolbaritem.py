import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSearchToolbarItem(TestCase):
    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(
            AppKit.NSSearchToolbarItem.resignsFirstResponderWithCancel
        )
        self.assertArgIsBOOL(
            AppKit.NSSearchToolbarItem.setResignsFirstResponderWithCancel_, 0
        )
