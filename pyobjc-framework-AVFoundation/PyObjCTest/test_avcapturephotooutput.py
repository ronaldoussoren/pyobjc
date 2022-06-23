import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCapturePhotoOutput(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoSettings.isHighResolutionPhotoEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCapturePhotoSettings.setHighResolutionPhotoEnabled_, 0
        )
