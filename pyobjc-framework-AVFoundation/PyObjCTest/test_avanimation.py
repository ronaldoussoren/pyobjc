from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAnimation (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVCoreAnimationBeginTimeAtZero, float)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspect, unicode)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspectFill, unicode)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResize, unicode)

if __name__ == "__main__":
    main()
