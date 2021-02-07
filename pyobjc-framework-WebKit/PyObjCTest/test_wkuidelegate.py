from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit  # noqa: F401
import objc


class TestWKUIDelegateHelper(WebKit.NSObject):
    def webView_createWebViewWithConfiguration_forNavigationAction_windowFeatures_(
        self, w, c, a, f
    ):
        return None

    def webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_completionHandler_(
        self, w, m, f, h
    ):
        pass

    def webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_completionHandler_(
        self, w, m, f, h
    ):
        pass

    def webView_runJavaScriptTextInputPanelWithPrompt_defaultText_initiatedByFrame_completionHandler_(  # noqa: B950
        self, w, p, d, f, h
    ):
        pass

    def webView_runOpenPanelWithParameters_initiatedByFrame_completionHandler_(
        self, w, p, f, c
    ):
        pass


class TestWKUIDelegate(TestCase):
    @min_os_level("10.10")
    def testProtocols10_10(self):
        p = objc.protocolNamed("WKUIDelegate")
        self.assertIsInstance(p, objc.formal_protocol)

        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_completionHandler_,  # noqa: B950
            3,
            b"v",
        )
        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_completionHandler_,  # noqa: B950
            3,
            b"v",
        )
        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_completionHandler_,  # noqa: B950
            3,
            b"v",
        )
        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runJavaScriptTextInputPanelWithPrompt_defaultText_initiatedByFrame_completionHandler_,  # noqa: B950
            4,
            b"v",
        )
        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runOpenPanelWithParameters_initiatedByFrame_completionHandler_,  # noqa: B950
            3,
            b"v@",
        )
