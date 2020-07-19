import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLArgumentHelper(Metal.NSObject):
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

    def test_structs(self):
        v = Metal.MTLTextureSwizzleChannels()
        self.assertEqual(v.red, 0)
        self.assertEqual(v.green, 0)
        self.assertEqual(v.blue, 0)
        self.assertEqual(v.alpha, 0)

    @min_sdk_level("10.15")
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
        objc.protocolNamed("MTLTexture")

    def test_methods(self):
        self.assertResultHasType(
            TestMTLArgumentHelper.parentRelativeLevel, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLArgumentHelper.parentRelativeSlice, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMTLArgumentHelper.bufferOffset, objc._C_NSUInteger)
        self.assertResultHasType(
            TestMTLArgumentHelper.bufferBytesPerRow, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLArgumentHelper.iosurfacePlane, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMTLArgumentHelper.textureType, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.pixelFormat, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.width, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.height, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.depth, objc._C_NSUInteger)
        self.assertResultHasType(
            TestMTLArgumentHelper.mipmapLevelCount, objc._C_NSUInteger
        )
        self.assertResultHasType(TestMTLArgumentHelper.sampleCount, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.arrayLength, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.usage, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLArgumentHelper.isShareable, objc._C_NSBOOL)
        self.assertResultHasType(
            TestMTLArgumentHelper.isFramebufferOnly, objc._C_NSBOOL
        )
        self.assertResultHasType(
            TestMTLArgumentHelper.allowGPUOptimizedContents, objc._C_NSBOOL
        )

        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            0,
            b"o^v",
        )
        # XXX: Buffer size?
        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            3,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_bytesPerImage_fromRegion_mipmapLevel_slice_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            0,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            3,
            b"n^v",
        )
        # XXX: Buffer size?
        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_slice_withBytes_bytesPerRow_bytesPerImage_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_fromRegion_mipmapLevel_,
            0,
            b"o^v",
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_fromRegion_mipmapLevel_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_fromRegion_mipmapLevel_,
            2,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.getBytes_bytesPerRow_fromRegion_mipmapLevel_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_withBytes_bytesPerRow_,
            0,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_withBytes_bytesPerRow_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_withBytes_bytesPerRow_,
            2,
            b"n^v",
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.replaceRegion_mipmapLevel_withBytes_bytesPerRow_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_, 0, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            2,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            3,
            Metal.NSRange.__typestr__,
        )

        self.assertResultHasType(
            TestMTLArgumentHelper.swizzle, Metal.MTLTextureSwizzleChannels.__typestr__
        )

        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            2,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTLArgumentHelper.newTextureViewWithPixelFormat_textureType_levels_slices_,
            3,
            Metal.NSRange.__typestr__,
        )

        self.assertResultHasType(
            TestMTLArgumentHelper.firstMipmapInTail, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLArgumentHelper.tailSizeInBytes, objc._C_NSUInteger
        )
        self.assertResultIsBOOL(TestMTLArgumentHelper.isSparse)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(
            Metal.MTLTextureDescriptor.alloc().init().allowGPUOptimizedContents
        )
        self.assertArgIsBOOL(
            Metal.MTLTextureDescriptor.alloc().init().setAllowGPUOptimizedContents_, 0
        )
