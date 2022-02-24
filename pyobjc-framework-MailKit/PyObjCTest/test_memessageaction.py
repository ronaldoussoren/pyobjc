from PyObjCTools.TestSupport import TestCase
import MailKit


class TestMEMessageAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MailKit.MEMessageActionFlag)

    def test_constants(self):
        self.assertEqual(MailKit.MEMessageActionMessageColorNone, 0)
        self.assertEqual(MailKit.MEMessageActionMessageColorGreen, 1)
        self.assertEqual(MailKit.MEMessageActionMessageColorYellow, 2)
        self.assertEqual(MailKit.MEMessageActionMessageColorOrange, 3)
        self.assertEqual(MailKit.MEMessageActionMessageColorRed, 4)
        self.assertEqual(MailKit.MEMessageActionMessageColorPurple, 5)
        self.assertEqual(MailKit.MEMessageActionMessageColorBlue, 6)
        self.assertEqual(MailKit.MEMessageActionMessageColorGray, 7)

        self.assertEqual(MailKit.MEMessageActionFlagNone, 0)
        self.assertEqual(MailKit.MEMessageActionFlagDefaultColor, 1)
        self.assertEqual(MailKit.MEMessageActionFlagRed, 2)
        self.assertEqual(MailKit.MEMessageActionFlagOrange, 3)
        self.assertEqual(MailKit.MEMessageActionFlagYellow, 4)
        self.assertEqual(MailKit.MEMessageActionFlagGreen, 5)
        self.assertEqual(MailKit.MEMessageActionFlagBlue, 6)
        self.assertEqual(MailKit.MEMessageActionFlagPurple, 7)
        self.assertEqual(MailKit.MEMessageActionFlagGray, 8)

    def test_classes(self):
        MailKit.MEMessageAction
