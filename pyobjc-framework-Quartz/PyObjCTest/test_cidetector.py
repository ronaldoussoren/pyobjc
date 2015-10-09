from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCIDetector (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(CIDetectorTypeFace, unicode)
        self.assertIsInstance(CIDetectorAccuracy, unicode)
        self.assertIsInstance(CIDetectorAccuracyLow, unicode)
        self.assertIsInstance(CIDetectorAccuracyHigh, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(CIDetectorTracking, unicode)
        self.assertIsInstance(CIDetectorMinFeatureSize, unicode)
        self.assertIsInstance(CIDetectorImageOrientation, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(CIDetectorEyeBlink, unicode)
        self.assertIsInstance(CIDetectorSmile, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(CIDetectorTypeRectangle, unicode)
        self.assertIsInstance(CIDetectorTypeQRCode, unicode)
        self.assertIsInstance(CIDetectorFocalLength, unicode)
        self.assertIsInstance(CIDetectorAspectRatio, unicode)


if __name__ == "__main__":
    main()
