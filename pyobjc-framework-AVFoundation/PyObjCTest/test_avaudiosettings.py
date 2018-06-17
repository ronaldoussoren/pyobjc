from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAudioSettings (TestCase):

    def testConstants(self):
        self.assertEqual(AVFoundation.AVAudioQualityMin, 0)
        self.assertEqual(AVFoundation.AVAudioQualityLow, 0x20)
        self.assertEqual(AVFoundation.AVAudioQualityMedium, 0x40)
        self.assertEqual(AVFoundation.AVAudioQualityHigh, 0x60)
        self.assertEqual(AVFoundation.AVAudioQualityMax, 0x7F)

        self.assertIsInstance(AVFoundation.AVSampleRateKey, unicode)
        self.assertIsInstance(AVFoundation.AVNumberOfChannelsKey, unicode)
        self.assertIsInstance(AVFoundation.AVLinearPCMBitDepthKey, unicode)
        self.assertIsInstance(AVFoundation.AVLinearPCMIsBigEndianKey, unicode)
        self.assertIsInstance(AVFoundation.AVLinearPCMIsFloatKey, unicode)
        self.assertIsInstance(AVFoundation.AVEncoderAudioQualityKey, unicode)
        self.assertIsInstance(AVFoundation.AVEncoderBitRateKey, unicode)
        self.assertIsInstance(AVFoundation.AVEncoderBitDepthHintKey, unicode)
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAudioQualityKey, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(AVFoundation.AVLinearPCMIsNonInterleaved, unicode)
        self.assertIs(AVFoundation.AVLinearPCMIsNonInterleavedKey, AVFoundation.AVLinearPCMIsNonInterleaved)
        self.assertIsInstance(AVFoundation.AVEncoderBitRatePerChannelKey, unicode)
        self.assertIsInstance(AVFoundation.AVChannelLayoutKey, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVEncoderAudioQualityForVBRKey, unicode)
        self.assertIsInstance(AVFoundation.AVEncoderBitRateStrategyKey, unicode)
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAlgorithmKey, unicode)
        self.assertIsInstance(AVFoundation.AVAudioBitRateStrategy_Constant, unicode)
        self.assertIsInstance(AVFoundation.AVAudioBitRateStrategy_LongTermAverage, unicode)
        self.assertIsInstance(AVFoundation.AVAudioBitRateStrategy_VariableConstrained, unicode)
        self.assertIsInstance(AVFoundation.AVAudioBitRateStrategy_Variable, unicode)
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAlgorithm_Normal, unicode)
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAlgorithm_Mastering, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(AVFoundation.AVSampleRateConverterAlgorithm_MinimumPhase, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVAudioFileTypeKey, unicode)


if __name__ == "__main__":
    main()
