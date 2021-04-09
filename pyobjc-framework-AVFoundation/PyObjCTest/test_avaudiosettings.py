import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioSettings(TestCase):
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioQualityMin, 0)
        self.assertEqual(AVFoundation.AVAudioQualityLow, 0x20)
        self.assertEqual(AVFoundation.AVAudioQualityMedium, 0x40)
        self.assertEqual(AVFoundation.AVAudioQualityHigh, 0x60)
        self.assertEqual(AVFoundation.AVAudioQualityMax, 0x7F)

        self.assertIsInstance(AVFoundation.AVSampleRateKey, str)
        self.assertIsInstance(AVFoundation.AVNumberOfChannelsKey, str)
        self.assertIsInstance(AVFoundation.AVLinearPCMBitDepthKey, str)
        self.assertIsInstance(AVFoundation.AVLinearPCMIsBigEndianKey, str)
        self.assertIsInstance(AVFoundation.AVLinearPCMIsFloatKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderAudioQualityKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderBitRateKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderBitDepthHintKey, str)
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAudioQualityKey, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AVFoundation.AVLinearPCMIsNonInterleaved, str)
        self.assertIs(
            AVFoundation.AVLinearPCMIsNonInterleavedKey,
            AVFoundation.AVLinearPCMIsNonInterleaved,
        )
        self.assertIsInstance(AVFoundation.AVEncoderBitRatePerChannelKey, str)
        self.assertIsInstance(AVFoundation.AVChannelLayoutKey, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVEncoderAudioQualityForVBRKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderBitRateStrategyKey, str)
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAlgorithmKey, str)
        self.assertIsInstance(AVFoundation.AVAudioBitRateStrategy_Constant, str)
        self.assertIsInstance(AVFoundation.AVAudioBitRateStrategy_LongTermAverage, str)
        self.assertIsInstance(
            AVFoundation.AVAudioBitRateStrategy_VariableConstrained, str
        )
        self.assertIsInstance(AVFoundation.AVAudioBitRateStrategy_Variable, str)
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAlgorithm_Normal, str)
        self.assertIsInstance(
            AVFoundation.AVSampleRateConverterAlgorithm_Mastering, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(
            AVFoundation.AVSampleRateConverterAlgorithm_MinimumPhase, str
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVAudioFileTypeKey, str)
