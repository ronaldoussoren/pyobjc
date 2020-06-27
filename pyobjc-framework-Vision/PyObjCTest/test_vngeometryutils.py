from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNGeometryUtils(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsOut(Vision.VNGeometryUtils.boundingCircleForContour_error_, 1)
        self.assertArgIsOut(Vision.VNGeometryUtils.boundingCircleForPoints_error_, 1)

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
            Vision.VMGeometryUtils.calculateArea_forCountour_orientedArea_error_
        )
        self.assertArgIsIn(
            Vision.VMGeometryUtils.calculateArea_forCountour_orientedArea_error_, 0
        )
        self.assertArgIsBOOL(
            Vision.VMGeometryUtils.calculateArea_forCountour_orientedArea_error_, 1
        )
        self.assertArgIsOut(
            Vision.VMGeometryUtils.calculateArea_forCountour_orientedArea_error_, 2
        )

        self.assertResultIsBOOL(
            Vision.VMGeometryUtils.calculatePerimeter_forCountour_orientedArea_error_
        )
        self.assertArgIsIn(
            Vision.VMGeometryUtils.calculatePerimeter_forCountour_orientedArea_error_, 0
        )
        self.assertArgIsBOOL(
            Vision.VMGeometryUtils.calculatePerimeter_forCountour_orientedArea_error_, 1
        )
        self.assertArgIsOut(
            Vision.VMGeometryUtils.calculatePerimeter_forCountour_orientedArea_error_, 2
        )
