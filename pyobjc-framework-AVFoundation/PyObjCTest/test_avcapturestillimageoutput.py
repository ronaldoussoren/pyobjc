import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureStillImageOutput(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureStillImageOutput.captureStillImageAsynchronouslyFromConnection_completionHandler_,  # noqa: B950
            1,
            b"v^{opaqueCMSampleBuffer=}@",
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureStillImageOutput.isCapturingStillImage
        )
