from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision
from objc import simd


class TestVNGeometryUtils(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsOut(Vision.VNGeometryUtils.boundingCircleForContour_error_, 1)
        self.assertArgIsOut(Vision.VNGeometryUtils.boundingCircleForPoints_error_, 1)

        self.assertArgHasType(
            Vision.VNGeometryUtils.boundingCircleForSIMDPoints_pointCount_error_,
            0,
            b"n^" + simd.simd_float2.__typestr__,
        )
        self.assertArgIsIn(
            Vision.VNGeometryUtils.boundingCircleForSIMDPoints_pointCount_error_, 0
        )
        self.assertArgSizeInArg(
            Vision.VNGeometryUtils.boundingCircleForSIMDPoints_pointCount_error_, 0, 1
        )
        self.assertArgIsOut(
            Vision.VNGeometryUtils.boundingCircleForSIMDPoints_pointCount_error_, 2
        )

        self.assertResultIsBOOL(
            Vision.VNGeometryUtils.calculateArea_forContour_orientedArea_error_
        )
        self.assertArgIsIn(
            Vision.VNGeometryUtils.calculateArea_forContour_orientedArea_error_, 0
        )
        self.assertArgIsBOOL(
            Vision.VNGeometryUtils.calculateArea_forContour_orientedArea_error_, 2
        )
        self.assertArgIsOut(
            Vision.VNGeometryUtils.calculateArea_forContour_orientedArea_error_, 3
        )

        self.assertResultIsBOOL(
            Vision.VNGeometryUtils.calculatePerimeter_forContour_error_
        )
        self.assertArgIsIn(
            Vision.VNGeometryUtils.calculatePerimeter_forContour_error_, 0
        )
        self.assertArgIsOut(
            Vision.VNGeometryUtils.calculatePerimeter_forContour_error_, 2
        )
