from PyObjCTools.TestSupport import TestCase
import MailKit  # noqa: F401


class TestMEMessageSecurityHandlerHelper(MailKit.NSObject):
    def primaryActionClickedForMessageContext_completionHandler_(self, a, b):
        pass


class TestMEMessageSecurityHandler(TestCase):
    def test_constants(self):
        self.assertEqual(MailKit.MEMessageSecurityEncodingError, 0)
        self.assertEqual(MailKit.MEMessageSecurityDecodingError, 1)

    def test_protocols(self):
        self.assertProtocolExists("MEMessageSecurityHandler")

    def test_methods(self):
        self.assertArgIsBlock(
            TestMEMessageSecurityHandlerHelper.primaryActionClickedForMessageContext_completionHandler_,
            1,
            b"v@",
        )
