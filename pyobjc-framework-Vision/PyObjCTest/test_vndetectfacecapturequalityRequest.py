from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import Vision

    class TestVNDetectFaceCaptureQualityRequest(TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNDetectFaceCaptureQualityRequestRevision1, 1)
            self.assertEqual(Vision.VNDetectFaceQualityRequestRevision1, 1)


if __name__ == "__main__":
    main()
