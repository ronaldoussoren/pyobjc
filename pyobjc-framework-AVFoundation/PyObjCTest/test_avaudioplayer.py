from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioPlayerHelper (AVFoundation.NSObject):
    def audioPlayerDidFinishPlaying_successfully_(self, a, b): pass

class TestAVAudioPlayer (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsOut(AVFoundation.AVAudioPlayer.initWithContentsOfURL_error_, 1)
        self.assertArgIsOut(AVFoundation.AVAudioPlayer.initWithData_error_, 1)

        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.prepareToPlay)
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.play)
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.playAtTime_)
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.isPlaying)

        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.isMeteringEnabled)
        self.assertArgIsBOOL(AVFoundation.AVAudioPlayer.setMeteringEnabled_, 0)

        self.assertArgIsBOOL(TestAVAudioPlayerHelper.audioPlayerDidFinishPlaying_successfully_, 1)

    @min_sdk_level('10.13')
    def testProtocols(self):
        objc.protocolNamed('AVAudioPlayerDelegate')

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioPlayer.enableRate)
        self.assertArgIsBOOL(AVFoundation.AVAudioPlayer.setEnableRate_, 0)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsOut(AVFoundation.AVAudioPlayer.initWithContentsOfURL_fileTypeHint_error_, 2)
        self.assertArgIsOut(AVFoundation.AVAudioPlayer.initWithData_fileTypeHint_error_, 2)

if __name__ == "__main__":
    main()
