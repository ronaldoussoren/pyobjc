import CoreMotion
from PyObjCTools.TestSupport import TestCase


class TestCMAccelerometer(TestCase):
    def test_structs(self):
        v = CoreMotion.CMRotationMatrix()
        self.assertEqual(v.m11, 0.0)
        self.assertEqual(v.m12, 0.0)
        self.assertEqual(v.m13, 0.0)
        self.assertEqual(v.m21, 0.0)
        self.assertEqual(v.m22, 0.0)
        self.assertEqual(v.m23, 0.0)
        self.assertEqual(v.m31, 0.0)
        self.assertEqual(v.m32, 0.0)
        self.assertEqual(v.m33, 0.0)

        v = CoreMotion.CMQuaternion()
        self.assertEqual(v.x, 0.0)
        self.assertEqual(v.y, 0.0)
        self.assertEqual(v.z, 0.0)
        self.assertEqual(v.w, 0.0)

    def test_constants(self):
        self.assertEqual(CoreMotion.CMAttitudeReferenceFrameXArbitraryZVertical, 1 << 0)
        self.assertEqual(
            CoreMotion.CMAttitudeReferenceFrameXArbitraryCorrectedZVertical, 1 << 1
        )
        self.assertEqual(
            CoreMotion.CMAttitudeReferenceFrameXMagneticNorthZVertical, 1 << 2
        )
        self.assertEqual(CoreMotion.CMAttitudeReferenceFrameXTrueNorthZVertical, 1 << 3)
