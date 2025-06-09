import SoundAnalysis
import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSNClassifySoundRequest(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            SoundAnalysis.SNClassifySoundRequest.initWithMLModel_error_, 1
        )
        self.assertResultHasType(
            SoundAnalysis.SNClassifySoundRequest.windowDuration,
            CoreMedia.CMTime.__typestr__,
        )
        self.assertArgHasType(
            SoundAnalysis.SNClassifySoundRequest.setWindowDuration_,
            0,
            CoreMedia.CMTime.__typestr__,
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsOut(
            SoundAnalysis.SNClassifySoundRequest.initWithClassifierIdentifier_error_, 1
        )
