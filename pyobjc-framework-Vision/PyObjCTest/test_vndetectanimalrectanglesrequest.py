from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNDetectAnimalRectanglesRequest (TestCase):
        @min_os_level('10.15')
        def test_constants(self):
            self.assertIsInstance(Vision.VNAnimalDetectorDog, unicode)
            self.assertIsInstance(Vision.VNAnimalDetectorCat, unicode)

            self.assertEqual(Vision.VNDetectAnimalRectanglesRequestRevision1, 1)

if __name__ == "__main__":
    main()
