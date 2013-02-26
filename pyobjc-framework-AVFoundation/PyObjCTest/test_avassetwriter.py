from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetWriter (TestCase):
    def test_constants(self):
        self.assertEqual(AVFoundation.AVAssetWriterStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetWriterStatusWriting, 1)
        self.assertEqual(AVFoundation.AVAssetWriterStatusCompleted, 2)
        self.assertEqual(AVFoundation.AVAssetWriterStatusFailed, 3)
        self.assertEqual(AVFoundation.AVAssetWriterStatusCancelled, 4)


    def test_methods(self):
        self.assertArgIsOut(AVFoundation.AVAssetWriter.assetWriterWithURL_fileType_error_, 2)
        self.assertArgIsOut(AVFoundation.AVAssetWriter.initWithURL_fileType_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.shouldOptimizeForNetworkUse)
        self.assertArglsBOOL(AVFoundation.AVAssetWriter.setShouldOptimizeForNetworkUse_, 0)

        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.canApplyOutputSettings_forMediaType_)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.canAddInput_)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.startWriting)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.finishWriting)

if __name__ == "__main__":
    main()
