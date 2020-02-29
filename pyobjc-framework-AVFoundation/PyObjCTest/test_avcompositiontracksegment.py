import AVFoundation
from PyObjCTools.TestSupport import *


class TestAVCompositionTrackSegment(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertResultIsBOOL(AVFoundation.AVCompositionTrackSegment.isEmpty)


if __name__ == "__main__":
    main()
