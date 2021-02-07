from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINCallCapabilityOptions(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INCallCapabilityOptionAudioCall, 1 << 0)
        self.assertEqual(Intents.INCallCapabilityOptionVideoCall, 1 << 1)
