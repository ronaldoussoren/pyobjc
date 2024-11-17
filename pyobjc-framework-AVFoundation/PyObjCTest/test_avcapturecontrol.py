import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAnimation(TestCase):
    @min_os_level("15.2")
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureControl.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureControl.setEnabled_, 0)
