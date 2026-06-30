import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSUserInterfaceLayout(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSUserInterfaceLayoutDirection)
        self.assertEqual(AppKit.NSUserInterfaceLayoutDirectionLeftToRight, 0)
        self.assertEqual(AppKit.NSUserInterfaceLayoutDirectionRightToLeft, 1)

        self.assertIsEnumType(AppKit.NSUserInterfaceLayoutOrientation)
        self.assertEqual(AppKit.NSUserInterfaceLayoutOrientationHorizontal, 0)
        self.assertEqual(AppKit.NSUserInterfaceLayoutOrientationVertical, 1)
