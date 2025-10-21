import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestMTLRenderPipelineHelper(Metal.NSObject):
    def functionHandleWithName_stage_(self, a, b):
        pass

    def functionHandleWithBinaryFunction_stage_(self, a, b):
        pass

    def newRenderPipelineStateWithBinaryFunctions_error_(self, a, b):
        pass

    def maxTotalThreadsPerThreadgroup(self):
        return 1

    def threadgroupSizeMatchesTileSize(self):
        return 1

    def imageblockSampleLength(self):
        return 1

    def supportIndirectCommandBuffers(self):
        return 1

    def maxTotalThreadsPerObjectThreadgroup(self):
        return 1

    def maxTotalThreadsPerMeshThreadgroup(self):
        return 1

    def objectThreadExecutionWidth(self):
        return 1

    def meshThreadExecutionWidth(self):
        return 1

    def maxTotalThreadgroupsPerMeshGrid(self):
        return 1

    def gpuResourceID(self):
        return 1

    def functionHandleWithFunction_stage_(self, a, b):
        return 1

    def newVisibleFunctionTableWithDescriptor_stage_(self, a, b):
        return 1

    def newIntersectionFunctionTableWithDescriptor_stage_(self, a, b):
        return 1

    def newRenderPipelineStateWithAdditionalBinaryFunctions_error_(self, a, b):
        return 1

    def shaderValidation(self):
        return 1

    def requiredThreadsPerTileThreadgroup(self):
        return 1

    def requiredThreadsPerObjectThreadgroup(self):
        return 1

    def requiredThreadsPerMeshThreadgroup(self):
        return 1


class TestMTLRenderPipeline(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLArgumentAccess)
        self.assertIsEnumType(Metal.MTLArgumentType)
        self.assertIsEnumType(Metal.MTLDataType)

    def test_constants(self):
        self.assertEqual(Metal.MTLDataTypeNone, 0)
        self.assertEqual(Metal.MTLDataTypeStruct, 1)
        self.assertEqual(Metal.MTLDataTypeArray, 2)
        self.assertEqual(Metal.MTLDataTypeFloat, 3)
        self.assertEqual(Metal.MTLDataTypeFloat2, 4)
        self.assertEqual(Metal.MTLDataTypeFloat3, 5)
        self.assertEqual(Metal.MTLDataTypeFloat4, 6)
        self.assertEqual(Metal.MTLDataTypeFloat2x2, 7)
        self.assertEqual(Metal.MTLDataTypeFloat2x3, 8)
        self.assertEqual(Metal.MTLDataTypeFloat2x4, 9)
        self.assertEqual(Metal.MTLDataTypeFloat3x2, 10)
        self.assertEqual(Metal.MTLDataTypeFloat3x3, 11)
        self.assertEqual(Metal.MTLDataTypeFloat3x4, 12)
        self.assertEqual(Metal.MTLDataTypeFloat4x2, 13)
        self.assertEqual(Metal.MTLDataTypeFloat4x3, 14)
        self.assertEqual(Metal.MTLDataTypeFloat4x4, 15)
        self.assertEqual(Metal.MTLDataTypeHalf, 16)
        self.assertEqual(Metal.MTLDataTypeHalf2, 17)
        self.assertEqual(Metal.MTLDataTypeHalf3, 18)
        self.assertEqual(Metal.MTLDataTypeHalf4, 19)
        self.assertEqual(Metal.MTLDataTypeHalf2x2, 20)
        self.assertEqual(Metal.MTLDataTypeHalf2x3, 21)
        self.assertEqual(Metal.MTLDataTypeHalf2x4, 22)
        self.assertEqual(Metal.MTLDataTypeHalf3x2, 23)
        self.assertEqual(Metal.MTLDataTypeHalf3x3, 24)
        self.assertEqual(Metal.MTLDataTypeHalf3x4, 25)
        self.assertEqual(Metal.MTLDataTypeHalf4x2, 26)
        self.assertEqual(Metal.MTLDataTypeHalf4x3, 27)
        self.assertEqual(Metal.MTLDataTypeHalf4x4, 28)
        self.assertEqual(Metal.MTLDataTypeInt, 29)
        self.assertEqual(Metal.MTLDataTypeInt2, 30)
        self.assertEqual(Metal.MTLDataTypeInt3, 31)
        self.assertEqual(Metal.MTLDataTypeInt4, 32)
        self.assertEqual(Metal.MTLDataTypeUInt, 33)
        self.assertEqual(Metal.MTLDataTypeUInt2, 34)
        self.assertEqual(Metal.MTLDataTypeUInt3, 35)
        self.assertEqual(Metal.MTLDataTypeUInt4, 36)
        self.assertEqual(Metal.MTLDataTypeShort, 37)
        self.assertEqual(Metal.MTLDataTypeShort2, 38)
        self.assertEqual(Metal.MTLDataTypeShort3, 39)
        self.assertEqual(Metal.MTLDataTypeShort4, 40)
        self.assertEqual(Metal.MTLDataTypeUShort, 41)
        self.assertEqual(Metal.MTLDataTypeUShort2, 42)
        self.assertEqual(Metal.MTLDataTypeUShort3, 43)
        self.assertEqual(Metal.MTLDataTypeUShort4, 44)
        self.assertEqual(Metal.MTLDataTypeChar, 45)
        self.assertEqual(Metal.MTLDataTypeChar2, 46)
        self.assertEqual(Metal.MTLDataTypeChar3, 47)
        self.assertEqual(Metal.MTLDataTypeChar4, 48)
        self.assertEqual(Metal.MTLDataTypeUChar, 49)
        self.assertEqual(Metal.MTLDataTypeUChar2, 50)
        self.assertEqual(Metal.MTLDataTypeUChar3, 51)
        self.assertEqual(Metal.MTLDataTypeUChar4, 52)
        self.assertEqual(Metal.MTLDataTypeBool, 53)
        self.assertEqual(Metal.MTLDataTypeBool2, 54)
        self.assertEqual(Metal.MTLDataTypeBool3, 55)
        self.assertEqual(Metal.MTLDataTypeBool4, 56)
        self.assertEqual(Metal.MTLDataTypeTexture, 58)
        self.assertEqual(Metal.MTLDataTypeSampler, 59)
        self.assertEqual(Metal.MTLDataTypePointer, 60)
        self.assertEqual(Metal.MTLDataTypeR8Unorm, 62)
        self.assertEqual(Metal.MTLDataTypeR8Snorm, 63)
        self.assertEqual(Metal.MTLDataTypeR16Unorm, 64)
        self.assertEqual(Metal.MTLDataTypeR16Snorm, 65)
        self.assertEqual(Metal.MTLDataTypeRG8Unorm, 66)
        self.assertEqual(Metal.MTLDataTypeRG8Snorm, 67)
        self.assertEqual(Metal.MTLDataTypeRG16Unorm, 68)
        self.assertEqual(Metal.MTLDataTypeRG16Snorm, 69)
        self.assertEqual(Metal.MTLDataTypeRGBA8Unorm, 70)
        self.assertEqual(Metal.MTLDataTypeRGBA8Unorm_sRGB, 71)
        self.assertEqual(Metal.MTLDataTypeRGBA8Snorm, 72)
        self.assertEqual(Metal.MTLDataTypeRGBA16Unorm, 73)
        self.assertEqual(Metal.MTLDataTypeRGBA16Snorm, 74)
        self.assertEqual(Metal.MTLDataTypeRGB10A2Unorm, 75)
        self.assertEqual(Metal.MTLDataTypeRG11B10Float, 76)
        self.assertEqual(Metal.MTLDataTypeRGB9E5Float, 77)
        self.assertEqual(Metal.MTLDataTypeRenderPipeline, 78)
        self.assertEqual(Metal.MTLDataTypeComputePipeline, 79)
        self.assertEqual(Metal.MTLDataTypeIndirectCommandBuffer, 80)
        self.assertEqual(Metal.MTLDataTypeLong, 81)
        self.assertEqual(Metal.MTLDataTypeLong2, 82)
        self.assertEqual(Metal.MTLDataTypeLong3, 83)
        self.assertEqual(Metal.MTLDataTypeLong4, 84)
        self.assertEqual(Metal.MTLDataTypeULong, 85)
        self.assertEqual(Metal.MTLDataTypeULong2, 86)
        self.assertEqual(Metal.MTLDataTypeULong3, 87)
        self.assertEqual(Metal.MTLDataTypeULong4, 88)

        self.assertEqual(Metal.MTLDataTypeVisibleFunctionTable, 115)
        self.assertEqual(Metal.MTLDataTypeIntersectionFunctionTable, 116)
        self.assertEqual(Metal.MTLDataTypePrimitiveAccelerationStructure, 117)
        self.assertEqual(Metal.MTLDataTypeInstanceAccelerationStructure, 118)

        self.assertEqual(Metal.MTLArgumentTypeBuffer, 0)
        self.assertEqual(Metal.MTLArgumentTypeThreadgroupMemory, 1)
        self.assertEqual(Metal.MTLArgumentTypeTexture, 2)
        self.assertEqual(Metal.MTLArgumentTypeSampler, 3)
        self.assertEqual(Metal.MTLArgumentTypeImageblockData, 16)
        self.assertEqual(Metal.MTLArgumentTypeImageblock, 17)
        self.assertEqual(Metal.MTLArgumentTypeVisibleFunctionTable, 24)
        self.assertEqual(Metal.MTLArgumentTypePrimitiveAccelerationStructure, 25)
        self.assertEqual(Metal.MTLArgumentTypeInstanceAccelerationStructure, 26)
        self.assertEqual(Metal.MTLArgumentTypeIntersectionFunctionTable, 27)

        self.assertEqual(Metal.MTLArgumentAccessReadOnly, 0)
        self.assertEqual(Metal.MTLArgumentAccessReadWrite, 1)
        self.assertEqual(Metal.MTLArgumentAccessWriteOnly, 2)

        self.assertIsEnumType(Metal.MTLBlendFactor)
        self.assertEqual(Metal.MTLBlendFactorZero, 0)
        self.assertEqual(Metal.MTLBlendFactorOne, 1)
        self.assertEqual(Metal.MTLBlendFactorSourceColor, 2)
        self.assertEqual(Metal.MTLBlendFactorOneMinusSourceColor, 3)
        self.assertEqual(Metal.MTLBlendFactorSourceAlpha, 4)
        self.assertEqual(Metal.MTLBlendFactorOneMinusSourceAlpha, 5)
        self.assertEqual(Metal.MTLBlendFactorDestinationColor, 6)
        self.assertEqual(Metal.MTLBlendFactorOneMinusDestinationColor, 7)
        self.assertEqual(Metal.MTLBlendFactorDestinationAlpha, 8)
        self.assertEqual(Metal.MTLBlendFactorOneMinusDestinationAlpha, 9)
        self.assertEqual(Metal.MTLBlendFactorSourceAlphaSaturated, 10)
        self.assertEqual(Metal.MTLBlendFactorBlendColor, 11)
        self.assertEqual(Metal.MTLBlendFactorOneMinusBlendColor, 12)
        self.assertEqual(Metal.MTLBlendFactorBlendAlpha, 13)
        self.assertEqual(Metal.MTLBlendFactorOneMinusBlendAlpha, 14)
        self.assertEqual(Metal.MTLBlendFactorSource1Color, 15)
        self.assertEqual(Metal.MTLBlendFactorOneMinusSource1Color, 16)
        self.assertEqual(Metal.MTLBlendFactorSource1Alpha, 17)
        self.assertEqual(Metal.MTLBlendFactorOneMinusSource1Alpha, 18)
        self.assertEqual(Metal.MTLBlendFactorUnspecialized, 19)

        self.assertIsEnumType(Metal.MTLBlendOperation)
        self.assertEqual(Metal.MTLBlendOperationAdd, 0)
        self.assertEqual(Metal.MTLBlendOperationSubtract, 1)
        self.assertEqual(Metal.MTLBlendOperationReverseSubtract, 2)
        self.assertEqual(Metal.MTLBlendOperationMin, 3)
        self.assertEqual(Metal.MTLBlendOperationMax, 4)
        self.assertEqual(Metal.MTLBlendOperationUnspecialized, 5)

        self.assertIsEnumType(Metal.MTLColorWriteMask)
        self.assertEqual(Metal.MTLColorWriteMaskNone, 0)
        self.assertEqual(Metal.MTLColorWriteMaskRed, 0x1 << 3)
        self.assertEqual(Metal.MTLColorWriteMaskGreen, 0x1 << 2)
        self.assertEqual(Metal.MTLColorWriteMaskBlue, 0x1 << 1)
        self.assertEqual(Metal.MTLColorWriteMaskAlpha, 0x1 << 0)
        self.assertEqual(Metal.MTLColorWriteMaskAll, 0xF)
        self.assertEqual(Metal.MTLColorWriteMaskUnspecialized, 0x10)

        self.assertIsEnumType(Metal.MTLPrimitiveTopologyClass)
        self.assertEqual(Metal.MTLPrimitiveTopologyClassUnspecified, 0)
        self.assertEqual(Metal.MTLPrimitiveTopologyClassPoint, 1)
        self.assertEqual(Metal.MTLPrimitiveTopologyClassLine, 2)
        self.assertEqual(Metal.MTLPrimitiveTopologyClassTriangle, 3)

        self.assertIsEnumType(Metal.MTLTessellationPartitionMode)
        self.assertEqual(Metal.MTLTessellationPartitionModePow2, 0)
        self.assertEqual(Metal.MTLTessellationPartitionModeInteger, 1)
        self.assertEqual(Metal.MTLTessellationPartitionModeFractionalOdd, 2)
        self.assertEqual(Metal.MTLTessellationPartitionModeFractionalEven, 3)

        self.assertIsEnumType(Metal.MTLTessellationFactorStepFunction)
        self.assertEqual(Metal.MTLTessellationFactorStepFunctionConstant, 0)
        self.assertEqual(Metal.MTLTessellationFactorStepFunctionPerPatch, 1)
        self.assertEqual(Metal.MTLTessellationFactorStepFunctionPerInstance, 2)
        self.assertEqual(
            Metal.MTLTessellationFactorStepFunctionPerPatchAndPerInstance, 3
        )

        self.assertIsEnumType(Metal.MTLTessellationFactorFormat)
        self.assertEqual(Metal.MTLTessellationFactorFormatHalf, 0)

        self.assertIsEnumType(Metal.MTLTessellationControlPointIndexType)
        self.assertEqual(Metal.MTLTessellationControlPointIndexTypeNone, 0)
        self.assertEqual(Metal.MTLTessellationControlPointIndexTypeUInt16, 1)
        self.assertEqual(Metal.MTLTessellationControlPointIndexTypeUInt32, 2)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(Metal.MTLArgument.alloc().init().isActive)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(
            Metal.MTLPointerType.alloc().init().elementIsArgumentBuffer
        )
        self.assertResultIsBOOL(
            Metal.MTLTextureReferenceType.alloc().init().isDepthTexture
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(
            Metal.MTLTileRenderPipelineDescriptor.alloc()
            .init()
            .threadgroupSizeMatchesTileSize
        )
        self.assertArgIsBOOL(
            Metal.MTLTileRenderPipelineDescriptor.alloc()
            .init()
            .setThreadgroupSizeMatchesTileSize_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTLTileRenderPipelineDescriptor.alloc()
            .init()
            .supportAddingBinaryFunctions
        )
        self.assertArgIsBOOL(
            Metal.MTLTileRenderPipelineDescriptor.alloc()
            .init()
            .setSupportAddingBinaryFunctions_,
            0,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .objectThreadgroupSizeIsMultipleOfThreadExecutionWidth
        )
        self.assertArgIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .setObjectThreadgroupSizeIsMultipleOfThreadExecutionWidth_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .meshThreadgroupSizeIsMultipleOfThreadExecutionWidth
        )
        self.assertArgIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .setMeshThreadgroupSizeIsMultipleOfThreadExecutionWidth_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .isAlphaToCoverageEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .setAlphaToCoverageEnabled_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc().init().isRasterizationEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .setRasterizationEnabled_,
            0,
        )

    @min_os_level("14.0")
    def test_methods14_2(self):
        self.assertResultIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .supportIndirectCommandBuffers
        )
        self.assertArgIsBOOL(
            Metal.MTLMeshRenderPipelineDescriptor.alloc()
            .init()
            .setSupportIndirectCommandBuffers_,
            0,
        )

    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLRenderPipelineState")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMTLRenderPipelineHelper.functionHandleWithName_stage_, 1, b"Q"
        )
        self.assertArgHasType(
            TestMTLRenderPipelineHelper.functionHandleWithBinaryFunction_stage_, 1, b"Q"
        )
        self.assertArgHasType(
            TestMTLRenderPipelineHelper.newRenderPipelineStateWithBinaryFunctions_error_,
            1,
            b"o^@",
        )

        self.assertResultHasType(
            TestMTLRenderPipelineHelper.maxTotalThreadsPerThreadgroup, b"Q"
        )
        self.assertResultIsBOOL(
            TestMTLRenderPipelineHelper.threadgroupSizeMatchesTileSize
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.imageblockSampleLength, b"q"
        )
        self.assertResultIsBOOL(
            TestMTLRenderPipelineHelper.supportIndirectCommandBuffers
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.maxTotalThreadsPerObjectThreadgroup, b"Q"
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.maxTotalThreadsPerMeshThreadgroup, b"Q"
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.objectThreadExecutionWidth, b"Q"
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.meshThreadExecutionWidth, b"Q"
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.maxTotalThreadgroupsPerMeshGrid, b"Q"
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.gpuResourceID, Metal.MTLResourceID.__typestr__
        )
        self.assertArgHasType(
            TestMTLRenderPipelineHelper.functionHandleWithFunction_stage_, 1, b"Q"
        )
        self.assertArgHasType(
            TestMTLRenderPipelineHelper.newVisibleFunctionTableWithDescriptor_stage_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTLRenderPipelineHelper.newIntersectionFunctionTableWithDescriptor_stage_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTLRenderPipelineHelper.newRenderPipelineStateWithAdditionalBinaryFunctions_error_,
            1,
            b"o^@",
        )

        self.assertResultHasType(TestMTLRenderPipelineHelper.shaderValidation, b"q")
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.requiredThreadsPerTileThreadgroup,
            Metal.MTLSize.__typestr__,
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.requiredThreadsPerObjectThreadgroup,
            Metal.MTLSize.__typestr__,
        )
        self.assertResultHasType(
            TestMTLRenderPipelineHelper.requiredThreadsPerMeshThreadgroup,
            Metal.MTLSize.__typestr__,
        )
