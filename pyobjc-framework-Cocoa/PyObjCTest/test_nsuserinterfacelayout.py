import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSUserInterfaceLayout(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSUserInterfaceLayoutDirection)
        self.assertIsEnumType(AppKit.NSUserInterfaceLayoutOrientation)

    def testConstants(self):
        self.assertEqual(AppKit.NSUserInterfaceLayoutDirectionLeftToRight, 0)
        self.assertEqual(AppKit.NSUserInterfaceLayoutDirectionRightToLeft, 1)
        self.assertEqual(AppKit.NSUserInterfaceLayoutOrientationHorizontal, 0)
        self.assertEqual(AppKit.NSUserInterfaceLayoutOrientationVertical, 1)
