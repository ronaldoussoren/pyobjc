import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptionRenderer(TestCase):
    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptionRendererScene.hasActiveCaptions)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptionRendererScene.needsPeriodicRefresh
        )
