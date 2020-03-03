import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioUnitTimeEffect(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitTimeEffect.bypass)
        self.assertArgIsBOOL(AVFoundation.AVAudioUnitTimeEffect.setBypass_, 0)
