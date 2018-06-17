from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVMediaFormat (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVMediaTypeVideo, unicode)
        self.assertIsInstance(AVFoundation.AVMediaTypeAudio, unicode)
        self.assertIsInstance(AVFoundation.AVMediaTypeText, unicode)
        self.assertIsInstance(AVFoundation.AVMediaTypeClosedCaption, unicode)
        self.assertIsInstance(AVFoundation.AVMediaTypeSubtitle, unicode)
        self.assertIsInstance(AVFoundation.AVMediaTypeTimecode, unicode)
        self.assertIsInstance(AVFoundation.AVMediaTypeMuxed, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicVisual, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicAudible, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicLegible, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicFrameBased, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeQuickTimeMovie, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeMPEG4, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeAppleM4V, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeAppleM4A, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeCoreAudioFormat, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeWAVE, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeAIFF, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeAIFC, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeAMR, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(AVFoundation.AVMediaTypeMetadata, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicIsMainProgramContent, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicIsAuxiliaryContent, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicContainsOnlyForcedSubtitles, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicTranscribesSpokenDialogForAccessibility, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicDescribesMusicAndSoundForAccessibility, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicEasyToRead, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicDescribesVideoForAccessibility, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVFileTypeMPEGLayer3, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeSunAU, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeAC3, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicLanguageTranslation, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicDubbedTranslation, unicode)
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicVoiceOverTranslation, unicode)
        self.assertIsInstance(AVFoundation.AVFileType3GPP, unicode)
        self.assertIsInstance(AVFoundation.AVFileType3GPP2, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeEnhancedAC3, unicode)
        self.assertIsInstance(AVFoundation.AVStreamingKeyDeliveryContentKeyType, unicode)
        self.assertIsInstance(AVFoundation.AVStreamingKeyDeliveryPersistentContentKeyType, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(AVFoundation.AVMediaCharacteristicUsesWideGamutColorSpace, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVMediaTypeDepthData, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeJPEG, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeDNG, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeHEIC, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeAVCI, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeHEIF, unicode)
        self.assertIsInstance(AVFoundation.AVFileTypeTIFF, unicode)

if __name__ == "__main__":
    main()
