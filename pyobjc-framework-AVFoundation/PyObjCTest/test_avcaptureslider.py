import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureSlider(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureSlider.setActionQueue_action_, 1, b"vf"
        )
