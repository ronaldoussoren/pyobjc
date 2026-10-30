import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAnimation(TestCase):
    @min_os_level("10.13")
    def test_constants(self):
        self.assertIsInstance(
            AVFoundation.AVRouteDetectorMultipleRoutesDetectedDidChangeNotification, str
        )

    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVRouteDetector.isRouteDetectionEnabled)
        self.assertArgIsBOOL(AVFoundation.AVRouteDetector.setRouteDetectionEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVRouteDetector.multipleRoutesDetected)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(AVFoundation.AVRouteDetector.detectsCustomRoutes)
