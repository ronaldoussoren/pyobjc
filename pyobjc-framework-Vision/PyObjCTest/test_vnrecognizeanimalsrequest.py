from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNRecognizeAnimalsRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNRecognizeAnimalsRequestRevision1, 1)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Vision.VNAnimalIdentifierDog, str)
        self.assertIsInstance(Vision.VNAnimalIdentifierCat, str)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            Vision.VNRecognizeAnimalsRequest.knownAnimalIdentifiersForRevision_error_, 1
        )
