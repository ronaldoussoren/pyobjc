import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTFrameProcessor_LowLatencyFrameInterpolation(TestCase):
    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertResultIsBOOL(
            VideoToolbox.VTLowLatencyFrameInterpolationConfiguration.isSupported
        )
        self.assertArgIsBOOL(
            VideoToolbox.VTLowLatencyFrameInterpolationConfiguration.setSupported_, 0
        )
