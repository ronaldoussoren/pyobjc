from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEMessage(TestCase):
    def test_constants(self):
        self.assertEqual(MailKit.MEMessageStateReceived, 0)
        self.assertEqual(MailKit.MEMessageStateDraft, 1)
        self.assertEqual(MailKit.MEMessageStateSending, 2)

    def test_classes(self):
        MailKit.MEMessage
