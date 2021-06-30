from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectFaceRectanglesRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectFaceRectanglesRequestRevision1, 1)
        self.assertEqual(Vision.VNDetectFaceRectanglesRequestRevision2, 2)
        self.assertEqual(Vision.VNDetectFaceRectanglesRequestRevision3, 3)
