from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNDetectHorizonRequest (TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNDetectHorizonRequestRevision1, 1)



if __name__ == "__main__":
    main()
