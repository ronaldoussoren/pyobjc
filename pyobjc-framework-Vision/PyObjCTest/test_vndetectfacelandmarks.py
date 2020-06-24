from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectFaceLandmarks(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectFaceLandmarksRequestRevision1, 1)
        self.assertEqual(Vision.VNDetectFaceLandmarksRequestRevision2, 2)
