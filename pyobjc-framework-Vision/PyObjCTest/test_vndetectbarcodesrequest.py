from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectBarcodesRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectBarcodesRequestRevision1, 1)
        self.assertEqual(Vision.VNDetectBarcodesRequestRevision2, 2)
        self.assertEqual(Vision.VNDetectBarcodesRequestRevision3, 3)
        self.assertEqual(Vision.VNDetectBarcodesRequestRevision4, 4)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsOut(
            Vision.VNDetectBarcodesRequest.supportedSymbologiesAndReturnError_, 0
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            Vision.VNDetectBarcodesRequest.coalesceCompositeSymbologies
        )
        self.assertArgIsBOOL(
            Vision.VNDetectBarcodesRequest.setCoalesceCompositeSymbologies_, 0
        )
