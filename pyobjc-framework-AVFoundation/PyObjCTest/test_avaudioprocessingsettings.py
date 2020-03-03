import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioProcessingSettings(TestCase):
    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmTimeDomain, str)
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmSpectral, str)
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmVarispeed, str)
