import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioSetting(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVFormatIDKey, str)
        self.assertIsInstance(AVFoundation.AVSampleRateKey, str)
        self.assertIsInstance(AVFoundation.AVNumberOfChannelsKey, str)

        self.assertIsInstance(AVFoundation.AVLinearPCMBitDepthKey, str)
        self.assertIsInstance(AVFoundation.AVLinearPCMIsBigEndianKey, str)
        self.assertIsInstance(AVFoundation.AVLinearPCMIsFloatKey, str)

        self.assertIsInstance(AVFoundation.AVLinearPCMIsNonInterleaved, str)
        self.assertTrue(
            AVFoundation.AVLinearPCMIsNonInterleavedKey
            is AVFoundation.AVLinearPCMIsNonInterleaved
        )

        self.assertIsInstance(AVFoundation.AVEncoderAudioQualityKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderAudioQualityForVBRKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderBitRateKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderBitRatePerChannelKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderBitDepthHintKey, str)
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAudioQualityKey, str)
        self.assertIsInstance(AVFoundation.AVChannelLayoutKey, str)

        self.assertEqual(AVFoundation.AVAudioQualityMin, 0)
        self.assertEqual(AVFoundation.AVAudioQualityLow, 0x20)
        self.assertEqual(AVFoundation.AVAudioQualityMedium, 0x40)
        self.assertEqual(AVFoundation.AVAudioQualityHigh, 0x60)

    @min_os_level("10.9")
    def testConstants10_9(self):
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
