import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetTrackSegment(TestCase):
    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrackSegment.isEmpty)
