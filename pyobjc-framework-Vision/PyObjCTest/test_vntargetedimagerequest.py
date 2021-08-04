from PyObjCTools.TestSupport import TestCase, min_os_level, os_level_between
import Vision


class TestVNTargetedImageRequest(TestCase):
    @os_level_between("10.13", "11.5")
    def testMethods10_13_missing_12_0(self):
        # XXX: Needs further research!
        #      Also add "expectedFailure" instead of disabling the test
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCVPixelBuffer_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCGImage_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCIImage_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedImageURL_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedImageData_completionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCIImage_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCIImage_orientation_options_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedImageURL_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedImageURL_orientation_options_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedImageData_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedImageData_orientation_options_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCVPixelBuffer_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCVPixelBuffer_orientation_options_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCGImage_options_completionHandler_,  # noqa: B950
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCGImage_orientation_options_completionHandler_,  # noqa: B950
            3,
            b"v@@",
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCMSampleBuffer_options_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBlock(
            Vision.VNTargetedImageRequest.initWithTargetedCMSampleBuffer_orientation_options_completionHandler_,
            3,
            b"v@@",
        )
