import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVAssetTrackSegment(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrackSegment.isEmpty)
