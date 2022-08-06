from PyObjCTools.TestSupport import TestCase, min_sdk_level
import ModelIO
from objc import simd


class TestMDLAnimation(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("MDLJointAnimation")

    @min_sdk_level("10.13")
    def test_methods(self):
        self.assertResultHasType(
            ModelIO.MDLAnimationBindComponent.geometryBindTransform,
            simd.matrix_double4x4.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLAnimationBindComponent.setGeometryBindTransform_,
            0,
            simd.matrix_double4x4.__typestr__,
        )
