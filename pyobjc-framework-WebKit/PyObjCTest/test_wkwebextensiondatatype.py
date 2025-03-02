from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionDataType(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(WebKit.WKWebExtensionDataType, str)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(WebKit.WKWebExtensionDataTypeLocal, str)
        self.assertIsInstance(WebKit.WKWebExtensionDataTypeSession, str)
        self.assertIsInstance(WebKit.WKWebExtensionDataTypeSynchronized, str)
