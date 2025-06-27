import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureSystemExposureBiasSlider(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureSystemExposureBiasSlider.initWithDevice_action_,
            1,
            b"vf",
        )
