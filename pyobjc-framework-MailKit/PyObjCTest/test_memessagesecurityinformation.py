from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEMessageSecurityInformation(TestCase):
    def test_classes(self):
        MailKit.MEMessageSecurityInformation

    def test_methods(self):
        self.assertResultIsBOOL(MailKit.MEMessageSecurityInformation.isEncrypted)

        self.assertArgIsBOOL(
            MailKit.MEMessageSecurityInformation.initWithSigners_isEncrypted_signingError_,
            1,
        )
