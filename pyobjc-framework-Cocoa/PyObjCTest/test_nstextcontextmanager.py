import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSTextContentManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTextContentManagerEnumerationOptions)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertEqual(AppKit.NSTextElementProviderEnumerationOptionsNone, 0)
        self.assertEqual(AppKit.NSTextElementProviderEnumerationOptionsReverse, 1 << 0)

    @min_sdk_level("12.0")
    def testProtocols(self):
        objc.protocolNamed("NSTextElementProvider")

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(AppKit.NSAppearance.allowsVibrancy)
