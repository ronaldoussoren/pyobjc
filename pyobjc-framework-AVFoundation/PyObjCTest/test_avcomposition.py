from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVComposition (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVMutableComposition.insertTimeRange_ofAsset_atTime_error_)
        self.assertArgIsOut(AVFoundation.AVMutableComposition.insertTimeRange_ofAsset_atTime_error_, 3)

if __name__ == "__main__":
    main()
