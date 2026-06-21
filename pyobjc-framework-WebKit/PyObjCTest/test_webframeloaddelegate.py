from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit  # noqa: F401
import objc


class TestWebFrameLoadDelegateHelper(WebKit.NSObject):
    def webView_willPerformClientRedirectToURL_delay_fireDate_forFrame_(
        self, a, b, c, d, e
    ):
        pass


class TestWebFrameLoadDelegate(TestCase):
    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("WebFrameLoadDelegate", WebKit)

    def test_methods(self):
        self.assertArgHasType(
            TestWebFrameLoadDelegateHelper.webView_willPerformClientRedirectToURL_delay_fireDate_forFrame_,  # noqa: B950
            2,
            objc._C_DBL,
        )
