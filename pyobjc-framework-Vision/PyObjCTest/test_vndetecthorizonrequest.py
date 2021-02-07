from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectHorizonRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectHorizonRequestRevision1, 1)
