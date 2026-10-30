from PyObjCTools.TestSupport import TestCase
import Intents


class TestINCallCapability(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Intents.INCallCapability)
        self.assertEqual(Intents.INCallCapabilityUnknown, 0)
        self.assertEqual(Intents.INCallCapabilityAudioCall, 1)
        self.assertEqual(Intents.INCallCapabilityVideoCall, 2)
