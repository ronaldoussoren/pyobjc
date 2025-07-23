import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureOutputBase(TestCase):
    def test_enum(self):
        self.assertIsEnumType(AVFoundation.AVCaptureOutputDataDroppedReason)
        self.assertEqual(AVFoundation.AVCaptureOutputDataDroppedReasonNone, 0)
        self.assertEqual(AVFoundation.AVCaptureOutputDataDroppedReasonLateData, 1)
        self.assertEqual(AVFoundation.AVCaptureOutputDataDroppedReasonOutOfBuffers, 2)
        self.assertEqual(AVFoundation.AVCaptureOutputDataDroppedReasonDiscontinuity, 3)

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureOutput.isDeferredStartSupported)
        self.assertResultIsBOOL(AVFoundation.AVCaptureOutput.isDeferredStartEnabled)
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureOutput.setDeferredStartEnabled_,
            0,  # noqa: B950
        )
