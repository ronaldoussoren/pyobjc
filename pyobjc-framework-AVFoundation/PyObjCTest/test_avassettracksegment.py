from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetTrackSegment (TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrackSegment.isEmpty)

if __name__ == "__main__":
    main()
