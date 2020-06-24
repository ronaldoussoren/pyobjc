from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIDetector(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Quartz.CIDetectorTypeFace, str)
        self.assertIsInstance(Quartz.CIDetectorAccuracy, str)
        self.assertIsInstance(Quartz.CIDetectorAccuracyLow, str)
        self.assertIsInstance(Quartz.CIDetectorAccuracyHigh, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(Quartz.CIDetectorTracking, str)
        self.assertIsInstance(Quartz.CIDetectorMinFeatureSize, str)
        self.assertIsInstance(Quartz.CIDetectorImageOrientation, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Quartz.CIDetectorEyeBlink, str)
        self.assertIsInstance(Quartz.CIDetectorSmile, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Quartz.CIDetectorTypeRectangle, str)
        self.assertIsInstance(Quartz.CIDetectorTypeQRCode, str)
        self.assertIsInstance(Quartz.CIDetectorFocalLength, str)
        self.assertIsInstance(Quartz.CIDetectorAspectRatio, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.CIDetectorNumberOfAngles, str)

    @min_os_level("10.11")
    def testConstants10_11_64bit(self):
        self.assertIsInstance(Quartz.CIDetectorTypeText, str)
        self.assertIsInstance(Quartz.CIDetectorReturnSubFeatures, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.CIDetectorMaxFeatureCount, str)
