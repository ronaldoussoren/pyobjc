from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAssetTrack (TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isPlayable)
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.isEnabled)
        self.assertResultIsBOOL(AVFoundation.AVAssetTrack.hasMediaCharacteristic_)


if __name__ == "__main__":
    main()
