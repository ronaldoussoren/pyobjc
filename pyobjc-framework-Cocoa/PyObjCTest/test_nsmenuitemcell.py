import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSMenuItemCell(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSMenuItemCell.needsSizing)
        self.assertArgIsBOOL(AppKit.NSMenuItemCell.setNeedsSizing_, 0)
        self.assertResultIsBOOL(AppKit.NSMenuItemCell.needsDisplay)
        self.assertArgIsBOOL(AppKit.NSMenuItemCell.setNeedsDisplay_, 0)
