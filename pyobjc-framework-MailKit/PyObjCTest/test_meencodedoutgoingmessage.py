from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEEncodedOutgoingMessage(TestCase):
    def test_classes(self):
        MailKit.MEEncodedOutgoingMessage

    def test_methods(self):
        self.assertResultIsBOOL(MailKit.MEEncodedOutgoingMessage.isSigned)
        self.assertResultIsBOOL(MailKit.MEEncodedOutgoingMessage.isEncrypted)
