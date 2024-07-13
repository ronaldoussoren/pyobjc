from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit  # noqa: F401


class TestWKHTTPCookieStoreObserver(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("WKHTTPCookieStoreObserver")
