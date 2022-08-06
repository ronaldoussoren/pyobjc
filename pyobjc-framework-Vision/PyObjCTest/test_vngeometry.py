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
