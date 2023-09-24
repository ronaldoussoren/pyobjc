from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit
import objc


class TestWKError(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKCookiePolicy)
        self.assertEqual(WebKit.WKCookiePolicyAllow, 0)
        self.assertEqual(WebKit.WKCookiePolicyDisallow, 1)

    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsBlock(WebKit.WKHTTPCookieStore.getAllCookies_, 0, b"v@")
        self.assertArgIsBlock(
            WebKit.WKHTTPCookieStore.setCookie_completionHandler_, 1, b"v"
        )
        self.assertArgIsBlock(
            WebKit.WKHTTPCookieStore.deleteCookie_completionHandler_, 1, b"v"
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            WebKit.WKHTTPCookieStore.setCookiePolicy_completionHandler_, 1, b"v"
        )
        self.assertArgIsBlock(
            WebKit.WKHTTPCookieStore.getCookiePolicy_,
            0,
            b"v" + objc._C_NSInteger,
        )
