from PyObjCTools.TestSupport import TestCase
import MailKit  # noqa: F401


class TestMEMessageSecurityHandlerHelper(MailKit.NSObject):
    def primaryActionClickedForMessageContext_completionHandler_(self, a, b):
        pass


class TestMEMessageSecurityHandler(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MailKit.MEMessageSecurityErrorCode)
        self.assertEqual(MailKit.MEMessageSecurityEncodingError, 0)
        self.assertEqual(MailKit.MEMessageSecurityDecodingError, 1)

    def test_protocols(self):
        self.assertProtocolExists("MEMessageSecurityHandler", MailKit)

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestMEMessageSecurityHandlerHelper.primaryActionClickedForMessageContext_completionHandler_,
            1,
            b"v@",
        )
