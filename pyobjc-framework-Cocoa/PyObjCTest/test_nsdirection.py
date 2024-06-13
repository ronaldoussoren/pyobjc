import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSDirection(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AppKit.NSHorizontalDirections)
        self.assertEqual(AppKit.NSHorizontalDirectionsLeft, 1 << 0)
        self.assertEqual(AppKit.NSHorizontalDirectionsRight, 1 << 1)
        self.assertEqual(
            AppKit.NSHorizontalDirectionsAll,
            AppKit.NSHorizontalDirectionsLeft | AppKit.NSHorizontalDirectionsRight,
        )

        self.assertIsEnumType(AppKit.NSVerticalDirections)
        self.assertEqual(AppKit.NSVerticalDirectionsUp, 1 << 0)
        self.assertEqual(AppKit.NSVerticalDirectionsDown, 1 << 1)
        self.assertEqual(
            AppKit.NSVerticalDirectionsAll,
            AppKit.NSVerticalDirectionsUp | AppKit.NSVerticalDirectionsDown,
        )
