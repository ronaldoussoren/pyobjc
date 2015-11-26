from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCIFeature (TestCase):
    def testConstants(self):
        self.assertIsInstance(CIFeatureTypeFace, unicode)
        self.assertIsInstance(CIFeatureTypeRectangle, unicode)
        self.assertIsInstance(CIFeatureTypeQRCode, unicode)
        self.assertIsInstance(CIFeatureTypeText, unicode)

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
