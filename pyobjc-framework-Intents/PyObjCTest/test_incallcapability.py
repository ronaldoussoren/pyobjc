from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINCallCapability(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INCallCapability)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INCallCapabilityUnknown, 0)
        self.assertEqual(Intents.INCallCapabilityAudioCall, 1)
        self.assertEqual(Intents.INCallCapabilityVideoCall, 2)
