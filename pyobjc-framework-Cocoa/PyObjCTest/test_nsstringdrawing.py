import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSStringDrawing(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSStringDrawingOptions)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertEqual(AppKit.NSStringDrawingTruncatesLastVisibleLine, (1 << 5))

    def testConstants(self):
        self.assertEqual(AppKit.NSStringDrawingUsesLineFragmentOrigin, (1 << 0))
        self.assertEqual(AppKit.NSStringDrawingUsesFontLeading, (1 << 1))
        self.assertEqual(AppKit.NSStringDrawingDisableScreenFontSubstitution, (1 << 2))
        self.assertEqual(AppKit.NSStringDrawingUsesDeviceMetrics, (1 << 3))
        self.assertEqual(AppKit.NSStringDrawingOneShot, (1 << 4))
