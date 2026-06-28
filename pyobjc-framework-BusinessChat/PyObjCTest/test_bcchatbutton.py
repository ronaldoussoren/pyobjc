import BusinessChat
from PyObjCTools.TestSupport import TestCase


class TestBCChatButton(TestCase):
    def test_enums(self):
        self.assertIsEnumType(BusinessChat.BCChatButtonStyle)
        self.assertEqual(BusinessChat.BCChatButtonStyleLight, 0)
        self.assertEqual(BusinessChat.BCChatButtonStyleDark, 1)

    def test_classes(self):
        BusinessChat.BCChatButton
