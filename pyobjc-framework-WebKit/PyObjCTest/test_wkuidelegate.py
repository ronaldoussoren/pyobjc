from PyObjCTools.TestSupport import *
from WebKit import *

class TestWKUIDelegateHelper (NSObject):
    def webView_createWebViewWithConfiguration_forNavigationAction_windowFeatures_(self, w, c, a, f): return None
    def webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_completionHandler_(self, w, m, f, h): pass
    def webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_completionHandler_(self, w, m, f, h): pass
    def webView_runJavaScriptTextInputPanelWithPrompt_defaultText_initiatedByFrame_completionHandler_(self, w, p, d, f, h): pass
    def webView_runOpenPanelWithParameters_initiatedByFrame_completionHandler_(self, w, p, f, c): pass

class TestWKUIDelegate (TestCase):
    @onlyOn64Bit
    @min_os_level('10.10')
    def testProtocols10_10(self):
        p = objc.protocolNamed("WKUIDelegate")
        self.assertIsInstance(p, objc.formal_protocol)

        self.assertArgIsBlock(TestWKUIDelegateHelper.webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_completionHandler_, 3, b"v")
        self.assertArgIsBlock(TestWKUIDelegateHelper.webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_completionHandler_, 3, b"v")
        self.assertArgIsBlock(TestWKUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_completionHandler_, 3, b"v")
        self.assertArgIsBlock(TestWKUIDelegateHelper.webView_runJavaScriptTextInputPanelWithPrompt_defaultText_initiatedByFrame_completionHandler_, 4, b"v")
        self.assertArgIsBlock(TestWKUIDelegateHelper.webView_runOpenPanelWithParameters_initiatedByFrame_completionHandler_, 3, b"v@")

if __name__ == "__main__":
    main()
