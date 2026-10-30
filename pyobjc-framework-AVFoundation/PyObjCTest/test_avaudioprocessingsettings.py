import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVAudioProcessingSettings(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AVFoundation.AVAudioSpatializationFormats)
        self.assertEqual(AVFoundation.AVAudioSpatializationFormatNone, 0)
        self.assertEqual(AVFoundation.AVAudioSpatializationFormatMonoAndStereo, 0x3)
        self.assertEqual(AVFoundation.AVAudioSpatializationFormatMultichannel, 0x4)
        self.assertEqual(
            AVFoundation.AVAudioSpatializationFormatMonoStereoAndMultichannel, 0x7
        )

    def test_typed_enums(self):
        self.assertIsTypedEnum(AVFoundation.AVAudioTimePitchAlgorithm, str)

    def test_constants(self):
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmTimeDomain, str)
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmSpectral, str)
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmVarispeed, str)
