from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEComposeContext(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MailKit.MEComposeUserAction)

    def test_constants(self):
        self.assertEqual(MailKit.MEComposeUserActionNewMessage, 1)
        self.assertEqual(MailKit.MEComposeUserActionReply, 2)
        self.assertEqual(MailKit.MEComposeUserActionReplyAll, 3)
        self.assertEqual(MailKit.MEComposeUserActionForward, 4)

    def test_methods(self):
        self.assertResultIsBOOL(MailKit.MEComposeContext.isEncrypted)
        self.assertResultIsBOOL(MailKit.MEComposeContext.shouldEncrypt)
        self.assertResultIsBOOL(MailKit.MEComposeContext.isSigned)
        self.assertResultIsBOOL(MailKit.MEComposeContext.shouldSign)
