import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptionFormatConformer(TestCase):
    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptionFormatConformer.conformsCaptionTimeRange
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptionFormatConformer.setConformsCaptionTimeRange_, 0
        )

        self.assertArgIsOut(
            AVFoundation.AVCaptionFormatConformer.conformedCaptionForCaption_error_, 1
        )
