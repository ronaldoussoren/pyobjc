from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEMessageSecurityInformation(TestCase):
    def test_classes(self):
        MailKit.MEMessageSecurityInformation

    def test_methods(self):
        self.assertResultIsBOOL(MailKit.MEMessageSecurityInformation.isEncrypted)
        self.assertResultIsBOOL(
            MailKit.MEMessageSecurityInformation.shouldBlockRemoteContent
        )

        self.assertArgIsBOOL(
            MailKit.MEMessageSecurityInformation.initWithSigners_isEncrypted_signingError_encryptionError_,
            1,
        )

        self.assertArgIsBOOL(
            MailKit.MEMessageSecurityInformation.initWithSigners_isEncrypted_signingError_encryptionError_shouldBlockRemoteContent_localizedRemoteContentBlockingReason_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            MailKit.MEMessageSecurityInformation.initWithSigners_isEncrypted_signingError_encryptionError_shouldBlockRemoteContent_localizedRemoteContentBlockingReason_,  # noqa: B950
            4,
        )
