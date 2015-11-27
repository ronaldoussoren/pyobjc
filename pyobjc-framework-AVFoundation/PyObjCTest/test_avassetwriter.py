from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetWriter (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAssetWriterStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetWriterStatusWriting, 1)
        self.assertEqual(AVFoundation.AVAssetWriterStatusCompleted, 2)
        self.assertEqual(AVFoundation.AVAssetWriterStatusFailed, 3)
        self.assertEqual(AVFoundation.AVAssetWriterStatusCancelled, 4)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsBlock(AVFoundation.AVAssetWriter.finishWritingWithCompletionHandler_, 0, b'v')
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.canAddInputGroup_)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVAssetWriter.assetWriterWithURL_fileType_error_, 2)
        self.assertArgIsOut(AVFoundation.AVAssetWriter.initWithURL_fileType_error_, 2)

        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.shouldOptimizeForNetworkUse)
        self.assertArgIsBOOL(AVFoundation.AVAssetWriter.setShouldOptimizeForNetworkUse_, 0)

        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.canApplyOutputSettings_forMediaType_)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.canAddInput_)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.startWriting)
        self.assertResultIsBOOL(AVFoundation.AVAssetWriter.finishWriting)

if __name__ == "__main__":
    main()
