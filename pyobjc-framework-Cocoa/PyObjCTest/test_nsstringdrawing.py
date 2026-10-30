import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSStringDrawing(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSStringDrawingOptions)
        self.assertEqual(AppKit.NSStringDrawingUsesLineFragmentOrigin, (1 << 0))
        self.assertEqual(AppKit.NSStringDrawingUsesFontLeading, (1 << 1))
        self.assertEqual(AppKit.NSStringDrawingDisableScreenFontSubstitution, (1 << 2))
        self.assertEqual(AppKit.NSStringDrawingUsesDeviceMetrics, (1 << 3))
        self.assertEqual(AppKit.NSStringDrawingOneShot, (1 << 4))
        self.assertEqual(AppKit.NSStringDrawingTruncatesLastVisibleLine, (1 << 5))
        self.assertEqual(
            AppKit.NSStringDrawingOptionsResolvesNaturalAlignmentWithBaseWritingDirection,
            (1 << 9),
        )
