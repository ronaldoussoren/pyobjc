import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextList(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSTextListMarkerFormat, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTextListOptions)

    def testConstants(self):
        self.assertEqual(AppKit.NSTextListPrependEnclosingMarker, 1)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AppKit.NSTextListMarkerBox, str)
        self.assertIsInstance(AppKit.NSTextListMarkerCheck, str)
        self.assertIsInstance(AppKit.NSTextListMarkerCircle, str)
        self.assertIsInstance(AppKit.NSTextListMarkerDiamond, str)
        self.assertIsInstance(AppKit.NSTextListMarkerDisc, str)
        self.assertIsInstance(AppKit.NSTextListMarkerHyphen, str)
        self.assertIsInstance(AppKit.NSTextListMarkerSquare, str)
        self.assertIsInstance(AppKit.NSTextListMarkerLowercaseHexadecimal, str)
        self.assertIsInstance(AppKit.NSTextListMarkerUppercaseHexadecimal, str)
        self.assertIsInstance(AppKit.NSTextListMarkerOctal, str)
        self.assertIsInstance(AppKit.NSTextListMarkerLowercaseAlpha, str)
        self.assertIsInstance(AppKit.NSTextListMarkerUppercaseAlpha, str)
        self.assertIsInstance(AppKit.NSTextListMarkerLowercaseLatin, str)
        self.assertIsInstance(AppKit.NSTextListMarkerUppercaseLatin, str)
        self.assertIsInstance(AppKit.NSTextListMarkerLowercaseRoman, str)
        self.assertIsInstance(AppKit.NSTextListMarkerUppercaseRoman, str)
        self.assertIsInstance(AppKit.NSTextListMarkerDecimal, str)

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(AppKit.NSTextList.includesTextListMarkers)
