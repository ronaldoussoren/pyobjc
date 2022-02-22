import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSilderTouchBarItem(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSSliderAccessoryWidth, float)

    @min_os_level("10.12.2")
    def testConstants(self):
        self.assertIsInstance(AppKit.NSSliderAccessoryWidthDefault, float)
        self.assertIsInstance(AppKit.NSSliderAccessoryWidthWide, float)
