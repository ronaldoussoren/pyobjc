import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSTextContent(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSTextContentType, str)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(AppKit.NSTextContentTypeUsername, str)
        self.assertIsInstance(AppKit.NSTextContentTypePassword, str)
        self.assertIsInstance(AppKit.NSTextContentTypeOneTimeCode, str)

    @min_sdk_level("11.0")
    def test_protocols(self):
        objc.protocolNamed("NSTextContent")
