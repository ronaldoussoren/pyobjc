from PyObjCTools.TestSupport import *

import Metal


class TestMTLArgument(TestCase):
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
        self.assertEqual(Metal.MTLDataTypeRenderPipeline, 78)
        self.assertEqual(Metal.MTLDataTypeIndirectCommandBuffer, 80)

        self.assertEqual(Metal.MTLArgumentTypeBuffer, 0)
        self.assertEqual(Metal.MTLArgumentTypeThreadgroupMemory, 1)
        self.assertEqual(Metal.MTLArgumentTypeTexture, 2)
        self.assertEqual(Metal.MTLArgumentTypeSampler, 3)

        self.assertEqual(Metal.MTLArgumentAccessReadOnly, 0)
        self.assertEqual(Metal.MTLArgumentAccessReadWrite, 1)
        self.assertEqual(Metal.MTLArgumentAccessWriteOnly, 2)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(Metal.MTLArgument.alloc().init().isActive)

    @expectedFailure  # Documented, but not actually working..
    @min_os_level("10.12")
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
