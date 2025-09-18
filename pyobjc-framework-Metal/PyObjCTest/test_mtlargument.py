import Metal
import objc
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    min_sdk_level,
    expectedFailureIf,
    os_release,
    os_level_key,
)


class TestMTLArgumentHelper(Metal.NSObject):
    def index(self):
        return 1

    def type(self):  # noqa:  A003
        return 1

    def access(self):
        return 1

    def isUsed(self):
        return 1

    def isArgument(self):
        return 1

    def bufferAlignment(self):
        return 1

    def bufferDataSize(self):
        return 1

    def bufferDataType(self):
        return 1

    def threadgroupMemoryAlignment(self):
        return 1

    def threadgroupMemoryDataSize(self):
        return 1

    def textureType(self):
        return 1

    def textureDataType(self):
        return 1

    def isDepthTexture(self):
        return 1

    def arrayLength(self):
        return 1

    def objectPayloadAlignment(self):
        return 1

    def objectPayloadDataSize(self):
        return 1

    def tensorDataType(self):
        return 1

    def indexType(self):
        return 1


class TestMTLArgument(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLArgumentAccess)
        self.assertIsEnumType(Metal.MTLArgumentType)
        self.assertIsEnumType(Metal.MTLDataType)
        self.assertIsEnumType(Metal.MTLBindingType)

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
        self.assertEqual(Metal.MTLDataTypeBFloat, 121)
        self.assertEqual(Metal.MTLDataTypeBFloat2, 122)
        self.assertEqual(Metal.MTLDataTypeBFloat3, 123)
        self.assertEqual(Metal.MTLDataTypeBFloat4, 124)

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

        self.assertEqual(Metal.MTLBindingAccessReadOnly, 0)
        self.assertEqual(Metal.MTLBindingAccessReadWrite, 1)
        self.assertEqual(Metal.MTLBindingAccessWriteOnly, 2)
        self.assertEqual(
            Metal.MTLArgumentAccessReadOnly, Metal.MTLBindingAccessReadOnly
        )
        self.assertEqual(
            Metal.MTLArgumentAccessReadWrite, Metal.MTLBindingAccessReadWrite
        )
        self.assertEqual(
            Metal.MTLArgumentAccessWriteOnly, Metal.MTLBindingAccessWriteOnly
        )

        self.assertEqual(Metal.MTLBindingTypeBuffer, 0)
        self.assertEqual(Metal.MTLBindingTypeThreadgroupMemory, 1)
        self.assertEqual(Metal.MTLBindingTypeTexture, 2)
        self.assertEqual(Metal.MTLBindingTypeSampler, 3)
        self.assertEqual(Metal.MTLBindingTypeImageblockData, 16)
        self.assertEqual(Metal.MTLBindingTypeImageblock, 17)
        self.assertEqual(Metal.MTLBindingTypeVisibleFunctionTable, 24)
        self.assertEqual(Metal.MTLBindingTypePrimitiveAccelerationStructure, 25)
        self.assertEqual(Metal.MTLBindingTypeInstanceAccelerationStructure, 26)
        self.assertEqual(Metal.MTLBindingTypeIntersectionFunctionTable, 27)
        self.assertEqual(Metal.MTLBindingTypeObjectPayload, 34)

        self.assertIsEnumType(Metal.MTLIndexType)
        self.assertEqual(Metal.MTLIndexTypeUInt16, 0)
        self.assertEqual(Metal.MTLIndexTypeUInt32, 1)

    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLBinding")
        self.assertProtocolExists("MTLBufferBinding")
        self.assertProtocolExists("MTLThreadgroupBinding")
        self.assertProtocolExists("MTLTextureBinding")
        self.assertProtocolExists("MTLObjectPayloadBinding")

    @min_sdk_level("26.0")
    def test_protocols26_0(self):
        self.assertProtocolExists("MTLTensorBinding")

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(Metal.MTLArgument.alloc().init().isActive)

    @min_os_level("10.12")
    @expectedFailureIf(
        os_level_key("10.12") <= os_level_key(os_release()) < os_level_key("13.0")
    )
    def test_methods10_12(self):
        self.assertResultIsBOOL(Metal.MTLArgument.alloc().init().isDepthTexture)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(
            Metal.MTLPointerType.alloc().init().elementIsArgumentBuffer
        )
        self.assertResultIsBOOL(
            Metal.MTLTextureReferenceType.alloc().init().isDepthTexture
        )

    def test_protocol_methods(self):
        self.assertResultHasType(TestMTLArgumentHelper.type, objc._C_NSInteger)
        self.assertResultHasType(TestMTLArgumentHelper.access, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.index, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.index, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestMTLArgumentHelper.isUsed)
        self.assertResultIsBOOL(TestMTLArgumentHelper.isArgument)

        self.assertResultHasType(
            TestMTLArgumentHelper.bufferAlignment, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLArgumentHelper.bufferDataSize, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLArgumentHelper.bufferDataType, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLArgumentHelper.threadgroupMemoryAlignment, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLArgumentHelper.threadgroupMemoryDataSize, objc._C_NSUInteger
        )

        self.assertResultHasType(TestMTLArgumentHelper.textureType, objc._C_NSUInteger)
        self.assertResultHasType(
            TestMTLArgumentHelper.textureDataType, objc._C_NSUInteger
        )
        self.assertResultIsBOOL(TestMTLArgumentHelper.isDepthTexture)
        self.assertResultHasType(TestMTLArgumentHelper.arrayLength, objc._C_NSUInteger)

        self.assertResultHasType(
            TestMTLArgumentHelper.objectPayloadAlignment, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLArgumentHelper.objectPayloadDataSize, objc._C_NSUInteger
        )

        self.assertResultHasType(TestMTLArgumentHelper.tensorDataType, b"q")
        self.assertResultHasType(TestMTLArgumentHelper.indexType, b"Q")
