from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVCompositionTrack (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVMutableCompositionTrack.insertTimeRange_ofTrack_atTime_error_)
        self.assertArgIsOut(AVFoundation.AVMutableCompositionTrack.insertTimeRange_ofTrack_atTime_error_, 3)

        self.assertResultIsBOOL(AVFoundation.AVMutableCompositionTrack.insertTimeRanges_ofTracks_atTime_error_)
        self.assertArgIsOut(AVFoundation.AVMutableCompositionTrack.insertTimeRanges_ofTracks_atTime_error_, 3)

        self.assertResultIsBOOL(AVFoundation.AVMutableCompositionTrack.validateTrackSegments_error_)
        self.assertArgIsOut(AVFoundation.AVMutableCompositionTrack.validateTrackSegments_error_, 1)

if __name__ == "__main__":
    main()
