from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetWriterInput (TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.isReadyForMoreMediaData)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.expectsMediaDataInRealTime)
        self.assertArgIsBOOL(AVFoundation.AVAssetWriterInput.setExpectsMediaDataInRealTime_, 0)

        self.assertArgIsBlock(AVFoundation.AVAssetWriterInput.requestMediaDataWhenReadyOnQueue_usingBlock_, 1, b'v')
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.appendSampleBuffer_)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriterInput.appendPixelBuffer_withPresentationTime_)


if __name__ == "__main__":
    main()
