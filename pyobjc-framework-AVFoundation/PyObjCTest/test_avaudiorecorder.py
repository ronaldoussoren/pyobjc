import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioRecorderHelper(AVFoundation.NSObject):
    def audioRecorderDidFinishRecording_successfully_(self, a, b):
        pass


class TestAVAudioRecorder(TestCase):
    def test_methods(self):
        self.assertArgIsOut(AVFoundation.AVAudioRecorder.initWithURL_settings_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.prepareToRecord)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.record)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.recordForDuration_)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.deleteRecording)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.isRecording)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.isMeteringEnabled)
        self.assertArgIsBOOL(AVFoundation.AVAudioRecorder.setMeteringEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.recordAtTime_)

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertArgIsOut(AVFoundation.AVAudioRecorder.initWithURL_format_error_, 2)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAudioInputNode.setMutedSpeechActivityEventListener_
        )
        self.assertArgIsBlock(
            AVFoundation.AVAudioInputNode.setMutedSpeechActivityEventListener_, 0, b"vq"
        )

        self.assertArgIsOut(AVFoundation.AVAudioRecorder.initWithURL_format_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.prepareToRecord)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.record)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.recordAtTime_)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.recordForDuration_)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.recordAtTime_forDuration_)
        self.assertResultIsBOOL(AVFoundation.AVAudioRecorder.deleteRecording)

    def test_protocols(self):
        self.assertProtocolExists("AVAudioRecorderDelegate", AVFoundation)

    def test_protocol_methods(self):
        self.assertArgIsBOOL(
            TestAVAudioRecorderHelper.audioRecorderDidFinishRecording_successfully_, 1
        )
