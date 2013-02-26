from PyObjCTools.TestSupport import *

import AVFoundation

try:
    unicode
except NameError:
    unicode = str

class TestAVAnimation (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(AVFoundation.AVCoreAnimationBeginTimeAtZero, float)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspect, float)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResizeAspectFill, unicode)
        self.assertIsInstance(AVFoundation.AVLayerVideoGravityResize, unicode)

if __name__ == "__main__":
    main()
