from PyObjCTools.TestSupport import TestCase
import Intents


class TestINOutgoingMessageType(TestCase):
    def test_constants(self):
        self.assertEqual(Intents.INOutgoingMessageTypeUnknown, 0)
        self.assertEqual(Intents.INOutgoingMessageTypeOutgoingMessageText, 1)
        self.assertEqual(Intents.INOutgoingMessageTypeOutgoingMessageAudio, 2)
