import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCompositionTrackSegment(TestCase):
    @min_os_level("10.7")
    def test_constants(self):
        self.assertResultIsBOOL(AVFoundation.AVCompositionTrackSegment.isEmpty)
