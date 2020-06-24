import BusinessChat
from PyObjCTools.TestSupport import TestCase


class TestBCChatAction(TestCase):
    def test_constants(self):
        self.assertIsInstance(BusinessChat.BCParameterNameIntent, str)
        self.assertIsInstance(BusinessChat.BCParameterNameGroup, str)
        self.assertIsInstance(BusinessChat.BCParameterNameBody, str)

    def test_classes(self):
        BusinessChat.BCChatAction
