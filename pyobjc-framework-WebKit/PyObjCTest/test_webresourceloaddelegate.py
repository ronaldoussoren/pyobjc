from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc
import WebKit  # noqa: F401


class TestWebResourceLoadDelegateHelper(WebKit.NSObject):
    def webView_resource_didReceiveContentLength_fromDataSource_(self, a, b, c, d):
        pass


class TestWebResourceLoadDelegate(TestCase):
    @min_sdk_level("10.11")
    def testProtocols(self):
        self.assertProtocolExists("WebResourceLoadDelegate")

    def testMethods(self):
        self.assertArgHasType(
            TestWebResourceLoadDelegateHelper.webView_resource_didReceiveContentLength_fromDataSource_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
