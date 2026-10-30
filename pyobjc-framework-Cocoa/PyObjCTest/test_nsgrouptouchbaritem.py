import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSGroupTouchBarItem(TestCase):
    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSGroupTouchBarItem.prefersEqualWidths)
        self.assertArgIsBOOL(AppKit.NSGroupTouchBarItem.setPrefersEqualWidths_, 0)
