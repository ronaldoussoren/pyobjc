import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSTextContent(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(AppKit.NSTextContentTypeUsername, str)
        self.assertIsInstance(AppKit.NSTextContentTypePassword, str)
        self.assertIsInstance(AppKit.NSTextContentTypeOneTimeCode, str)

    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("NSTextContent")
