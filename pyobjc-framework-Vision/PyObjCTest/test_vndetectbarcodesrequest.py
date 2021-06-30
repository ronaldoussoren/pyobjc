from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectBarcodesRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectBarcodesRequestRevision1, 1)
        self.assertEqual(Vision.VNDetectBarcodesRequestRevision2, 2)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsOut(
            Vision.VNDetectBarcodesRequest.supportedSymbologiesAndReturnError_, 0
        )
