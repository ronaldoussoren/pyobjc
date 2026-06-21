import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTableColumn(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTableColumnResizingOptions)

    def test_constants(self):
        self.assertEqual(AppKit.NSTableColumnNoResizing, 0)
        self.assertEqual(AppKit.NSTableColumnAutoresizingMask, (1 << 0))
        self.assertEqual(AppKit.NSTableColumnUserResizingMask, (1 << 1))

    def test_methods(self):
        self.assertArgIsBOOL(AppKit.NSTableColumn.setEditable_, 0)
        self.assertResultIsBOOL(AppKit.NSTableColumn.isEditable)
        self.assertArgIsBOOL(AppKit.NSTableColumn.setResizable_, 0)
        self.assertResultIsBOOL(AppKit.NSTableColumn.isResizable)

    @min_os_level("10.5")
    def test_methods10_5(self):
        self.assertArgIsBOOL(AppKit.NSTableColumn.setHidden_, 0)
        self.assertResultIsBOOL(AppKit.NSTableColumn.isHidden)
