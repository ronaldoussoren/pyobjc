from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVision(TestCase):
    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Vision.VNVisionVersionNumber, float)
