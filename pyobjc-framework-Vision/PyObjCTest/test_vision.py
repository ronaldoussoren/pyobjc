from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVision (TestCase):
        @min_os_level('10.13')
        def testConstants10_13(self):
            self.assertIsInstance(Vision.VNVisionVersionNumber, float)

if __name__ == "__main__":
    main()
