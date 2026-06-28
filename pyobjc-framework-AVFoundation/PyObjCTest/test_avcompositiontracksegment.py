import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVCompositionTrackSegment(TestCase):
    def test_constants(self):
        self.assertResultIsBOOL(AVFoundation.AVCompositionTrackSegment.isEmpty)
