from PyObjCTools.TestSupport import TestCase
import MailKit
import objc


class TestMEMessageEncoderHelper(MailKit.NSObject):
    def getEncodingStatusForMessage_completionHandler_(self, a, b):
        pass

    def getEncodingStatusForMessage_composeContext_completionHandler_(self, a, b, c):
        pass

    def encodeMessage_composeContext_completionHandler_(self, a, b, c):
        pass


class TestMEMessageEncoder(TestCase):
    def test_protocols(self):
        objc.protocolNamed("MEMessageEncoder")

    def test_methods(self):
        self.assertArgIsBlock(
            TestMEMessageEncoderHelper.getEncodingStatusForMessage_composeContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            TestMEMessageEncoderHelper.encodeMessage_composeContext_completionHandler_,
            2,
            b"v@",
        )
