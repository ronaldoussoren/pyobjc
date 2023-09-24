from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit
from objc import simd


class TestSKAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SpriteKit.SKUniformType)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKUniformTypeNone, 0)
        self.assertEqual(SpriteKit.SKUniformTypeFloat, 1)
        self.assertEqual(SpriteKit.SKUniformTypeFloatVector2, 2)
        self.assertEqual(SpriteKit.SKUniformTypeFloatVector3, 3)
        self.assertEqual(SpriteKit.SKUniformTypeFloatVector4, 4)
        self.assertEqual(SpriteKit.SKUniformTypeFloatMatrix2, 5)
        self.assertEqual(SpriteKit.SKUniformTypeFloatMatrix3, 6)
        self.assertEqual(SpriteKit.SKUniformTypeFloatMatrix4, 7)
        self.assertEqual(SpriteKit.SKUniformTypeTexture, 8)

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertArgHasType(
            SpriteKit.SKUniform.uniformWithName_vectorFloat2_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.uniformWithName_vectorFloat3_,
            1,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.uniformWithName_vectorFloat4_,
            1,
            simd.vector_float4.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.uniformWithName_matrixFloat2x2_,
            1,
            simd.simd_float2x2.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.uniformWithName_matrixFloat3x3_,
            1,
            simd.simd_float3x3.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.uniformWithName_matrixFloat4x4_,
            1,
            simd.simd_float4x4.__typestr__,
        )

        self.assertResultHasType(
            SpriteKit.SKUniform.vectorFloat2Value, simd.vector_float2.__typestr__
        )
        self.assertResultHasType(
            SpriteKit.SKUniform.vectorFloat3Value, simd.vector_float3.__typestr__
        )
        self.assertResultHasType(
            SpriteKit.SKUniform.vectorFloat4Value, simd.vector_float4.__typestr__
        )
        self.assertResultHasType(
            SpriteKit.SKUniform.matrixFloat2x2Value, simd.simd_float2x2.__typestr__
        )
        self.assertResultHasType(
            SpriteKit.SKUniform.matrixFloat3x3Value, simd.simd_float3x3.__typestr__
        )
        self.assertResultHasType(
            SpriteKit.SKUniform.matrixFloat4x4Value, simd.simd_float4x4.__typestr__
        )

        self.assertArgHasType(
            SpriteKit.SKUniform.initWithName_vectorFloat2_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.initWithName_vectorFloat3_,
            1,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.initWithName_vectorFloat4_,
            1,
            simd.vector_float4.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.initWithName_matrixFloat2x2_,
            1,
            simd.simd_float2x2.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.initWithName_matrixFloat3x3_,
            1,
            simd.simd_float3x3.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKUniform.initWithName_matrixFloat4x4_,
            1,
            simd.simd_float4x4.__typestr__,
        )
