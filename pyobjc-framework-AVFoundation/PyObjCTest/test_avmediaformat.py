import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVMediaFormat(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVFileTypeProfile, str)
        self.assertIsTypedEnum(AVFoundation.AVVideoRange, str)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVMediaTypeVideo, str)
        self.assertIsInstance(AVFoundation.AVMediaTypeAudio, str)
        self.assertIsInstance(AVFoundation.AVMediaTypeText, str)
        self.assertIsInstance(AVFoundation.AVMediaTypeClosedCaption, str)
        self.assertIsInstance(AVFoundation.AVMediaTypeSubtitle, str)
        self.assertIsInstance(AVFoundation.AVMediaTypeTimecode, str)
        self.assertIsInstance(AVFoundation.AVMediaTypeMuxed, str)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicVisual, str)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicAudible, str)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicLegible, str)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicFrameBased, str)
        self.assertIsInstance(AVFoundation.AVFileTypeQuickTimeMovie, str)
        self.assertIsInstance(AVFoundation.AVFileTypeMPEG4, str)
        self.assertIsInstance(AVFoundation.AVFileTypeAppleM4V, str)
        self.assertIsInstance(AVFoundation.AVFileTypeAppleM4A, str)
        self.assertIsInstance(AVFoundation.AVFileTypeCoreAudioFormat, str)
        self.assertIsInstance(AVFoundation.AVFileTypeWAVE, str)
        self.assertIsInstance(AVFoundation.AVFileTypeAIFF, str)
        self.assertIsInstance(AVFoundation.AVFileTypeAIFC, str)
        self.assertIsInstance(AVFoundation.AVFileTypeAMR, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(AVFoundation.AVMediaTypeMetadata, str)
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicIsMainProgramContent, str
        )
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicIsAuxiliaryContent, str)
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicContainsOnlyForcedSubtitles, str
        )
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicTranscribesSpokenDialogForAccessibility,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicDescribesMusicAndSoundForAccessibility,
            str,
        )
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicEasyToRead, str)
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicDescribesVideoForAccessibility, str
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVFileTypeMPEGLayer3, str)
        self.assertIsInstance(AVFoundation.AVFileTypeSunAU, str)
        self.assertIsInstance(AVFoundation.AVFileTypeAC3, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicLanguageTranslation, str
        )
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicDubbedTranslation, str)
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicVoiceOverTranslation, str
        )
        self.assertIsInstance(AVFoundation.AVFileType3GPP, str)
        self.assertIsInstance(AVFoundation.AVFileType3GPP2, str)
        self.assertIsInstance(AVFoundation.AVFileTypeEnhancedAC3, str)
        self.assertIsInstance(AVFoundation.AVStreamingKeyDeliveryContentKeyType, str)
        self.assertIsInstance(
            AVFoundation.AVStreamingKeyDeliveryPersistentContentKeyType, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicUsesWideGamutColorSpace, str
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVMediaTypeDepthData, str)
        self.assertIsInstance(AVFoundation.AVFileTypeJPEG, str)
        self.assertIsInstance(AVFoundation.AVFileTypeDNG, str)
        self.assertIsInstance(AVFoundation.AVFileTypeHEIC, str)
        self.assertIsInstance(AVFoundation.AVFileTypeAVCI, str)
        self.assertIsInstance(AVFoundation.AVFileTypeHEIF, str)
        self.assertIsInstance(AVFoundation.AVFileTypeTIFF, str)

    # @min_os_level("10.14") # Not actually present on 10.14...
    @min_os_level("10.15")
    def testConstants10_14(self):
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicIsOriginalContent, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVMediaCharacteristicContainsAlphaChannel, str
        )

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicContainsHDRVideo, str)
        self.assertIsInstance(AVFoundation.AVFileTypeProfileMPEG4AppleHLS, str)
        self.assertIsInstance(AVFoundation.AVFileTypeProfileMPEG4CMAFCompliant, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(AVFoundation.AVFileTypeAppleiTT, str)
        self.assertIsInstance(AVFoundation.AVFileTypeSCC, str)
