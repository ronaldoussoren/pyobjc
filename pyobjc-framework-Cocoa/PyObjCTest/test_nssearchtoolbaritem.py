import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSearchToolbarItem(TestCase):
    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            AppKit.NSSearchToolbarItem.resignsFirstResponderWithCancel
        )
        self.assertArgIsBOOL(
            AppKit.NSSearchToolbarItem.setResignsFirstResponderWithCancel_, 0
        )
