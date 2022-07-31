from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision
import Quartz
import objc


class TestVNUtils(TestCase):
    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Vision.VNNormalizedIdentityRect, Quartz.CGRect)

    @min_os_level("10.13")
    def testFunctions(self):
        self.assertResultHasType(Vision.VNNormalizedRectIsIdentityRect, objc._C_BOOL)
        self.assertArgHasType(
            Vision.VNNormalizedRectIsIdentityRect, 0, Quartz.CGRect.__typestr__
        )

        self.assertResultHasType(
            Vision.VNImagePointForNormalizedPoint, Quartz.CGPoint.__typestr__
        )
        self.assertArgHasType(
            Vision.VNImagePointForNormalizedPoint, 0, Quartz.CGPoint.__typestr__
        )
        self.assertArgHasType(Vision.VNImagePointForNormalizedPoint, 1, objc._C_ULNG)
        self.assertArgHasType(Vision.VNImagePointForNormalizedPoint, 2, objc._C_ULNG)

        self.assertResultHasType(
            Vision.VNImageRectForNormalizedRect, Quartz.CGRect.__typestr__
        )
        self.assertArgHasType(
            Vision.VNImageRectForNormalizedRect, 0, Quartz.CGRect.__typestr__
        )
        self.assertArgHasType(Vision.VNImageRectForNormalizedRect, 1, objc._C_ULNG)
        self.assertArgHasType(Vision.VNImageRectForNormalizedRect, 2, objc._C_ULNG)

        self.assertResultHasType(
            Vision.VNNormalizedRectForImageRect, Quartz.CGRect.__typestr__
        )
        self.assertArgHasType(
            Vision.VNNormalizedRectForImageRect, 0, Quartz.CGRect.__typestr__
        )
        self.assertArgHasType(Vision.VNNormalizedRectForImageRect, 1, objc._C_ULNG)
        self.assertArgHasType(Vision.VNNormalizedRectForImageRect, 2, objc._C_ULNG)

        # XXX: These need explict tests
        Vision.VNNormalizedFaceBoundingBoxPointForLandmarkPoint
        Vision.VNImagePointForFaceLandmarkPoint

    @min_os_level("10.15")
    def testFunctions10_15(self):
        Vision.VNElementTypeSize

    @min_os_level("11.0")
    def testFunctions11_0(self):
        Vision.VNNormalizedPointForImagePoint

    @min_os_level("12.0")
    def testFunctions12_0(self):
        Vision.VNImagePointForNormalizedPointUsingRegionOfInterest
        Vision.VNNormalizedPointForImagePointUsingRegionOfInterest
        Vision.VNImageRectForNormalizedRectUsingRegionOfInterest
        Vision.VNNormalizedRectForImageRectUsingRegionOfInterest
