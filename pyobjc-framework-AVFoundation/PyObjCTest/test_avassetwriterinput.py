import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetWriterInput(TestCase):
    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInputCaptionAdaptor.appendCaption_
        )
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInputCaptionAdaptor.appendCaptionGroup_
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInput.performsMultiPassEncodingIfSupported
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetWriterInput.setPerformsMultiPassEncodingIfSupported_, 0
        )
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInput.canPerformMultiplePasses
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetWriterInput.respondToEachPassDescriptionOnQueue_usingBlock_,  # noqa: B950
            1,
            b"v",
        )
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInputMetadataAdaptor.appendTimedMetadataGroup_
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInput.marksOutputTrackAsEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetWriterInput.setMarksOutputTrackAsEnabled_, 0
        )
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInput.canAddTrackAssociationWithTrackOfInput_type_
        )

    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.isReadyForMoreMediaData)
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInput.expectsMediaDataInRealTime
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetWriterInput.setExpectsMediaDataInRealTime_, 0
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetWriterInput.requestMediaDataWhenReadyOnQueue_usingBlock_,  # noqa: B950
            1,
            b"v",
        )
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.appendSampleBuffer_)
        self.assertResultIsBOOL(
            AVFoundation.AVAssetWriterInputPixelBufferAdaptor.appendPixelBuffer_withPresentationTime_  # noqa: B950
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(
            AVFoundation.AVAssetWriterInputMediaDataLocationInterleavedWithMainMediaData,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVAssetWriterInputMediaDataLocationBeforeMainMediaDataNotInterleaved,  # noqa: B950
            str,
        )
