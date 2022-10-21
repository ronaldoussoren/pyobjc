from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit
from objc import simd


class TestSKAttribute(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SpriteKit.SKAttributeType)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKAttributeTypeNone, 0)
        self.assertEqual(SpriteKit.SKAttributeTypeFloat, 1)
        self.assertEqual(SpriteKit.SKAttributeTypeVectorFloat2, 2)
        self.assertEqual(SpriteKit.SKAttributeTypeVectorFloat3, 3)
        self.assertEqual(SpriteKit.SKAttributeTypeVectorFloat4, 4)
        self.assertEqual(SpriteKit.SKAttributeTypeHalfFloat, 5)
        self.assertEqual(SpriteKit.SKAttributeTypeVectorHalfFloat2, 6)
        self.assertEqual(SpriteKit.SKAttributeTypeVectorHalfFloat3, 7)
        self.assertEqual(SpriteKit.SKAttributeTypeVectorHalfFloat4, 8)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertArgHasType(
            SpriteKit.SKAttributeValue.valueWithVectorFloat2_,
            0,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKAttributeValue.valueWithVectorFloat3_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKAttributeValue.valueWithVectorFloat4_,
            0,
            simd.vector_float4.__typestr__,
        )

        self.assertResultHasType(
            SpriteKit.SKAttributeValue.vectorFloat2Value, simd.vector_float2.__typestr__
        )
        self.assertResultHasType(
            SpriteKit.SKAttributeValue.vectorFloat3Value, simd.vector_float3.__typestr__
        )
        self.assertResultHasType(
            SpriteKit.SKAttributeValue.vectorFloat4Value, simd.vector_float4.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SKAttributeValue.setVectorFloat2Value_,
            0,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKAttributeValue.setVectorFloat3Value_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKAttributeValue.setVectorFloat4Value_,
            0,
            simd.vector_float4.__typestr__,
        )

        value = SpriteKit.SKAttributeValue.valueWithVectorFloat2_((1, 2))
        self.assertEqual(value.vectorFloat2Value(), simd.vector_float2(1, 2))
        value.setVectorFloat2Value_((4, 5))
        self.assertEqual(value.vectorFloat2Value(), simd.vector_float2(4, 5))

        value = SpriteKit.SKAttributeValue.valueWithVectorFloat3_((1, 2, 3))
        self.assertEqual(value.vectorFloat3Value(), simd.vector_float3(1, 2, 3))
        value.setVectorFloat3Value_((4, 5, 6))
        self.assertEqual(value.vectorFloat3Value(), simd.vector_float3(4, 5, 6))

        value = SpriteKit.SKAttributeValue.valueWithVectorFloat4_((1, 2, 3, 4))
        self.assertEqual(value.vectorFloat4Value(), simd.vector_float4(1, 2, 3, 4))
        value.setVectorFloat4Value_((4, 5, 6, 7))
        self.assertEqual(value.vectorFloat4Value(), simd.vector_float4(4, 5, 6, 7))
