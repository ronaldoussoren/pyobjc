from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEMessage(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MailKit.MEMessageEncryptionState)
        self.assertIsEnumType(MailKit.MEMessageState)

    def test_constants(self):
        self.assertEqual(MailKit.MEMessageStateReceived, 0)
        self.assertEqual(MailKit.MEMessageStateDraft, 1)
        self.assertEqual(MailKit.MEMessageStateSending, 2)

        self.assertEqual(MailKit.MEMessageEncryptionStateUnknown, 0)
        self.assertEqual(MailKit.MEMessageEncryptionStateNotEncrypted, 1)
        self.assertEqual(MailKit.MEMessageEncryptionStateEncrypted, 2)

    def test_classes(self):
        MailKit.MEMessage
