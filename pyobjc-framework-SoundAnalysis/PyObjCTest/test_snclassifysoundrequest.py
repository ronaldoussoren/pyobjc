import SoundAnalysis
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSNClassifySoundRequest(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            SoundAnalysis.SNClassifySoundRequest.initWithMLModel_error_, 1
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsOut(
            SoundAnalysis.SNClassifySoundRequest.initWithClassifierIdentifier_error_, 1
        )
