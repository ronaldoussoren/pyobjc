import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetImageGenerator(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AVFoundation.AVAssetImageGeneratorApertureMode, str)

    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAssetImageGeneratorResult)

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
            b"v{CMTime=qiIq}^{CGImage=}{CMTime=qiIq}" + objc._C_NSInteger
        )

        self.assertArgIsBlock(
            AVFoundation.AVAssetImageGenerator.generateCGImagesAsynchronouslyForTimes_completionHandler_,  # noqa: B950
            1,
            AVAssetImageGeneratorCompletionHandler,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVAssetImageGenerator.generateCGImageAsynchronouslyForTime_completionHandler_,  # noqa: B950
            1,
            b"v^{CGImage=}" + AVFoundation.CMTime.__typestr__ + b"@",
        )
