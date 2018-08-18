from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNDetectFaceRectanglesRequest (TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNDetectFaceRectanglesRequestRevision1, 1)
            self.assertEqual(Vision.VNDetectFaceRectanglesRequestRevision2, 2)


if __name__ == "__main__":
    main()
