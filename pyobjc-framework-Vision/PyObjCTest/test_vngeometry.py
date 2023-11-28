from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision
from objc import simd


class TestVNGeometry(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(Vision.VNCircle.containsPoint_)
        self.assertResultIsBOOL(
            Vision.VNCircle.containsPoint_inCircumferentialRingOfWidth_
        )

        self.assertResultIsVariableSize(Vision.VNContour.normalizedPoints)
        self.assertResultHasType(
            Vision.VNContour.normalizedPoints, b"^" + simd.simd_float2.__typestr__
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgHasType(
            Vision.VNPoint3D.initWithPosition_, 0, simd.simd_float4x4.__typestr__
        )
        self.assertResultHasType(
            Vision.VNPoint3D.position, simd.simd_float4x4.__typestr__
        )
