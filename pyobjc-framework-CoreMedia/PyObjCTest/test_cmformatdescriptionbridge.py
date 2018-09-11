from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMFormatDescriptionBridge (TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMFormatDescriptionBridgeError_InvalidParameter, -12712)
        self.assertEqual(CoreMedia.kCMFormatDescriptionBridgeError_AllocationFailed, -12713)
        self.assertEqual(CoreMedia.kCMFormatDescriptionBridgeError_InvalidSerializedSampleDescription, -12714)
        self.assertEqual(CoreMedia.kCMFormatDescriptionBridgeError_InvalidFormatDescription, -12715)
        self.assertEqual(CoreMedia.kCMFormatDescriptionBridgeError_IncompatibleFormatDescription, -12716)
        self.assertEqual(CoreMedia.kCMFormatDescriptionBridgeError_UnsupportedSampleDescriptionFlavor, -12717)
        self.assertEqual(CoreMedia.kCMFormatDescriptionBridgeError_InvalidSlice, -12719)

    @min_os_level('10.10')
    def test_constants10_10(self):
        self.assertIsInstance(CoreMedia.kCMImageDescriptionFlavor_QuickTimeMovie, unicode)
        self.assertIsInstance(CoreMedia.kCMImageDescriptionFlavor_ISOFamily, unicode)
        self.assertIsInstance(CoreMedia.kCMImageDescriptionFlavor_3GPFamily, unicode)

        self.assertIsInstance(CoreMedia.kCMSoundDescriptionFlavor_QuickTimeMovie, unicode)
        self.assertIsInstance(CoreMedia.kCMSoundDescriptionFlavor_QuickTimeMovieV2, unicode)
        self.assertIsInstance(CoreMedia.kCMSoundDescriptionFlavor_ISOFamily, unicode)
        self.assertIsInstance(CoreMedia.kCMSoundDescriptionFlavor_3GPFamily, unicode)

    @min_os_level('10.10')
    def test_functions10_10(self):
        self.assertArgIsIn(CoreMedia.CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData, 1)
        self.assertArgSizeInArg(CoreMedia.CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData, 1, 2)
        self.assertArgIsOut(CoreMedia.CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData, 5)
        self.assertArgIsCFRetained(CoreMedia.CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionData, 5)

        self.assertArgIsOut(CoreMedia.CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer, 4)
        self.assertArgIsCFRetained(CoreMedia.CMVideoFormatDescriptionCreateFromBigEndianImageDescriptionBlockBuffer, 4)

        self.assertArgIsOut(CoreMedia.CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer, 4)
        self.assertArgIsCFRetained(CoreMedia.CMVideoFormatDescriptionCopyAsBigEndianImageDescriptionBlockBuffer, 4)

        self.assertArgIsInOut(CoreMedia.CMSwapBigEndianImageDescriptionToHost, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapBigEndianImageDescriptionToHost, 0, 1)

        self.assertArgIsInOut(CoreMedia.CMSwapHostEndianImageDescriptionToBig, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapHostEndianImageDescriptionToBig, 0, 1)

        self.assertArgIsIn(CoreMedia.CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData, 1)
        self.assertArgSizeInArg(CoreMedia.CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData, 1, 2)
        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData, 4)
        self.assertArgIsCFRetained(CoreMedia.CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionData, 4)

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMAudioFormatDescriptionCreateFromBigEndianSoundDescriptionBlockBuffer, 3)

        self.assertArgIsOut(CoreMedia.CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMAudioFormatDescriptionCopyAsBigEndianSoundDescriptionBlockBuffer, 3)

        self.assertResultIsBOOL(CoreMedia.CMDoesBigEndianSoundDescriptionRequireLegacyCBRSampleTableLayout)

        self.assertArgIsInOut(CoreMedia.CMSwapBigEndianSoundDescriptionToHost, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapBigEndianSoundDescriptionToHost, 0, 1)

        self.assertArgIsInOut(CoreMedia.CMSwapHostEndianSoundDescriptionToBig, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapHostEndianSoundDescriptionToBig, 0, 1)

        self.assertArgIsIn(CoreMedia.CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData, 1)
        self.assertArgSizeInArg(CoreMedia.CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData, 1, 2)
        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData, 5)
        self.assertArgIsCFRetained(CoreMedia.CMTextFormatDescriptionCreateFromBigEndianTextDescriptionData, 5)

        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer, 4)
        self.assertArgIsCFRetained(CoreMedia.CMTextFormatDescriptionCreateFromBigEndianTextDescriptionBlockBuffer, 4)

        self.assertArgIsOut(CoreMedia.CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMTextFormatDescriptionCopyAsBigEndianTextDescriptionBlockBuffer, 3)

        self.assertArgIsInOut(CoreMedia.CMSwapBigEndianTextDescriptionToHost, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapBigEndianTextDescriptionToHost, 0, 1)

        self.assertArgIsInOut(CoreMedia.CMSwapHostEndianTextDescriptionToBig, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapHostEndianTextDescriptionToBig, 0, 1)

        self.assertArgIsIn(CoreMedia.CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData, 1)
        self.assertArgSizeInArg(CoreMedia.CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData, 1, 2)
        self.assertArgIsOut(CoreMedia.CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData, 4)
        self.assertArgIsCFRetained(CoreMedia.CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionData, 4)

        self.assertArgIsOut(CoreMedia.CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMClosedCaptionFormatDescriptionCreateFromBigEndianClosedCaptionDescriptionBlockBuffer, 3)

        self.assertArgIsOut(CoreMedia.CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMClosedCaptionFormatDescriptionCopyAsBigEndianClosedCaptionDescriptionBlockBuffer, 3)

        self.assertArgIsInOut(CoreMedia.CMSwapBigEndianClosedCaptionDescriptionToHost, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapBigEndianClosedCaptionDescriptionToHost, 0, 1)

        self.assertArgIsInOut(CoreMedia.CMSwapHostEndianClosedCaptionDescriptionToBig, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapHostEndianClosedCaptionDescriptionToBig, 0, 1)

        self.assertArgIsIn(CoreMedia.CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData, 1)
        self.assertArgSizeInArg(CoreMedia.CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData, 1, 2)
        self.assertArgIsOut(CoreMedia.CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData, 4)
        self.assertArgIsCFRetained(CoreMedia.CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionData, 4)

        self.assertArgIsOut(CoreMedia.CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMTimeCodeFormatDescriptionCreateFromBigEndianTimeCodeDescriptionBlockBuffer, 3)

        self.assertArgIsOut(CoreMedia.CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMTimeCodeFormatDescriptionCopyAsBigEndianTimeCodeDescriptionBlockBuffer, 3)

        self.assertArgIsInOut(CoreMedia.CMSwapBigEndianTimeCodeDescriptionToHost, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapBigEndianTimeCodeDescriptionToHost, 0, 1)

        self.assertArgIsInOut(CoreMedia.CMSwapHostEndianTimeCodeDescriptionToBig, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapHostEndianTimeCodeDescriptionToBig, 0, 1)

        self.assertArgIsIn(CoreMedia.CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData, 1)
        self.assertArgSizeInArg(CoreMedia.CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData, 1, 2)
        self.assertArgIsOut(CoreMedia.CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData, 4)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionData, 4)

        self.assertArgIsOut(CoreMedia.CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataFormatDescriptionCreateFromBigEndianMetadataDescriptionBlockBuffer, 3)

        self.assertArgIsOut(CoreMedia.CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer, 3)
        self.assertArgIsCFRetained(CoreMedia.CMMetadataFormatDescriptionCopyAsBigEndianMetadataDescriptionBlockBuffer, 3)

        self.assertArgIsInOut(CoreMedia.CMSwapBigEndianMetadataDescriptionToHost, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapBigEndianMetadataDescriptionToHost, 0, 1)

        self.assertArgIsInOut(CoreMedia.CMSwapHostEndianMetadataDescriptionToBig, 0)
        self.assertArgSizeInArg(CoreMedia.CMSwapHostEndianMetadataDescriptionToBig, 0, 1)


if __name__ == "__main__":
    main()
