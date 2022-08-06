from PyObjCTools.TestSupport import TestCase
import ModelIO
from objc import simd


class TestMDLVertexDescriptor(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ModelIO.MDLVertexFormat)

    def testConstants(self):
        self.assertIsInstance(ModelIO.MDLVertexAttributeAnisotropy, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeBinormal, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeBitangent, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeColor, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeEdgeCrease, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeJointIndices, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeJointWeights, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeNormal, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeOcclusionValue, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributePosition, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeShadingBasisU, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeShadingBasisV, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeSubdivisionStencil, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeTangent, str)
        self.assertIsInstance(ModelIO.MDLVertexAttributeTextureCoordinate, str)

        self.assertEqual(ModelIO.MDLVertexFormatInvalid, 0)
        self.assertEqual(ModelIO.MDLVertexFormatPackedBit, 0x1000)
        self.assertEqual(ModelIO.MDLVertexFormatUCharBits, 0x10000)
        self.assertEqual(ModelIO.MDLVertexFormatCharBits, 0x20000)
        self.assertEqual(ModelIO.MDLVertexFormatUCharNormalizedBits, 0x30000)
        self.assertEqual(ModelIO.MDLVertexFormatCharNormalizedBits, 0x40000)
        self.assertEqual(ModelIO.MDLVertexFormatUShortBits, 0x50000)
        self.assertEqual(ModelIO.MDLVertexFormatShortBits, 0x60000)
        self.assertEqual(ModelIO.MDLVertexFormatUShortNormalizedBits, 0x70000)
        self.assertEqual(ModelIO.MDLVertexFormatShortNormalizedBits, 0x80000)
        self.assertEqual(ModelIO.MDLVertexFormatUIntBits, 0x90000)
        self.assertEqual(ModelIO.MDLVertexFormatIntBits, 0xA0000)
        self.assertEqual(ModelIO.MDLVertexFormatHalfBits, 0xB0000)
        self.assertEqual(ModelIO.MDLVertexFormatFloatBits, 0xC0000)
        self.assertEqual(
            ModelIO.MDLVertexFormatUChar, ModelIO.MDLVertexFormatUCharBits | 1
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUChar2, ModelIO.MDLVertexFormatUCharBits | 2
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUChar3, ModelIO.MDLVertexFormatUCharBits | 3
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUChar4, ModelIO.MDLVertexFormatUCharBits | 4
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatChar, ModelIO.MDLVertexFormatCharBits | 1
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatChar2, ModelIO.MDLVertexFormatCharBits | 2
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatChar3, ModelIO.MDLVertexFormatCharBits | 3
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatChar4, ModelIO.MDLVertexFormatCharBits | 4
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUCharNormalized,
            ModelIO.MDLVertexFormatUCharNormalizedBits | 1,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUChar2Normalized,
            ModelIO.MDLVertexFormatUCharNormalizedBits | 2,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUChar3Normalized,
            ModelIO.MDLVertexFormatUCharNormalizedBits | 3,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUChar4Normalized,
            ModelIO.MDLVertexFormatUCharNormalizedBits | 4,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatCharNormalized,
            ModelIO.MDLVertexFormatCharNormalizedBits | 1,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatChar2Normalized,
            ModelIO.MDLVertexFormatCharNormalizedBits | 2,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatChar3Normalized,
            ModelIO.MDLVertexFormatCharNormalizedBits | 3,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatChar4Normalized,
            ModelIO.MDLVertexFormatCharNormalizedBits | 4,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUShort, ModelIO.MDLVertexFormatUShortBits | 1
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUShort2, ModelIO.MDLVertexFormatUShortBits | 2
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUShort3, ModelIO.MDLVertexFormatUShortBits | 3
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUShort4, ModelIO.MDLVertexFormatUShortBits | 4
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatShort, ModelIO.MDLVertexFormatShortBits | 1
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatShort2, ModelIO.MDLVertexFormatShortBits | 2
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatShort3, ModelIO.MDLVertexFormatShortBits | 3
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatShort4, ModelIO.MDLVertexFormatShortBits | 4
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUShortNormalized,
            ModelIO.MDLVertexFormatUShortNormalizedBits | 1,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUShort2Normalized,
            ModelIO.MDLVertexFormatUShortNormalizedBits | 2,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUShort3Normalized,
            ModelIO.MDLVertexFormatUShortNormalizedBits | 3,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUShort4Normalized,
            ModelIO.MDLVertexFormatUShortNormalizedBits | 4,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatShortNormalized,
            ModelIO.MDLVertexFormatShortNormalizedBits | 1,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatShort2Normalized,
            ModelIO.MDLVertexFormatShortNormalizedBits | 2,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatShort3Normalized,
            ModelIO.MDLVertexFormatShortNormalizedBits | 3,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatShort4Normalized,
            ModelIO.MDLVertexFormatShortNormalizedBits | 4,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUInt, ModelIO.MDLVertexFormatUIntBits | 1
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUInt2, ModelIO.MDLVertexFormatUIntBits | 2
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUInt3, ModelIO.MDLVertexFormatUIntBits | 3
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUInt4, ModelIO.MDLVertexFormatUIntBits | 4
        )
        self.assertEqual(ModelIO.MDLVertexFormatInt, ModelIO.MDLVertexFormatIntBits | 1)
        self.assertEqual(
            ModelIO.MDLVertexFormatInt2, ModelIO.MDLVertexFormatIntBits | 2
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatInt3, ModelIO.MDLVertexFormatIntBits | 3
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatInt4, ModelIO.MDLVertexFormatIntBits | 4
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatHalf, ModelIO.MDLVertexFormatHalfBits | 1
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatHalf2, ModelIO.MDLVertexFormatHalfBits | 2
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatHalf3, ModelIO.MDLVertexFormatHalfBits | 3
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatHalf4, ModelIO.MDLVertexFormatHalfBits | 4
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatFloat, ModelIO.MDLVertexFormatFloatBits | 1
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatFloat2, ModelIO.MDLVertexFormatFloatBits | 2
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatFloat3, ModelIO.MDLVertexFormatFloatBits | 3
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatFloat4, ModelIO.MDLVertexFormatFloatBits | 4
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatInt1010102Normalized,
            ModelIO.MDLVertexFormatIntBits | ModelIO.MDLVertexFormatPackedBit | 4,
        )
        self.assertEqual(
            ModelIO.MDLVertexFormatUInt1010102Normalized,
            ModelIO.MDLVertexFormatUIntBits | ModelIO.MDLVertexFormatPackedBit | 4,
        )

    def test_methods(self):
        self.assertResultHasType(
            ModelIO.MDLVertexAttribute.initializationValue,
            simd.vector_float4.__typestr__,
        )
        self.assertArgHasType(
            ModelIO.MDLVertexAttribute.setInitializationValue_,
            0,
            simd.vector_float4.__typestr__,
        )
