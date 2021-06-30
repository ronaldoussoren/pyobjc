from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNGeometry(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(Vision.VNCircle.containsPoint_)
        self.assertResultIsBOOL(
            Vision.VNCircle.containsPoint_inCircumferentialRingOfWidth_
        )

        # XXX: VNContour.normalizedPoints
