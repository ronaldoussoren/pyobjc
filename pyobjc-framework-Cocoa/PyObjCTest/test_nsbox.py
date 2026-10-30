import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSBox(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTitlePosition)
        self.assertEqual(AppKit.NSNoTitle, 0)
        self.assertEqual(AppKit.NSAboveTop, 1)
        self.assertEqual(AppKit.NSAtTop, 2)
        self.assertEqual(AppKit.NSBelowTop, 3)
        self.assertEqual(AppKit.NSAboveBottom, 4)
        self.assertEqual(AppKit.NSAtBottom, 5)
        self.assertEqual(AppKit.NSBelowBottom, 6)

        self.assertIsEnumType(AppKit.NSBoxType)
        self.assertEqual(AppKit.NSBoxPrimary, 0)
        self.assertEqual(AppKit.NSBoxSecondary, 1)
        self.assertEqual(AppKit.NSBoxSeparator, 2)
        self.assertEqual(AppKit.NSBoxOldStyle, 3)
        self.assertEqual(AppKit.NSBoxCustom, 4)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSBox.isTransparent)
        self.assertArgIsBOOL(AppKit.NSBox.setTransparent_, 0)
