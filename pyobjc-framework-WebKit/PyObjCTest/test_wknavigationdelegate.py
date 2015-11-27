from PyObjCTools.TestSupport import *
from WebKit import *

class TestWKNavigationDelegateHelper (NSObject):
    def webView_decidePolicyForNavigationAction_decisionHandler_(self, w, a, h): pass
    def webView_decidePolicyForNavigationResponse_decisionHandler_(self, w, r, h): pass
    def webView_didReceiveAuthenticationChallenge_completionHandler_(self, w, c, h): pass



class TestWKNavigationDelegate (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(WKErrorDomain, unicode)

        self.assertEqual(WKNavigationActionPolicyCancel, 0)
        self.assertEqual(WKNavigationActionPolicyAllow, 1)

        self.assertEqual(WKNavigationResponsePolicyCancel, 0)
        self.assertEqual(WKNavigationResponsePolicyAllow, 1)

    @onlyOn64Bit
    @min_os_level('10.10')
    def testProtocols(self):
        p = objc.protocolNamed('WKNavigationDelegate')
        self.assertIsInstance(p, objc.formal_protocol)

        self.assertArgIsBlock(TestWKNavigationDelegateHelper.webView_decidePolicyForNavigationAction_decisionHandler_, 2, objc._C_VOID + objc._C_NSInteger)
        self.assertArgIsBlock(TestWKNavigationDelegateHelper.webView_decidePolicyForNavigationResponse_decisionHandler_, 2, objc._C_VOID + objc._C_NSInteger)
        self.assertArgIsBlock(TestWKNavigationDelegateHelper.webView_didReceiveAuthenticationChallenge_completionHandler_, 2, objc._C_VOID + objc._C_NSInteger + objc._C_ID)

if __name__ == "__main__":
    main()
