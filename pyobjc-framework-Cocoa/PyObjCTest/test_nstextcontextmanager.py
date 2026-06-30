import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSTextContentManager(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSTextContentManagerEnumerationOptions)
        self.assertEqual(AppKit.NSTextElementProviderEnumerationOptionsNone, 0)
        self.assertEqual(AppKit.NSTextElementProviderEnumerationOptionsReverse, 1 << 0)

    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("NSTextElementProvider", AppKit)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(AppKit.NSAppearance.allowsVibrancy)
