from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNFaceLandmarks(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsVariableSize(Vision.VNFaceLandmarkRegion2D.normalizedPoints)
        self.assertResultIsVariableSize(
            Vision.VNFaceLandmarkRegion2D.pointsInImageOfSize_
        )
