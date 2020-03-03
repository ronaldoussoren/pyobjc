import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioUnitEffect(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioUnitGenerator.bypass)
        self.assertArgIsBOOL(AVFoundation.AVAudioUnitGenerator.setBypass_, 0)
