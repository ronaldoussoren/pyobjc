from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVPlayerItemTrack (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItemTrack.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVPlayerItemTrack.setEnabled_, 0)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVPlayerItemTrackVideoFieldModeDeinterlaceFields, unicode)

if __name__ == "__main__":
    main()
