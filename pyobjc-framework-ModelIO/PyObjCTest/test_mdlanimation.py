from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level
import ModelIO
from objc import simd


class TestMDLAnimation(TestCase):
    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("MDLJointAnimation")

    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultHasType(
            ModelIO.MDLAnimationBindComponent.geometryBindTransform,
            simd.simd_double4x4.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLAnimationBindComponent.setGeometryBindTransform_,
            0,
            simd.simd_double4x4.__typestr__,
        )
