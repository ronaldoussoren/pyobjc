from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetTrackSegment (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrackSegment.isEmpty)

if __name__ == "__main__":
    main()
