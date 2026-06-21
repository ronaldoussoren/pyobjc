import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSTabViewItem(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTabState)

    def test_constants(self):
        self.assertEqual(AppKit.NSSelectedTab, 0)
        self.assertEqual(AppKit.NSBackgroundTab, 1)
        self.assertEqual(AppKit.NSPressedTab, 2)

    def test_methods(self):
        self.assertArgIsBOOL(AppKit.NSTabViewItem.drawLabel_inRect_, 0)
        self.assertArgIsBOOL(AppKit.NSTabViewItem.sizeOfLabel_, 0)
