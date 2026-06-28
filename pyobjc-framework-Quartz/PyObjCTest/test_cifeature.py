from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIFeature(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.CIFeatureTypeFace, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(Quartz.CIFeatureTypeRectangle, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(Quartz.CIFeatureTypeQRCode, str)
        self.assertIsInstance(Quartz.CIFeatureTypeText, str)

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.CIFaceFeature.hasLeftEyePosition)
        self.assertResultIsBOOL(Quartz.CIFaceFeature.hasRightEyePosition)
        self.assertResultIsBOOL(Quartz.CIFaceFeature.hasMouthPosition)
        self.assertResultIsBOOL(Quartz.CIFaceFeature.hasTrackingID)
        self.assertResultIsBOOL(Quartz.CIFaceFeature.hasTrackingFrameCount)
        self.assertResultIsBOOL(Quartz.CIFaceFeature.hasFaceAngle)
        self.assertResultIsBOOL(Quartz.CIFaceFeature.hasSmile)
        self.assertResultIsBOOL(Quartz.CIFaceFeature.leftEyeClosed)
        self.assertResultIsBOOL(Quartz.CIFaceFeature.rightEyeClosed)
