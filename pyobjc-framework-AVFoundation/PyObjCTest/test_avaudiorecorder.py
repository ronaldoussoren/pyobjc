from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioRecorderHelper (AVFoundation.NSObject):
    def audioRecorderDidFinishRecording_successfully_(self, a, b): pass

class TestAVAudioRecorder (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVAudioRecorder.initWithURL_settings_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.prepareToRecord)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.record)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.recordForDuration_)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.deleteRecording)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.isRecording)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.isMeteringEnabled)
        self.assertArgIsBOOL(AVFoundation.AVAudioRecorder.setMeteringEnabled_, 0)

        self.assertArgIsBOOL(TestAVAudioRecorderHelper.audioRecorderDidFinishRecording_successfully_, 1)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.recordAtTime_)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertArgIsOut(AVFoundation.AVAudioRecorder.initWithURL_format_error_, 2)

    def testProtocols(self):
        objc.protocolNamed('AVAudioRecorderDelegate')


if __name__ == "__main__":
    main()
