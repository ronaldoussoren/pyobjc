import SoundAnalysis
import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSNAnalyzer(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultHasType(
            SoundAnalysis.SNClassificationResult.timeRange,
            CoreMedia.CMTimeRange.__typestr__,
        )
