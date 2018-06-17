from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetWriterInput (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.performsMultiPassEncodingIfSupported)
        self.assertArgIsBOOL(AVFoundation.AVAssetWriterInput.setPerformsMultiPassEncodingIfSupported_, 0)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.canPerformMultiplePasses)
        self.assertArgIsBlock(AVFoundation.AVAssetWriterInput.respondToEachPassDescriptionOnQueue_usingBlock_, 1, b'v')
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInputMetadataAdaptor.appendTimedMetadataGroup_)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.marksOutputTrackAsEnabled)
        self.assertArgIsBOOL(AVFoundation.AVAssetWriterInput.setMarksOutputTrackAsEnabled_, 0)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.canAddTrackAssociationWithTrackOfInput_type_)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.isReadyForMoreMediaData)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.expectsMediaDataInRealTime)
        self.assertArgIsBOOL(AVFoundation.AVAssetWriterInput.setExpectsMediaDataInRealTime_, 0)
        self.assertArgIsBlock(AVFoundation.AVAssetWriterInput.requestMediaDataWhenReadyOnQueue_usingBlock_, 1, b'v')
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.appendSampleBuffer_)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInputPixelBufferAdaptor.appendPixelBuffer_withPresentationTime_)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVAssetWriterInputMediaDataLocationInterleavedWithMainMediaData, unicode)
        self.assertIsInstance(AVFoundation.AVAssetWriterInputMediaDataLocationBeforeMainMediaDataNotInterleaved, unicode)

if __name__ == "__main__":
    main()
