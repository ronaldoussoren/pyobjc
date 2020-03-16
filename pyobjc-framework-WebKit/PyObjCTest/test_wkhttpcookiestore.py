from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit
import WebKit


class TestWKError(TestCase):
    @onlyOn64Bit
    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsBlock(WebKit.WKHTTPCookieStore.getAllCookies_, 0, b"v@")
        self.assertArgIsBlock(
            WebKit.WKHTTPCookieStore.setCookie_completionHandler_, 1, b"v"
        )
        self.assertArgIsBlock(
            WebKit.WKHTTPCookieStore.deleteCookie_completionHandler_, 1, b"v"
        )
