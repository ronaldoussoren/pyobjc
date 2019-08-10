from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import Vision

    class TestVNRecognizeAnimalsRequest(TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNRecognizeAnimalsRequestRevision1, 1)

        @min_os_level("10.15")
        def test_constants10_15(self):
            self.assertIsInstance(Vision.VNAnimalIdentifierDog, unicode)
            self.assertIsInstance(Vision.VNAnimalIdentifierCat, unicode)

        @min_os_level("10.15")
        def test_methods10_15(self):
            self.assertArgIsOut(
                Vision.VNRecognizeAnimalsRequest.knownAnimalIdentifiersForRevision_error_,
                1,
            )


if __name__ == "__main__":
    main()
