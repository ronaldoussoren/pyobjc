from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit


class TestWKWebExtensionControllerDelegateHelper(WebKit.NSObject):
    def webExtensionController_openNewWindowUsingConfiguration_forExtensionContext_completionHandler_(
        self, a, b, c, d
    ):
        pass

    def webExtensionController_openNewTabUsingConfiguration_forExtensionContext_completionHandler_(
        self, a, b, c, d
    ):
        pass

    def webExtensionController_openOptionsPageForExtensionContext_completionHandler_(
        self, a, b, c
    ):
        pass

    def webExtensionController_promptForPermissions_inTab_forExtensionContext_completionHandler_(
        self, a, b, c, d, e
    ):
        pass

    def webExtensionController_promptForPermissionToAccessURLs_inTab_forExtensionContext_completionHandler_(
        self, a, b, c, d, e
    ):
        pass

    def webExtensionController_promptForPermissionMatchPatterns_inTab_forExtensionContext_completionHandler_(
        self, a, b, c, d, e
    ):
        pass

    def webExtensionController_presentPopupForAction_forExtensionContext_completionHandler_(
        self, a, b, c, d
    ):
        pass

    def webExtensionController_sendMessage_toApplicationWithIdentifier_forExtensionContext_replyHandler_(
        self, a, b, c, d, e
    ):
        pass

    def webExtensionController_connectUsingMessagePort_forExtensionContext_completionHandler_(
        self, a, b, c, d
    ):
        pass


class TestWKWebExtensionControllerDelegate(TestCase):
    @min_sdk_level("15.4")
    def test_protoocls(self):
        self.assertProtocolExists("WKWebExtensionControllerDelegate")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_openNewWindowUsingConfiguration_forExtensionContext_completionHandler_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_openNewTabUsingConfiguration_forExtensionContext_completionHandler_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_openOptionsPageForExtensionContext_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_promptForPermissions_inTab_forExtensionContext_completionHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_promptForPermissionToAccessURLs_inTab_forExtensionContext_completionHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_promptForPermissionMatchPatterns_inTab_forExtensionContext_completionHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_presentPopupForAction_forExtensionContext_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_sendMessage_toApplicationWithIdentifier_forExtensionContext_replyHandler_,
            4,
            b"v@@",
        )
        self.assertArgIsBlock(
            TestWKWebExtensionControllerDelegateHelper.webExtensionController_connectUsingMessagePort_forExtensionContext_completionHandler_,
            3,
            b"v@",
        )
