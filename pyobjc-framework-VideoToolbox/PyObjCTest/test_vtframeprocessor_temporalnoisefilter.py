import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTFrameProcessor_TemporalNoiseFilter(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            VideoToolbox.VTTemporalNoiseFilterConfiguration.isSupported
        )
        self.assertResultIsBOOL(
            VideoToolbox.VTTemporalNoiseFilterParameters.hasDiscontinuity
        )
        self.assertArgIsBOOL(
            VideoToolbox.VTTemporalNoiseFilterParameters.setHasDiscontinuity_, 0
        )
