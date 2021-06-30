from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEMessageAction(TestCase):
    def test_constants(self):
        self.assertEqual(MailKit.MEMessageActionMessageColorNone, 0)
        self.assertEqual(MailKit.MEMessageActionMessageColorGreen, 1)
        self.assertEqual(MailKit.MEMessageActionMessageColorYellow, 2)
        self.assertEqual(MailKit.MEMessageActionMessageColorOrange, 3)
        self.assertEqual(MailKit.MEMessageActionMessageColorRed, 4)
        self.assertEqual(MailKit.MEMessageActionMessageColorPurple, 5)
        self.assertEqual(MailKit.MEMessageActionMessageColorBlue, 6)
        self.assertEqual(MailKit.MEMessageActionMessageColorGray, 7)

    def test_classes(self):
        MailKit.MEMessageAction
