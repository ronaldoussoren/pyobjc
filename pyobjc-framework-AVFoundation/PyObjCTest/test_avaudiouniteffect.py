import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioUnitEffect(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitEffect.bypass)
        self.assertArgIsBOOL(AVFoundation.AVAudioUnitEffect.setBypass_, 0)
