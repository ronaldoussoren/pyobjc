from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit
import objc


class TestWKNavigationDelegateHelper(WebKit.NSObject):
    def webView_decidePolicyForNavigationAction_decisionHandler_(self, w, a, h):
        pass

    def webView_decidePolicyForNavigationResponse_decisionHandler_(self, w, r, h):
        pass

    def webView_didReceiveAuthenticationChallenge_completionHandler_(self, w, c, h):
        pass

    def webView_authenticationChallenge_shouldAllowDeprecatedTLS_(self, w, c, h):
        pass


class TestWKNavigationDelegate(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKNavigationActionPolicy)
        self.assertIsEnumType(WebKit.WKNavigationResponsePolicy)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(WebKit.WKErrorDomain, str)

        self.assertEqual(WebKit.WKNavigationActionPolicyCancel, 0)
        self.assertEqual(WebKit.WKNavigationActionPolicyAllow, 1)
        self.assertEqual(WebKit.WKNavigationActionPolicyDownload, 2)

        self.assertEqual(WebKit.WKNavigationResponsePolicyCancel, 0)
        self.assertEqual(WebKit.WKNavigationResponsePolicyAllow, 1)
        self.assertEqual(WebKit.WKNavigationResponsePolicyDownload, 2)

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("WKNavigationDelegate")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestWKNavigationDelegateHelper.webView_decidePolicyForNavigationAction_decisionHandler_,  # noqa: B950
            2,
            objc._C_VOID + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestWKNavigationDelegateHelper.webView_decidePolicyForNavigationResponse_decisionHandler_,  # noqa: B950
            2,
            objc._C_VOID + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestWKNavigationDelegateHelper.webView_didReceiveAuthenticationChallenge_completionHandler_,  # noqa: B950
            2,
            objc._C_VOID + objc._C_NSInteger + objc._C_ID,
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertArgIsBlock(
            TestWKNavigationDelegateHelper.webView_authenticationChallenge_shouldAllowDeprecatedTLS_,
            2,
            b"vZ",
        )
