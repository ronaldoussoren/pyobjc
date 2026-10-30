import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureStillImageOutput(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureStillImageOutput.captureStillImageAsynchronouslyFromConnection_completionHandler_,  # noqa: B950
            1,
            b"v^{opaqueCMSampleBuffer=}@",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureStillImageOutput.isCapturingStillImage
        )

    @min_os_level("12.0")
    def test_methods_tundra10_7(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureStillImageOutput_Tundra.captureStillImageAsynchronouslyFromConnection_completionHandler_,  # noqa: B950
            1,
            b"v^{opaqueCMSampleBuffer=}@",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureStillImageOutput_Tundra.isCapturingStillImage
        )
