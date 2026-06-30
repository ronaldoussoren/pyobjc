from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEMessage(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MailKit.MEMessageEncryptionState)
        self.assertEqual(MailKit.MEMessageEncryptionStateUnknown, 0)
        self.assertEqual(MailKit.MEMessageEncryptionStateNotEncrypted, 1)
        self.assertEqual(MailKit.MEMessageEncryptionStateEncrypted, 2)

        self.assertIsEnumType(MailKit.MEMessageState)
        self.assertEqual(MailKit.MEMessageStateReceived, 0)
        self.assertEqual(MailKit.MEMessageStateDraft, 1)
        self.assertEqual(MailKit.MEMessageStateSending, 2)

    def test_classes(self):
        MailKit.MEMessage
