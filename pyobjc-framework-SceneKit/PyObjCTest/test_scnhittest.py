from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit
from objc import simd


class TestSCNHitTest(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(SceneKit.SCNHitTestOption, str)

    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNHitTestSearchMode)

    def testConstants(self):
        self.assertEqual(SceneKit.SCNHitTestSearchModeClosest, 0)
        self.assertEqual(SceneKit.SCNHitTestSearchModeAll, 1)
        self.assertEqual(SceneKit.SCNHitTestSearchModeAny, 2)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(SceneKit.SCNHitTestOptionSearchMode, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(SceneKit.SCNHitTestOptionIgnoreLightArea, str)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultHasType(
            SceneKit.SCNHitTestResult.simdLocalCoordinates, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNHitTestResult.simdWorldCoordinates, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNHitTestResult.simdLocalNormal, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNHitTestResult.simdWorldNormal, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNHitTestResult.simdModelTransform, simd.simd_float4x4.__typestr__
        )
