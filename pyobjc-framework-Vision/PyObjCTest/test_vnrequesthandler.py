from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNRequestHandler(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Vision.VNImageOption, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Vision.VNImageOptionProperties, str)
        self.assertIsInstance(Vision.VNImageOptionCameraIntrinsics, str)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(Vision.VNImageRequestHandler.performRequests_error_)
        self.assertArgIsOut(Vision.VNImageRequestHandler.performRequests_error_, 1)

        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onCVPixelBuffer_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onCVPixelBuffer_error_, 2
        )
        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onCVPixelBuffer_orientation_error_  # noqa: B950
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onCVPixelBuffer_orientation_error_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onCGImage_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onCGImage_error_, 2
        )
        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onCGImage_orientation_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onCGImage_orientation_error_,
            3,
        )

        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onCIImage_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onCIImage_error_, 2
        )
        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onCIImage_orientation_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onCIImage_orientation_error_,
            3,
        )

        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onImageURL_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onImageURL_error_, 2
        )
        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onImageURL_orientation_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onImageURL_orientation_error_,
            3,
        )

        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onImageData_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onImageData_error_, 2
        )
        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onImageData_orientation_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onImageData_orientation_error_,
            3,
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onCMSampleBuffer_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onCMSampleBuffer_error_, 2
        )

        self.assertResultIsBOOL(
            Vision.VNSequenceRequestHandler.performRequests_onCMSampleBuffer_orientation_error_
        )
        self.assertArgIsOut(
            Vision.VNSequenceRequestHandler.performRequests_onCMSampleBuffer_orientation_error_,
            3,
        )
