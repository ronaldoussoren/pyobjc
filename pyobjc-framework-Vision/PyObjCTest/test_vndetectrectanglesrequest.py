from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectRectanglesRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectRectanglesRequestRevision1, 1)
