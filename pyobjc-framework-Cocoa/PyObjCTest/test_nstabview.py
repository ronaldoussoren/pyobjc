import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTabViewHelper(AppKit.NSObject):
    def tabView_shouldSelectTabViewItem_(self, tv, it):
        return 1


class TestNSTabView(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTabPosition)
        self.assertIsEnumType(AppKit.NSTabViewBorderType)
        self.assertIsEnumType(AppKit.NSTabViewType)

    def testConstants(self):
        self.assertEqual(AppKit.NSTopTabsBezelBorder, 0)
        self.assertEqual(AppKit.NSLeftTabsBezelBorder, 1)
        self.assertEqual(AppKit.NSBottomTabsBezelBorder, 2)
        self.assertEqual(AppKit.NSRightTabsBezelBorder, 3)
        self.assertEqual(AppKit.NSNoTabsBezelBorder, 4)
        self.assertEqual(AppKit.NSNoTabsLineBorder, 5)
        self.assertEqual(AppKit.NSNoTabsNoBorder, 6)

        self.assertEqual(AppKit.NSTabPositionNone, 0)
        self.assertEqual(AppKit.NSTabPositionTop, 1)
        self.assertEqual(AppKit.NSTabPositionLeft, 2)
        self.assertEqual(AppKit.NSTabPositionBottom, 3)
        self.assertEqual(AppKit.NSTabPositionRight, 4)

        self.assertEqual(AppKit.NSTabViewBorderTypeNone, 0)
        self.assertEqual(AppKit.NSTabViewBorderTypeLine, 1)
        self.assertEqual(AppKit.NSTabViewBorderTypeBezel, 2)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTabView.allowsTruncatedLabels)
        self.assertResultIsBOOL(AppKit.NSTabView.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSTabView.setAllowsTruncatedLabels_, 0)
        self.assertArgIsBOOL(AppKit.NSTabView.setDrawsBackground_, 0)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSTabViewHelper.tabView_shouldSelectTabViewItem_)
