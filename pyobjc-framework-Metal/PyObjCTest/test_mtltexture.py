import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLTextureHelper(Metal.NSObject):
    def parentRelativeLevel(self):
        return 0

    def parentRelativeSlice(self):
        return 0

    def bufferOffset(self):
        return 0

    def bufferBytesPerRow(self):
        return 0

    def iosurfacePlane(self):
        return 0

    def textureType(self):
        return 0

    def pixelFormat(self):
        return 0

    def width(self):
        return 0

    def height(self):
        return 0

    def depth(self):
        return 0

    def mipmapLevelCount(self):
        return 0

    def sampleCount(self):
        return 0

    def arrayLength(self):
        return 0

    def usage(self):
        return 0

    def isShareable(self):
        return 0

    def isFramebufferOnly(self):
        return 0

    def allowGPUOptimizedContents(self):
        return 0

    def compressionType(self):
        return 0

    def gpuResourceID(self):
        return 0

    def getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_(
        self, a, b, c, d, e, f
    ):
        pass

    def replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_(
        self, a, b, c, d, e, f
    ):
        pass

    def getBytes_bytesPerRow_fromRegion_mipmapLevel_(self, a, b, c, d):
        pass

    def replaceRegion_mipmapLevel_withBytes_bytesPerRow_(self, a, b, c, d):
        pass

    def newTextureViewWithPixelFormat_(self, a):
        pass

    def newTextureViewWithPixelFormat_textureType_levels_slices_(self, a, b, c, d):
        pass

    def swizzle(self):
        return 1

    def firstMipmapInTail(self):
        return 1

    def tailSizeInBytes(self):
        return 1

    def isSparse(self):
        return 1


class TestMTLArgument(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLTextureSwizzle)
        self.assertIsEnumType(Metal.MTLTextureType)
        self.assertIsEnumType(Metal.MTLTextureUsage)
        self.assertIsEnumType(Metal.MTLTextureCompressionType)

    def test_constants(self):
        self.assertEqual(Metal.MTLTextureType1D, 0)
        self.assertEqual(Metal.MTLTextureType1DArray, 1)
        self.assertEqual(Metal.MTLTextureType2D, 2)
        self.assertEqual(Metal.MTLTextureType2DArray, 3)
        self.assertEqual(Metal.MTLTextureType2DMultisample, 4)
        self.assertEqual(Metal.MTLTextureTypeCube, 5)
        self.assertEqual(Metal.MTLTextureTypeCubeArray, 6)
        self.assertEqual(Metal.MTLTextureType3D, 7)
        self.assertEqual(Metal.MTLTextureType2DMultisampleArray, 8)
        self.assertEqual(Metal.MTLTextureTypeTextureBuffer, 9)

        self.assertEqual(Metal.MTLTextureSwizzleZero, 0)
        self.assertEqual(Metal.MTLTextureSwizzleOne, 1)
        self.assertEqual(Metal.MTLTextureSwizzleRed, 2)
        self.assertEqual(Metal.MTLTextureSwizzleGreen, 3)
        self.assertEqual(Metal.MTLTextureSwizzleBlue, 4)
        self.assertEqual(Metal.MTLTextureSwizzleAlpha, 5)

        self.assertEqual(Metal.MTLTextureUsageUnknown, 0x0000)
        self.assertEqual(Metal.MTLTextureUsageShaderRead, 0x0001)
        self.assertEqual(Metal.MTLTextureUsageShaderWrite, 0x0002)
        self.assertEqual(Metal.MTLTextureUsageRenderTarget, 0x0004)
        self.assertEqual(Metal.MTLTextureUsagePixelFormatView, 0x0010)
        self.assertEqual(Metal.MTLTextureUsageShaderAtomic, 0x0020)

        self.assertEqual(Metal.MTLTextureCompressionTypeLossless, 0)
        self.assertEqual(Metal.MTLTextureCompressionTypeLossy, 1)

    def test_structs(self):
        v = Metal.MTLTextureSwizzleChannels()
        self.assertEqual(v.red, 0)
        self.assertEqual(v.green, 0)
        self.assertEqual(v.blue, 0)
        self.assertEqual(v.alpha, 0)
        self.assertPickleRoundTrips(v)

    @min_os_level("10.15")
    def test_functions(self):
        v = Metal.MTLTextureSwizzleChannelsMake(0, 1, 2, 3)
        self.assertIsInstance(v, Metal.MTLTextureSwizzleChannels)
        self.assertEqual(v, (0, 1, 2, 3))

        v = Metal.MTLTextureSwizzleChannelsDefault
        self.assertIsInstance(v, Metal.MTLTextureSwizzleChannels)
        self.assertEqual(
            v,
            (
                Metal.MTLTextureSwizzleRed,
                Metal.MTLTextureSwizzleGreen,
                Metal.MTLTextureSwizzleBlue,
                Metal.MTLTextureSwizzleAlpha,
            ),
        )

    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLTexture")

    def test_methods(self):
        self.assertResultHasType(
            TestMTLTextureHelper.parentRelativeLevel, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLTextureHelper.parentRelativeSlice, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMTLTextureHelper.bufferOffset, objc._C_NSUInteger)
        self.assertResultHasType(
            TestMTLTextureHelper.bufferBytesPerRow, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMTLTextureHelper.iosurfacePlane, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLTextureHelper.textureType, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLTextureHelper.pixelFormat, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLTextureHelper.width, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLTextureHelper.height, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLTextureHelper.depth, objc._C_NSUInteger)
        self.assertResultHasType(
            TestMTLTextureHelper.mipmapLevelCount, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMTLTextureHelper.sampleCount, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLTextureHelper.arrayLength, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLTextureHelper.usage, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLTextureHelper.isShareable, objc._C_NSBOOL)
        self.assertResultHasType(TestMTLTextureHelper.isFramebufferOnly, objc._C_NSBOOL)
        self.assertResultHasType(
            TestMTLTextureHelper.allowGPUOptimizedContents, objc._C_NSBOOL
        )
        self.assertResultHasType(TestMTLTextureHelper.compressionType, objc._C_NSInteger)
        self.assertResultHasType(
            TestMTLTextureHelper.gpuResourceID, Metal.MTLResourceID.__typestr__
        )

        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            0,
            b"o^v",
        )
        # XXX: Buffer size?
        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            3,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            0,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            3,
            b"n^v",
        )
        # XXX: Buffer size?
        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_fromRegion_mipmapLevel_,
            0,
            b"o^v",
        )
        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_fromRegion_mipmapLevel_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_fromRegion_mipmapLevel_,
            2,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.getBytes_bytesPerRow_fromRegion_mipmapLevel_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_withBytes_bytesPerRow_,
            0,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_withBytes_bytesPerRow_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_withBytes_bytesPerRow_,
            2,
            b"n^v",
        )
        self.assertArgHasType(
            TestMTLTextureHelper.replaceRegion_mipmapLevel_withBytes_bytesPerRow_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_, 0, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            2,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            3,
            Metal.NSRange.__typestr__,
        )

        self.assertResultHasType(
            TestMTLTextureHelper.swizzle, Metal.MTLTextureSwizzleChannels.__typestr__
        )

        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            2,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTLTextureHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            3,
            Metal.NSRange.__typestr__,
        )

        self.assertResultHasType(
            TestMTLTextureHelper.firstMipmapInTail, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMTLTextureHelper.tailSizeInBytes, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestMTLTextureHelper.isSparse)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(
            Metal.MTLTextureDescriptor.alloc().init().allowGPUOptimizedContents
        )
        self.assertArgIsBOOL(
            Metal.MTLTextureDescriptor.alloc().init().setAllowGPUOptimizedContents_, 0
        )
