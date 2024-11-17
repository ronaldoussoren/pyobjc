import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureIndexPicker(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureIndexPicker.initWithLocalizedTitle_symbolName_numberOfIndexes_localizedTitleTransform_,
            3,
            b"@q",
        )

        self.assertArgIsBlock(
            AVFoundation.AVCaptureIndexPicker.setActionQueue_action_, 1, b"vq"
        )
