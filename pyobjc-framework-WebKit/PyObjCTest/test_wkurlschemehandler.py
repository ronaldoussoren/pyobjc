from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit  # noqa: F401


class TestWKURLSchemeHandler(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("WKURLSchemeHandler")
