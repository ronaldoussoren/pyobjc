import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetImageGenerator(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(
            AVFoundation.AVAssetImageGeneratorApertureModeCleanAperture, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetImageGeneratorApertureModeProductionAperture,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVAssetImageGeneratorApertureModeEncodedPixels, str
        )

        self.assertEqual(AVFoundation.AVAssetImageGeneratorSucceeded, 0)
        self.assertEqual(AVFoundation.AVAssetImageGeneratorFailed, 1)
        self.assertEqual(AVFoundation.AVAssetImageGeneratorCancelled, 2)

    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetImageGenerator.appliesPreferredTrackTransform
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetImageGenerator.setAppliesPreferredTrackTransform_,
            0,  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVAssetImageGenerator.copyCGImageAtTime_actualTime_error_,
            2,  # noqa: B950
        )

        AVAssetImageGeneratorCompletionHandler = (
            b"v{_CMTime=qiIq}^{__CGImage}{_CMTime=qiIq}" + objc._C_NSInteger
        )

        self.assertArgIsBlock(
            AVFoundation.AVAssetImageGenerator.generateCGImagesAsynchronouslyForTimes_completionHandler_,  # noqa: B950
            1,
            AVAssetImageGeneratorCompletionHandler,
        )
