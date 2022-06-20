import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAnimation(TestCase):
    @min_os_level("10.13")
    def testConstants(self):
        self.assertIsInstance(
            AVFoundation.AVRouteDetectorMultipleRoutesDetectedDidChangeNotification, str
        )

    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVRouteDetector.isRouteDetectionEnabled)
        self.assertArgIsBOOL(AVFoundation.AVRouteDetector.setRouteDetectionEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVRouteDetector.multipleRoutesDetected)

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBOOL(AVFoundation.AVRouteDetector.detectsCustomRoutes)
