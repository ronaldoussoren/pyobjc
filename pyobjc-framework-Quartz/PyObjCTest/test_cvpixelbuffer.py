from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure, fourcc
import Quartz
import objc


class TestCVPixelBuffer(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCVPixelFormatType_1Monochrome, 0x00000001)
        self.assertEqual(Quartz.kCVPixelFormatType_2Indexed, 0x00000002)
        self.assertEqual(Quartz.kCVPixelFormatType_4Indexed, 0x00000004)
        self.assertEqual(Quartz.kCVPixelFormatType_8Indexed, 0x00000008)
        self.assertEqual(Quartz.kCVPixelFormatType_1IndexedGray_WhiteIsZero, 0x00000021)
        self.assertEqual(Quartz.kCVPixelFormatType_2IndexedGray_WhiteIsZero, 0x00000022)
        self.assertEqual(Quartz.kCVPixelFormatType_4IndexedGray_WhiteIsZero, 0x00000024)
        self.assertEqual(Quartz.kCVPixelFormatType_8IndexedGray_WhiteIsZero, 0x00000028)
        self.assertEqual(Quartz.kCVPixelFormatType_16BE555, 0x00000010)
        self.assertEqual(Quartz.kCVPixelFormatType_16LE555, fourcc(b"L555"))
        self.assertEqual(Quartz.kCVPixelFormatType_16LE5551, fourcc(b"5551"))
        self.assertEqual(Quartz.kCVPixelFormatType_16BE565, fourcc(b"B565"))
        self.assertEqual(Quartz.kCVPixelFormatType_16LE565, fourcc(b"L565"))
        self.assertEqual(Quartz.kCVPixelFormatType_24RGB, 0x00000018)
        self.assertEqual(Quartz.kCVPixelFormatType_24BGR, fourcc(b"24BG"))
        self.assertEqual(Quartz.kCVPixelFormatType_32ARGB, 0x00000020)
        self.assertEqual(Quartz.kCVPixelFormatType_32BGRA, fourcc(b"BGRA"))
        self.assertEqual(Quartz.kCVPixelFormatType_32ABGR, fourcc(b"ABGR"))
        self.assertEqual(Quartz.kCVPixelFormatType_32RGBA, fourcc(b"RGBA"))
        self.assertEqual(Quartz.kCVPixelFormatType_64ARGB, fourcc(b"b64a"))
        self.assertEqual(Quartz.kCVPixelFormatType_48RGB, fourcc(b"b48r"))
        self.assertEqual(Quartz.kCVPixelFormatType_32AlphaGray, fourcc(b"b32a"))
        self.assertEqual(Quartz.kCVPixelFormatType_16Gray, fourcc(b"b16g"))
        self.assertEqual(Quartz.kCVPixelFormatType_422YpCbCr8, fourcc(b"2vuy"))
        self.assertEqual(Quartz.kCVPixelFormatType_4444YpCbCrA8, fourcc(b"v408"))
        self.assertEqual(Quartz.kCVPixelFormatType_4444YpCbCrA8R, fourcc(b"r408"))
        self.assertEqual(Quartz.kCVPixelFormatType_4444AYpCbCr8, fourcc(b"y408"))
        self.assertEqual(Quartz.kCVPixelFormatType_4444AYpCbCr16, fourcc(b"y416"))
        self.assertEqual(Quartz.kCVPixelFormatType_444YpCbCr8, fourcc(b"v308"))
        self.assertEqual(Quartz.kCVPixelFormatType_422YpCbCr16, fourcc(b"v216"))
        self.assertEqual(Quartz.kCVPixelFormatType_422YpCbCr10, fourcc(b"v210"))
        self.assertEqual(Quartz.kCVPixelFormatType_444YpCbCr10, fourcc(b"v410"))
        self.assertEqual(Quartz.kCVPixelFormatType_420YpCbCr8Planar, fourcc(b"y420"))
        self.assertEqual(
            Quartz.kCVPixelFormatType_420YpCbCr8PlanarFullRange, fourcc(b"f420")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_422YpCbCr_4A_8BiPlanar, fourcc(b"a2vy")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange, fourcc(b"420v")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_420YpCbCr8BiPlanarFullRange, fourcc(b"420f")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_422YpCbCr8BiPlanarVideoRange, fourcc(b"422v")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_422YpCbCr8BiPlanarFullRange, fourcc(b"422f")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_444YpCbCr8BiPlanarVideoRange, fourcc(b"444v")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_444YpCbCr8BiPlanarFullRange, fourcc(b"444f")
        )

        self.assertEqual(Quartz.kCVPixelFormatType_422YpCbCr8_yuvs, fourcc(b"yuvs"))
        self.assertEqual(Quartz.kCVPixelFormatType_422YpCbCr8FullRange, fourcc(b"yuvf"))
        self.assertEqual(Quartz.kCVPixelFormatType_OneComponent8, fourcc(b"L008"))
        self.assertEqual(Quartz.kCVPixelFormatType_TwoComponent8, fourcc(b"2C08"))
        self.assertEqual(Quartz.kCVPixelFormatType_OneComponent16Half, fourcc(b"L00h"))
        self.assertEqual(Quartz.kCVPixelFormatType_OneComponent32Float, fourcc(b"L00f"))
        self.assertEqual(Quartz.kCVPixelFormatType_TwoComponent16Half, fourcc(b"2C0h"))
        self.assertEqual(Quartz.kCVPixelFormatType_TwoComponent32Float, fourcc(b"2C0f"))
        self.assertEqual(Quartz.kCVPixelFormatType_64RGBAHalf, fourcc(b"RGhA"))
        self.assertEqual(Quartz.kCVPixelFormatType_128RGBAFloat, fourcc(b"RGfA"))
        self.assertEqual(
            Quartz.kCVPixelFormatType_30RGBLEPackedWideGamut, fourcc(b"w30r")
        )
        self.assertEqual(Quartz.kCVPixelFormatType_ARGB2101010LEPacked, fourcc(b"l10r"))

        self.assertEqual(Quartz.kCVPixelFormatType_OneComponent10, fourcc(b"L010"))
        self.assertEqual(Quartz.kCVPixelFormatType_OneComponent12, fourcc(b"L012"))
        self.assertEqual(Quartz.kCVPixelFormatType_OneComponent16, fourcc(b"L016"))
        self.assertEqual(Quartz.kCVPixelFormatType_TwoComponent16, fourcc(b"2C16"))

        self.assertEqual(Quartz.kCVPixelFormatType_14Bayer_GRBG, fourcc(b"grb4"))
        self.assertEqual(Quartz.kCVPixelFormatType_14Bayer_RGGB, fourcc(b"rgg4"))
        self.assertEqual(Quartz.kCVPixelFormatType_14Bayer_BGGR, fourcc(b"bgg4"))
        self.assertEqual(Quartz.kCVPixelFormatType_14Bayer_GBRG, fourcc(b"gbr4"))

        self.assertIsInstance(Quartz.kCVPixelBufferPixelFormatTypeKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferMemoryAllocatorKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferWidthKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferHeightKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferExtendedPixelsLeftKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferExtendedPixelsTopKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferExtendedPixelsRightKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferExtendedPixelsBottomKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferBytesPerRowAlignmentKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferCGBitmapContextCompatibilityKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferCGImageCompatibilityKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferOpenGLCompatibilityKey, str)

        self.assertEqual(Quartz.kCVPixelFormatType_DisparityFloat16, fourcc(b"hdis"))
        self.assertEqual(Quartz.kCVPixelFormatType_DisparityFloat32, fourcc(b"fdis"))
        self.assertEqual(Quartz.kCVPixelFormatType_DepthFloat16, fourcc(b"hdep"))
        self.assertEqual(Quartz.kCVPixelFormatType_DepthFloat32, fourcc(b"fdep"))
        self.assertEqual(
            Quartz.kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange, fourcc(b"x420")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange, fourcc(b"x422")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_444YpCbCr10BiPlanarVideoRange, fourcc(b"x444")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_420YpCbCr10BiPlanarFullRange, fourcc(b"xf20")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_422YpCbCr10BiPlanarFullRange, fourcc(b"xf22")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_444YpCbCr10BiPlanarFullRange, fourcc(b"xf44")
        )
        self.assertEqual(
            Quartz.kCVPixelFormatType_420YpCbCr8VideoRange_8A_TriPlanar, fourcc(b"v0a8")
        )
        self.assertEqual(Quartz.kCVPixelFormatType_16VersatileBayer, fourcc(b"bp16"))
        self.assertEqual(
            Quartz.kCVPixelFormatType_64RGBA_DownscaledProResRAW, fourcc(b"bp64")
        )

        self.assertEqual(Quartz.kCVVersatileBayer_BayerPattern_RGGB, 0)
        self.assertEqual(Quartz.kCVVersatileBayer_BayerPattern_GRBG, 1)
        self.assertEqual(Quartz.kCVVersatileBayer_BayerPattern_GBRG, 2)
        self.assertEqual(Quartz.kCVVersatileBayer_BayerPattern_BGGR, 3)

    def testTypes(self):
        self.assertIsCFType(Quartz.CVPixelBufferRef)

    def testStructures(self):
        v = Quartz.CVPlanarComponentInfo()
        self.assertIsInstance(v.offset, int)
        self.assertIsInstance(v.rowBytes, int)

        # XXX: Type needs more work (unconstrained C array) in componentInfo:
        v = Quartz.CVPlanarPixelBufferInfo()
        self.assertEqual(v.componentInfo, None)

        v = Quartz.CVPlanarPixelBufferInfo_YCbCrPlanar()
        self.assertEqual(v.componentInfoY, Quartz.CVPlanarComponentInfo())
        self.assertEqual(v.componentInfoCb, Quartz.CVPlanarComponentInfo())
        self.assertEqual(v.componentInfoCr, Quartz.CVPlanarComponentInfo())

        v = Quartz.CVPlanarPixelBufferInfo_YCbCrBiPlanar()
        self.assertEqual(v.componentInfoY, Quartz.CVPlanarComponentInfo())
        self.assertEqual(v.componentInfoCbCr, Quartz.CVPlanarComponentInfo())

    def testFunctions(self):
        self.assertIsInstance(Quartz.CVPixelBufferGetTypeID(), int)

        buf = self.makeBuffer()
        self.assertIsInstance(buf, Quartz.CVPixelBufferRef)

        v = Quartz.CVPixelBufferRetain(buf)
        self.assertTrue(v is buf)
        Quartz.CVPixelBufferRelease(v)

        self.assertArgIsOut(Quartz.CVPixelBufferCreateResolvedAttributesDictionary, 2)
        rv, v = Quartz.CVPixelBufferCreateResolvedAttributesDictionary(None, [], None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(v, Quartz.CFDictionaryRef)

        v = Quartz.CVPixelBufferGetWidth(buf)
        self.assertIsInstance(v, int)

        v = Quartz.CVPixelBufferGetHeight(buf)
        self.assertIsInstance(v, int)

        v = Quartz.CVPixelBufferGetPixelFormatType(buf)
        self.assertIsInstance(v, int)

        rv = Quartz.CVPixelBufferLockBaseAddress(buf, 0)
        self.assertEqual(rv, 0)

        self.assertResultHasType(Quartz.CVPixelBufferGetBaseAddress, b"^v")
        self.assertResultIsVariableSize(Quartz.CVPixelBufferGetBaseAddress)
        v = Quartz.CVPixelBufferGetBaseAddress(buf)
        self.assertIsInstance(v, objc.varlist)
        self.assertIsInstance(v[0], bytes)

        self.assertResultHasType(Quartz.CVPixelBufferGetBaseAddressOfPlane, b"^v")
        self.assertResultIsVariableSize(Quartz.CVPixelBufferGetBaseAddressOfPlane)
        v = Quartz.CVPixelBufferGetBaseAddressOfPlane(buf, 0)
        if v is not objc.NULL:
            self.assertIsInstance(v, objc.varlist)
            self.assertIsInstance(v[0], bytes)

        rv = Quartz.CVPixelBufferUnlockBaseAddress(buf, 0)
        self.assertEqual(rv, 0)

        v = Quartz.CVPixelBufferGetWidth(buf)
        self.assertIsInstance(v, int)

        v = Quartz.CVPixelBufferGetHeight(buf)
        self.assertIsInstance(v, int)

        v = Quartz.CVPixelBufferGetBytesPerRow(buf)
        self.assertIsInstance(v, int)

        v = Quartz.CVPixelBufferGetDataSize(buf)
        self.assertIsInstance(v, int)

        self.assertResultIsBOOL(Quartz.CVPixelBufferIsPlanar)

        v = Quartz.CVPixelBufferGetPlaneCount(buf)
        self.assertIsInstance(v, int)

        v = Quartz.CVPixelBufferGetWidthOfPlane(buf, 0)
        self.assertIsInstance(v, int)

        v = Quartz.CVPixelBufferGetHeightOfPlane(buf, 0)
        self.assertIsInstance(v, int)

        v = Quartz.CVPixelBufferGetBytesPerRowOfPlane(buf, 0)
        self.assertIsInstance(v, int)

        self.assertArgIsOut(Quartz.CVPixelBufferGetExtendedPixels, 1)
        self.assertArgIsOut(Quartz.CVPixelBufferGetExtendedPixels, 2)
        self.assertArgIsOut(Quartz.CVPixelBufferGetExtendedPixels, 3)
        self.assertArgIsOut(Quartz.CVPixelBufferGetExtendedPixels, 4)
        v = Quartz.CVPixelBufferGetExtendedPixels(buf, None, None, None, None)
        self.assertEqual(len(v), 4)
        for i in range(4):
            self.assertIsInstance(v[i], int)

        rv = Quartz.CVPixelBufferFillExtendedPixels(buf)
        self.assertIsInstance(rv, int)

    @expectedFailure
    def testManual(self):
        self.fail("CVPixelBufferCreate requires manual wrapper")
        self.fail("CVPixelBufferCreateWithBytes requires manual wrapper")
        self.fail("CVPixelBufferCreateWithPlanarBytes requires manual wrapper")

    def makeBuffer(self):
        # Helper function for creating a buffer, needed until we write the
        # manual wrappers for creating a buffer without a pool
        rv, pool = Quartz.CVPixelBufferPoolCreate(
            None,
            {
                Quartz.kCVPixelBufferPoolMinimumBufferCountKey: 1,
                Quartz.kCVPixelBufferPoolMaximumBufferAgeKey: 300,
            },
            {
                Quartz.kCVPixelBufferWidthKey: 100,
                Quartz.kCVPixelBufferHeightKey: 100,
                Quartz.kCVPixelBufferPixelFormatTypeKey: Quartz.kCVPixelFormatType_32ARGB,
            },
            None,
        )
        self.assertEqual(rv, 0)
        self.assertIsInstance(pool, Quartz.CVPixelBufferPoolRef)

        rv, image = Quartz.CVPixelBufferPoolCreatePixelBuffer(None, pool, None)
        self.assertEqual(rv, 0)
        return image

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Quartz.kCVPixelBufferLock_ReadOnly, 1)

        self.assertIsInstance(Quartz.kCVPixelBufferPlaneAlignmentKey, str)
        self.assertIsInstance(Quartz.kCVPixelBufferIOSurfacePropertiesKey, str)
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey, str
        )
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey, str
        )
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey, str
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCVPixelBufferMetalCompatibilityKey, str)
        self.assertIsInstance(
            Quartz.kCVPixelBufferOpenGLTextureCacheCompatibilityKey, str
        )

    @min_os_level("10.6")
    def testFunctions10_6(self):
        self.assertResultHasType(Quartz.CVPixelBufferGetIOSurface, b"^{__IOSurface=}")
        self.assertArgHasType(Quartz.CVPixelBufferGetIOSurface, 0, b"^{__CVBuffer=}")
        self.assertArgHasType(
            Quartz.CVPixelBufferCreateWithIOSurface, 1, b"^{__IOSurface=}"
        )
        self.assertArgIsOut(Quartz.CVPixelBufferCreateWithIOSurface, 3)
