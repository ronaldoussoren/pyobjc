from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import Vision

    class TestVNObservation(TestCase):
        @min_os_level("10.15")
        def test_methods(self):
            self.assertResultIsBOOL(
                Vision.VNClassificationObservation.hasMinimumRecall_forPrecision_
            )
            self.assertResultIsBOOL(
                Vision.VNClassificationObservation.hasMinimumPrecision_forRecall_
            )

            self.assertArgIsOut(Vision.VNRecognizedText.boundingBoxForRange_error_, 1)

            self.assertResultIsBOOL(
                Vision.VNFeaturePrintObservation.computeDistance_toFeaturePrintObservation_error_
            )
            self.assertArgIsOut(
                Vision.VNFeaturePrintObservation.computeDistance_toFeaturePrintObservation_error_,
                2,
            )


if __name__ == "__main__":
    main()
