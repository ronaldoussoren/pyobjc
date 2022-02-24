import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioProcessingSettings(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVAudioTimePitchAlgorithm, str)

    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAudioSpatializationFormats)

    def test_constants(self):
        self.assertEqual(AVFoundation.AVAudioSpatializationFormatNone, 0)
        self.assertEqual(AVFoundation.AVAudioSpatializationFormatMonoAndStereo, 0x3)
        self.assertEqual(AVFoundation.AVAudioSpatializationFormatMultichannel, 0x4)
        self.assertEqual(
            AVFoundation.AVAudioSpatializationFormatMonoStereoAndMultichannel, 0x7
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmTimeDomain, str)
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmSpectral, str)
        self.assertIsInstance(AVFoundation.AVAudioTimePitchAlgorithmVarispeed, str)
