from PyObjCTools.TestSupport import TestCase
import Intents


class TestINCallCapabilityOptions(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INCallCapabilityOptions)
        self.assertEqual(Intents.INCallCapabilityOptionAudioCall, 1 << 0)
        self.assertEqual(Intents.INCallCapabilityOptionVideoCall, 1 << 1)
