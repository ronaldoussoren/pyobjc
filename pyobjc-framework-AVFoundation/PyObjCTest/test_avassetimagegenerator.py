from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetImageGenerator (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVAssetImageGeneratorApertureModeCleanAperture, unicode)
        self.assertIsInstance(AVFoundation.AVAssetImageGeneratorApertureModeProductionAperture, unicode)
        self.assertIsInstance(AVFoundation.AVAssetImageGeneratorApertureModeEncodedPixels, unicode)

        self.assertEqual(AVFoundation.AVAssetImageGeneratorSucceeded, 0)
        self.assertEqual(AVFoundation.AVAssetImageGeneratorFailed, 1)
        self.assertEqual(AVFoundation.AVAssetImageGeneratorCancelled, 2)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetImageGenerator.appliesPreferredTrackTransform)
        self.assertArgIsBOOL(AVFoundation.AVAssetImageGenerator.setAppliesPreferredTrackTransform_, 0)
        self.assertArgIsOut(AVFoundation.AVAssetImageGenerator.copyCGImageAtTime_actualTime_error_, 2)

        AVAssetImageGeneratorCompletionHandler = b'v{_CMTime=qiIq}^{__CGImage}{_CMTime=qiIq}' + objc._C_NSInteger

        self.assertArgIsBlock(
            AVFoundation.AVAssetImageGenerator.generateCGImagesAsynchronouslyForTimes_completionHandler_,
            1,  AVAssetImageGeneratorCompletionHandler)

if __name__ == "__main__":
    main()
