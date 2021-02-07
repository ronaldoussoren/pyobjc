from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectBarcodesRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectBarcodesRequestRevision1, 1)
