import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureSpatialAudioMetadataSampleGenerator(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsCFRetained(
            AVFoundation.AVCaptureSpatialAudioMetadataSampleGenerator.newTimedMetadataSampleBufferAndResetAnalyzer
        )
