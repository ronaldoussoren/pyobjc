from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNDetectFaceLandmarks (TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNDetectFaceLandmarksRequestRevision1, 1)
            self.assertEqual(Vision.VNDetectFaceLandmarksRequestRevision2, 2)



if __name__ == "__main__":
    main()
