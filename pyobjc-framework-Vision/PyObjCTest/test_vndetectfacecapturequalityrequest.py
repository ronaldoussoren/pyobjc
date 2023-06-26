from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectFaceCaptureQualityRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectFaceCaptureQualityRequestRevision1, 1)
        self.assertEqual(Vision.VNDetectFaceCaptureQualityRequestRevision2, 2)
        self.assertEqual(Vision.VNDetectFaceCaptureQualityRequestRevision3, 3)
        self.assertEqual(Vision.VNDetectFaceQualityRequestRevision1, 1)
