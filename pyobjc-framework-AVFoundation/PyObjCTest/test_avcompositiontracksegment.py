import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCompositionTrackSegment(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertResultIsBOOL(AVFoundation.AVCompositionTrackSegment.isEmpty)
