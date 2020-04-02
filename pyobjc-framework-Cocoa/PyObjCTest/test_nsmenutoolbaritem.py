import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMenuToolbarItem(TestCase):
    @min_os_level("10.15")
    def test_nethods10_15(self):
        self.assertResultIsBOOL(AppKit.NSMenuToolbarItem.showsIndicator)
        self.assertArgIsBOOL(AppKit.NSMenuToolbarItem.setShowsIndicator_, 0)
