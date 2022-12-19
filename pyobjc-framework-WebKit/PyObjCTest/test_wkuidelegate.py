from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit  # noqa: F401


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

    def webView_requestMediaCapturePermissionForOrigin_initiatedByFrame_type_decisionHandler_(
        self, a, b, c, d, e
    ):
        pass

    def webView_requestDeviceOrientationAndMotionPermissionForOrigin_initiatedByFrame_type_decisionHandler_(
        self, a, b, c, d, e
    ):
        pass


class TestWKUIDelegate(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKMediaCaptureType)
        self.assertIsEnumType(WebKit.WKPermissionDecision)

    @min_os_level("10.10")
    def testProtocols10_10(self):
        self.assertProtocolExists("WKUIDelegate")

        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runJavaScriptAlertPanelWithMessage_initiatedByFrame_completionHandler_,  # noqa: B950
            3,
            b"v",
        )
        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_completionHandler_,  # noqa: B950
            3,
            b"vZ",
        )
        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runJavaScriptTextInputPanelWithPrompt_defaultText_initiatedByFrame_completionHandler_,  # noqa: B950
            4,
            b"v@",
        )
        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_runOpenPanelWithParameters_initiatedByFrame_completionHandler_,  # noqa: B950
            3,
            b"v@",
        )

        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_requestMediaCapturePermissionForOrigin_initiatedByFrame_type_decisionHandler_,  # noqa: B950
            4,
            b"vq",
        )
        self.assertArgIsBlock(
            TestWKUIDelegateHelper.webView_requestDeviceOrientationAndMotionPermissionForOrigin_initiatedByFrame_type_decisionHandler_,  # noqa: B950
            4,
            b"vq",
        )

    def test_constants(self):
        self.assertEqual(WebKit.WKPermissionDecisionPrompt, 0)
        self.assertEqual(WebKit.WKPermissionDecisionGrant, 1)
        self.assertEqual(WebKit.WKPermissionDecisionDeny, 2)

        self.assertEqual(WebKit.WKMediaCaptureTypeCamera, 0)
        self.assertEqual(WebKit.WKMediaCaptureTypeMicrophone, 1)
        self.assertEqual(WebKit.WKMediaCaptureTypeCameraAndMicrophone, 2)
