import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioSettings(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AVFoundation.AVAudioQuality)
        self.assertEqual(AVFoundation.AVAudioQualityMin, 0)
        self.assertEqual(AVFoundation.AVAudioQualityLow, 0x20)
        self.assertEqual(AVFoundation.AVAudioQualityMedium, 0x40)
        self.assertEqual(AVFoundation.AVAudioQualityHigh, 0x60)
        self.assertEqual(AVFoundation.AVAudioQualityMax, 0x7F)

        self.assertIsEnumType(AVFoundation.AVAudioDynamicRangeControlConfiguration)
        self.assertEqual(AVFoundation.AVAudioDynamicRangeControlConfiguration_None, 0)
        self.assertEqual(AVFoundation.AVAudioDynamicRangeControlConfiguration_Music, 1)
        self.assertEqual(AVFoundation.AVAudioDynamicRangeControlConfiguration_Speech, 2)
        self.assertEqual(AVFoundation.AVAudioDynamicRangeControlConfiguration_Movie, 3)
        self.assertEqual(
            AVFoundation.AVAudioDynamicRangeControlConfiguration_Capture, 4
        )

        self.assertIsEnumType(AVFoundation.AVAudioContentSource)
        self.assertEqual(AVFoundation.AVAudioContentSource_Unspecified, -1)
        self.assertEqual(AVFoundation.AVAudioContentSource_Reserved, 0)
        self.assertEqual(AVFoundation.AVAudioContentSource_AppleCapture_Traditional, 1)
        self.assertEqual(AVFoundation.AVAudioContentSource_AppleCapture_Spatial, 2)
        self.assertEqual(
            AVFoundation.AVAudioContentSource_AppleCapture_Spatial_Enhanced, 3
        )
        self.assertEqual(AVFoundation.AVAudioContentSource_AppleMusic_Traditional, 4)
        self.assertEqual(AVFoundation.AVAudioContentSource_AppleMusic_Spatial, 5)
        self.assertEqual(
            AVFoundation.AVAudioContentSource_AppleAV_Traditional_Offline, 6
        )
        self.assertEqual(AVFoundation.AVAudioContentSource_AppleAV_Spatial_Offline, 7)
        self.assertEqual(AVFoundation.AVAudioContentSource_AppleAV_Traditional_Live, 8)
        self.assertEqual(AVFoundation.AVAudioContentSource_AppleAV_Spatial_Live, 9)
        self.assertEqual(AVFoundation.AVAudioContentSource_ApplePassthrough, 10)
        self.assertEqual(AVFoundation.AVAudioContentSource_Capture_Traditional, 33)
        self.assertEqual(AVFoundation.AVAudioContentSource_Capture_Spatial, 34)
        self.assertEqual(AVFoundation.AVAudioContentSource_Capture_Spatial_Enhanced, 35)
        self.assertEqual(AVFoundation.AVAudioContentSource_Music_Traditional, 36)
        self.assertEqual(AVFoundation.AVAudioContentSource_Music_Spatial, 37)
        self.assertEqual(AVFoundation.AVAudioContentSource_AV_Traditional_Offline, 38)
        self.assertEqual(AVFoundation.AVAudioContentSource_AV_Spatial_Offline, 39)
        self.assertEqual(AVFoundation.AVAudioContentSource_AV_Traditional_Live, 40)
        self.assertEqual(AVFoundation.AVAudioContentSource_AV_Spatial_Live, 41)
        self.assertEqual(AVFoundation.AVAudioContentSource_Passthrough, 42)

    def testConstants(self):
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

    @min_os_level("26.0")
    def testConstants26_0(self):
        self.assertIsInstance(
            AVFoundation.AVEncoderDynamicRangeControlConfigurationKey, str
        )
        self.assertIsInstance(AVFoundation.AVEncoderContentSourceKey, str)
        self.assertIsInstance(AVFoundation.AVEncoderASPFrequencyKey, str)
