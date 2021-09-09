from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEOutgoingMessageEncodingStatus(TestCase):
    def test_classes(self):
        MailKit.MEOutgoingMessageEncodingStatus

    def test_methods(self):
        self.assertResultIsBOOL(MailKit.MEOutgoingMessageEncodingStatus.canSign)
        self.assertResultIsBOOL(MailKit.MEOutgoingMessageEncodingStatus.canEncrypt)

        self.assertArgIsBOOL(
            MailKit.MEOutgoingMessageEncodingStatus.initWithCanSign_canEncrypt_securityError_addressesFailingEncryption_,
            0,
        )
        self.assertArgIsBOOL(
            MailKit.MEOutgoingMessageEncodingStatus.initWithCanSign_canEncrypt_securityError_addressesFailingEncryption_,
            1,
        )
