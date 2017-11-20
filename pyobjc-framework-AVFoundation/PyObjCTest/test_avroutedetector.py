from PyObjCTools.TestSupport import *

import AVFoundation

class TestAVAnimation (TestCase):
    @min_os_level('10.13')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVRouteDetectorMultipleRoutesDetectedDidChangeNotification, unicode)

    @min_os_level('10.13')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVRouteDetector.isRouteDetectionEnabled)
        self.assertArgIsBOOL(AVFoundation.AVRouteDetector.setRouteDetectionEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVRouteDetector.multipleRoutesDetected)
if __name__ == "__main__":
    main()
