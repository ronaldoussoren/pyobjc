from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNGeometryUtils(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsOut(Vision.VNGeometryUtils.boundingCircleForContour_error_, 1)
        self.assertArgIsOut(Vision.VNGeometryUtils.boundingCircleForPoints_error_, 1)

        # XXX: SIMD argument
        # self.assertArgIsIn(
        #     Vision.VNGeometryUtils.boundingCircleForSIMDPoints_pointCount_error_, 0
        # )
        # self.assertArgSizeInArg(
        #     Vision.VNGeometryUtils.boundingCircleForSIMDPoints_pointCount_error_, 0, 1
        # )
        # self.assertArgIsOut(
        #     Vision.VNGeometryUtils.boundingCircleForSIMDPoints_pointCount_error_, 2
        # )

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
