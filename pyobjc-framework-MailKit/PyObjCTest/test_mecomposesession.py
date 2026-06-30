from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEComposeSessionHelper(MailKit.NSObject):
    def session_annotateAddressesWithCompletionHandler_(self, a, b):
        pass

    def session_canSendMessageWithCompletionHandler_(self, a, b):
        pass


class TestMEComposeSession(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MailKit.MEComposeSessionErrorCode)
        self.assertEqual(MailKit.MEComposeSessionErrorCodeInvalidRecipients, 0)
        self.assertEqual(MailKit.MEComposeSessionErrorCodeInvalidHeaders, 1)
        self.assertEqual(MailKit.MEComposeSessionErrorCodeInvalidBody, 2)

    def test_classes(self):
        MailKit.MEComposeSession

    def test_protocols(self):
        self.assertProtocolExists("MEComposeSessionHandler", MailKit)

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestMEComposeSessionHelper.session_annotateAddressesWithCompletionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestMEComposeSessionHelper.session_canSendMessageWithCompletionHandler_,
            1,
            b"v@",
        )
