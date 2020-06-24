from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectHumanRectanglesRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectHumanRectanglesRequestRevision1, 1)
