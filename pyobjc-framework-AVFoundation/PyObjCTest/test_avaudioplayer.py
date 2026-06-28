import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAVAudioPlayerHelper(AVFoundation.NSObject):
    def audioPlayerDidFinishPlaying_successfully_(self, a, b):
        pass


class TestAVAudioPlayer(TestCase):
    def test_methods(self):
        self.assertArgIsOut(AVFoundation.AVAudioPlayer.initWithContentsOfURL_error_, 1)
        self.assertArgIsOut(AVFoundation.AVAudioPlayer.initWithData_error_, 1)

        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.prepareToPlay)
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.play)
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.playAtTime_)
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.isPlaying)

        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.isMeteringEnabled)
        self.assertArgIsBOOL(AVFoundation.AVAudioPlayer.setMeteringEnabled_, 0)

        self.assertArgIsBOOL(
            TestAVAudioPlayerHelper.audioPlayerDidFinishPlaying_successfully_, 1
        )

        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.enableRate)
        self.assertArgIsBOOL(AVFoundation.AVAudioPlayer.setEnableRate_, 0)

        self.assertArgIsOut(
            AVFoundation.AVAudioPlayer.initWithContentsOfURL_fileTypeHint_error_, 2
        )
        self.assertArgIsOut(
            AVFoundation.AVAudioPlayer.initWithData_fileTypeHint_error_, 2
        )

    @min_sdk_level("10.13")
    def test_protocols(self):
        self.assertProtocolExists("AVAudioPlayerDelegate", AVFoundation)
