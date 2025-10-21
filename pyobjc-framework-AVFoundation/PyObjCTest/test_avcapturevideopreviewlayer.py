import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureVideoPreviewLayer(TestCase):
    def testClasses(self):
        AVFoundation.AVCaptureVideoPreviewLayer

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoPreviewLayer.isDeferredStartEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoPreviewLayer.setDeferredStartEnabled_, 0
        )
