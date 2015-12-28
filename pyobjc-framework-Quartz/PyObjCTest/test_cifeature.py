from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIFeature (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(CIFeatureTypeFace, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(CIFeatureTypeRectangle, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(CIFeatureTypeQRCode, unicode)
        self.assertIsInstance(CIFeatureTypeText, unicode)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(CIFaceFeature.hasLeftEyePosition)
        self.assertResultIsBOOL(CIFaceFeature.hasRightEyePosition)
        self.assertResultIsBOOL(CIFaceFeature.hasMouthPosition)
        self.assertResultIsBOOL(CIFaceFeature.hasTrackingID)
        self.assertResultIsBOOL(CIFaceFeature.hasTrackingFrameCount)
        self.assertResultIsBOOL(CIFaceFeature.hasFaceAngle)
        self.assertResultIsBOOL(CIFaceFeature.hasSmile)
        self.assertResultIsBOOL(CIFaceFeature.leftEyeClosed)
        self.assertResultIsBOOL(CIFaceFeature.rightEyeClosed)

if __name__ == "__main__":
    main()
