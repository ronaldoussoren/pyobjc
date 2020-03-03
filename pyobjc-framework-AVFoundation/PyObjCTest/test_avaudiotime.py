import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioTime(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsIn(
            AVFoundation.AVAudioTime.initWithAudioTimeStamp_sampleRate_, 0
        )
        self.assertArgIsIn(
            AVFoundation.AVAudioTime.timeWithAudioTimeStamp_sampleRate_, 0
        )

        self.assertResultIsBOOL(AVFoundation.AVAudioTime.isHostTimeValid)
        self.assertResultIsBOOL(AVFoundation.AVAudioTime.isSampleTimeValid)
