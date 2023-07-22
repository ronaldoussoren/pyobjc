import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetVariant(TestCase):
    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetVariantAudioRenditionSpecificAttributes.isBinaural
        )
        self.assertResultIsBOOL(
            AVFoundation.AVAssetVariantAudioRenditionSpecificAttributes.isImmersive
        )
        self.assertResultIsBOOL(
            AVFoundation.AVAssetVariantAudioRenditionSpecificAttributes.isDownmix
        )

        self.assertArgIsBOOL(
            AVFoundation.AVAssetVariantQualifier.predicateForBinauralAudio_mediaSelectionOption_,
            0,
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetVariantQualifier.predicateForImmersiveAudio_mediaSelectionOption_,
            0,
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetVariantQualifier.predicateForDownmixAudio_mediaSelectionOption_,
            0,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInputTaggedPixelBufferGroupAdaptor.appendTaggedPixelBufferGroup_withPresentationTime_
        )
