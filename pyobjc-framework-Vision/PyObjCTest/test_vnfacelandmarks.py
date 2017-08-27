from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNFaceLandmarks (TestCase):
        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertResultIsVariableSize(Vision.VNFaceLandmarkRegion2D.normalizedPoints)
            self.assertResultIsVariableSize(Vision.VNFaceLandmarkRegion2D.pointsInImageOfSize_)


if __name__ == "__main__":
    main()
