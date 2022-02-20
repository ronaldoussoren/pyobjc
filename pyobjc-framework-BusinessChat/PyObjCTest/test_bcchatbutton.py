import BusinessChat
from PyObjCTools.TestSupport import TestCase


class TestBCChatButton(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(BusinessChat.BCChatButtonStyle)

    def test_constants(self):
        self.assertEqual(BusinessChat.BCChatButtonStyleLight, 0)
        self.assertEqual(BusinessChat.BCChatButtonStyleDark, 1)

    def test_classes(self):
        BusinessChat.BCChatButton
