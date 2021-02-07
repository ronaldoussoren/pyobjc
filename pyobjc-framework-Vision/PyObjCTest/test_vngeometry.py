from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNGeometry(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(Vision.VNCircle.containsPoint_)
        self.assertResultIsBOOL(
            Vision.VNCircle.containsPoint_inCircumferentialRingOfWidth_
        )

        # XXX: VNContour.normalizedPoints
