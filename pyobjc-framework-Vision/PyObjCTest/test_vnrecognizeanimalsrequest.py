from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNRecognizeAnimalsRequest(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Vision.VNAnimalIdentifier, str)

    def test_constants(self):
        self.assertEqual(Vision.VNRecognizeAnimalsRequestRevision1, 1)
        self.assertEqual(Vision.VNRecognizeAnimalsRequestRevision2, 2)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Vision.VNAnimalIdentifierDog, str)
        self.assertIsInstance(Vision.VNAnimalIdentifierCat, str)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            Vision.VNRecognizeAnimalsRequest.knownAnimalIdentifiersForRevision_error_, 1
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsOut(
            Vision.VNRecognizeAnimalsRequest.supportedIdentifiersAndReturnError_, 0
        )
