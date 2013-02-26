from PyObjCTools.TestSupport import *

import AVFoundation
import obj

try:
    unicode
except NameError:
    unicode = str

AVAssetImageGeneratorCompletionHandler = b'v{CMTime}^{CGImage}{CMTime}' + objc._C_NSInteger + b'@'

class TestAVAssetImageGenerator (TestCase):
    def test_constants(self):
        self.assertIsInstance(AVFoundation.AVAssetImageGeneratorApertureModeCleanAperture, unicode)
        self.assertIsInstance(AVFoundation.AVAssetImageGeneratorApertureModeProductionAperture, unicode)
        self.assertIsInstance(AVFoundation.AVAssetImageGeneratorApertureModeEncodedPixels, unicode)

        self.assertEqual(AVFoundation.AVAssetImageGeneratorSucceeded, 0)
        self.assertEqual(AVFoundation.AVAssetImageGeneratorFailed, 1)
        self.assertEqual(AVFoundation.AVAssetImageGeneratorCancelled, 2)

    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetImageGenerator.appliesPreferredTrackTransform)
        self.assertArgIsBOOL(AVFoundation.AVAssetImageGenerator.setAppliesPreferredTrackTransform_, 0)

        self.assertResultIsCFRetained(AVFoundation.AVAssetImageGenerator.copyCGImageAtTime_actualTime_error_)
        self.assertArgIsOut(AVFoundation.AVAssetImageGenerator.copyCGImageAtTime_actualTime_error_, 1)
        self.assertArgIsOut(AVFoundation.AVAssetImageGenerator.copyCGImageAtTime_actualTime_error_, 2)

        self.assertArgIsBlock(AVFoundation.AVAssertImageGenerator.generateCGImagesAsynchronouslyForTimes_completionHandler_,
                1, AVAssetImageGeneratorCompletionHandler)

if __name__ == "__main__":
    main()
