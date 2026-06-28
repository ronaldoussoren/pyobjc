import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTableColumn(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTableColumnResizingOptions)
        self.assertEqual(AppKit.NSTableColumnNoResizing, 0)
        self.assertEqual(AppKit.NSTableColumnAutoresizingMask, (1 << 0))
        self.assertEqual(AppKit.NSTableColumnUserResizingMask, (1 << 1))

    def test_methods(self):
        self.assertArgIsBOOL(AppKit.NSTableColumn.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSTableColumn.isEditable)
        self.assertArgIsBOOL(AppKit.NSTableColumn.setResizable_, 0)
        self.assertResultIsBOOL(AppKit.NSTableColumn.isResizable)

        self.assertArgIsBOOL(AppKit.NSTableColumn.setHidden_, 0)
        self.assertResultIsBOOL(AppKit.NSTableColumn.isHidden)
