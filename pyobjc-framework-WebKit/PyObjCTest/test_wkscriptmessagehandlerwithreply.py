from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc
import WebKit


class TestWKScriptMessageHandlerWithReplyHelper(WebKit.NSObject):
    def userContentController_didReceiveScriptMessage_replyHandler_(self, a, b, c):
        pass


class TestWKScriptMessageHandlerWithReply(TestCase):
    @min_sdk_level("10.16")
    def testProtocols10_16(self):
        objc.protocolNamed("WKScriptMessageHandlerWithReply")

    def testMethods(self):
        self.assertArgIsBlock(
            TestWKScriptMessageHandlerWithReplyHelper.userContentController_didReceiveScriptMessage_replyHandler_,
            2,
            b"v@@",
        )
