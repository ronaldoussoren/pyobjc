from PyObjCTools.TestSupport import TestCase
import MailKit
import objc


class TestMEMessageEncoderHelper(MailKit.NSObject):
    def getEncodingStatusForMessage_completionHandler_(self, a, b):
        pass

    def encodeMessage_shouldSign_shouldEncrypt_completionHandler_(self, a, b, c, d):
        pass


class TestMEMessageEncoder(TestCase):
    def test_protocols(self):
        objc.protocolNamed("MEMessageEncoder")

    def test_methods(self):
        self.assertArgIsBlock(
            TestMEMessageEncoderHelper.getEncodingStatusForMessage_completionHandler_,
            1,
            b"v@",
        )

        self.assertArgIsBOOL(
            TestMEMessageEncoderHelper.encodeMessage_shouldSign_shouldEncrypt_completionHandler_,
            1,
        )
        self.assertArgIsBOOL(
            TestMEMessageEncoderHelper.encodeMessage_shouldSign_shouldEncrypt_completionHandler_,
            2,
        )
        self.assertArgIsBlock(
            TestMEMessageEncoderHelper.encodeMessage_shouldSign_shouldEncrypt_completionHandler_,
            3,
            b"v@",
        )
