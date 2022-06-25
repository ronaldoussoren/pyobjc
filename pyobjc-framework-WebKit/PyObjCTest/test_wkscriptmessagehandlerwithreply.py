from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit


class TestWKScriptMessageHandlerWithReplyHelper(WebKit.NSObject):
    def userContentController_didReceiveScriptMessage_replyHandler_(self, a, b, c):
        pass


class TestWKScriptMessageHandlerWithReply(TestCase):
    @min_sdk_level("11.0")
    def testProtocols11_0(self):
        self.assertProtocolExists("WKScriptMessageHandlerWithReply")

    def testMethods(self):
        self.assertArgIsBlock(
            TestWKScriptMessageHandlerWithReplyHelper.userContentController_didReceiveScriptMessage_replyHandler_,
            2,
            b"v@@",
        )
