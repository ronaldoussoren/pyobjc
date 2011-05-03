
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVPixelBuffer (TestCase):
    def testConstants(self):
        self.assertEqual(kCVPixelFormatType_1Monochrome, 0x00000001)
        self.assertEqual(kCVPixelFormatType_2Indexed, 0x00000002)
        self.assertEqual(kCVPixelFormatType_4Indexed, 0x00000004)
        self.assertEqual(kCVPixelFormatType_8Indexed, 0x00000008)
        self.assertEqual(kCVPixelFormatType_1IndexedGray_WhiteIsZero, 0x00000021)
        self.assertEqual(kCVPixelFormatType_2IndexedGray_WhiteIsZero, 0x00000022)
        self.assertEqual(kCVPixelFormatType_4IndexedGray_WhiteIsZero, 0x00000024)
        self.assertEqual(kCVPixelFormatType_8IndexedGray_WhiteIsZero, 0x00000028)
        self.assertEqual(kCVPixelFormatType_16BE555, 0x00000010)
        self.assertEqual(kCVPixelFormatType_16LE555, fourcc(b'L555'))
        self.assertEqual(kCVPixelFormatType_16LE5551, fourcc(b'5551'))
        self.assertEqual(kCVPixelFormatType_16BE565, fourcc(b'B565'))
        self.assertEqual(kCVPixelFormatType_16LE565, fourcc(b'L565'))
        self.assertEqual(kCVPixelFormatType_24RGB, 0x00000018)
        self.assertEqual(kCVPixelFormatType_24BGR, fourcc(b'24BG'))
        self.assertEqual(kCVPixelFormatType_32ARGB, 0x00000020)
        self.assertEqual(kCVPixelFormatType_32BGRA, fourcc(b'BGRA'))
        self.assertEqual(kCVPixelFormatType_32ABGR, fourcc(b'ABGR'))
        self.assertEqual(kCVPixelFormatType_32RGBA, fourcc(b'RGBA'))
        self.assertEqual(kCVPixelFormatType_64ARGB, fourcc(b'b64a'))
        self.assertEqual(kCVPixelFormatType_48RGB, fourcc(b'b48r'))
        self.assertEqual(kCVPixelFormatType_32AlphaGray, fourcc(b'b32a'))
        self.assertEqual(kCVPixelFormatType_16Gray, fourcc(b'b16g'))
        self.assertEqual(kCVPixelFormatType_422YpCbCr8, fourcc(b'2vuy'))
        self.assertEqual(kCVPixelFormatType_4444YpCbCrA8, fourcc(b'v408'))
        self.assertEqual(kCVPixelFormatType_4444YpCbCrA8R, fourcc(b'r408'))
        self.assertEqual(kCVPixelFormatType_444YpCbCr8, fourcc(b'v308'))
        self.assertEqual(kCVPixelFormatType_422YpCbCr16, fourcc(b'v216'))
        self.assertEqual(kCVPixelFormatType_422YpCbCr10, fourcc(b'v210'))
        self.assertEqual(kCVPixelFormatType_444YpCbCr10, fourcc(b'v410'))
        self.assertEqual(kCVPixelFormatType_420YpCbCr8Planar, fourcc(b'y420'))

        self.assertIsInstance(kCVPixelBufferPixelFormatTypeKey, unicode)
        self.assertIsInstance(kCVPixelBufferMemoryAllocatorKey, unicode)
        self.assertIsInstance(kCVPixelBufferWidthKey, unicode)
        self.assertIsInstance(kCVPixelBufferHeightKey, unicode)
        self.assertIsInstance(kCVPixelBufferExtendedPixelsLeftKey, unicode)
        self.assertIsInstance(kCVPixelBufferExtendedPixelsTopKey, unicode)
        self.assertIsInstance(kCVPixelBufferExtendedPixelsRightKey, unicode)
        self.assertIsInstance(kCVPixelBufferExtendedPixelsBottomKey, unicode)
        self.assertIsInstance(kCVPixelBufferBytesPerRowAlignmentKey, unicode)
        self.assertIsInstance(kCVPixelBufferCGBitmapContextCompatibilityKey, unicode)
        self.assertIsInstance(kCVPixelBufferCGImageCompatibilityKey, unicode)
        self.assertIsInstance(kCVPixelBufferOpenGLCompatibilityKey, unicode)

    def testTypes(self):
        self.assertIsCFType(CVPixelBufferRef)

    def testStructures(self):
        v = CVPlanarComponentInfo()
        self.assertIsInstance(v.offset, (int, long))
        self.assertIsInstance(v.rowBytes, (int, long))

        v = CVPlanarPixelBufferInfo_YCbCrPlanar()
        self.assertIsInstance(v.componentInfoY, CVPlanarComponentInfo)
        self.assertIsInstance(v.componentInfoCb, CVPlanarComponentInfo)
        self.assertIsInstance(v.componentInfoCr, CVPlanarComponentInfo)

    def testFunctions(self):
        self.assertIsInstance(CVPixelBufferGetTypeID(), (int, long))


        buf = self.makeBuffer()
        self.assertIsInstance(buf, CVPixelBufferRef)


        v = CVPixelBufferRetain(buf)
        self.assertTrue(v is buf)
        CVPixelBufferRelease(v)

        self.assertArgIsOut(CVPixelBufferCreateResolvedAttributesDictionary, 2)
        rv, v = CVPixelBufferCreateResolvedAttributesDictionary(None, [], None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(v, CFDictionaryRef)



        v = CVPixelBufferGetWidth(buf)
        self.assertIsInstance(v, (int, long))

        v = CVPixelBufferGetHeight(buf)
        self.assertIsInstance(v, (int, long))

        v = CVPixelBufferGetPixelFormatType(buf)
        self.assertIsInstance(v, (int, long))

        rv = CVPixelBufferLockBaseAddress(buf, 0)
        self.assertEqual(rv, 0)

        self.assertResultHasType(CVPixelBufferGetBaseAddress, b'^v')
        self.assertResultIsVariableSize(CVPixelBufferGetBaseAddress)
        v = CVPixelBufferGetBaseAddress(buf)
        self.assertIsInstance(v, objc.varlist)
        self.assertIsInstance(v[0], str)

        self.assertResultHasType(CVPixelBufferGetBaseAddressOfPlane, b'^v')
        self.assertResultIsVariableSize(CVPixelBufferGetBaseAddressOfPlane)
        v = CVPixelBufferGetBaseAddressOfPlane(buf, 0)
        if v is not objc.NULL:
            self.assertIsInstance(v, objc.varlist)
            self.assertIsInstance(v[0], str)

        rv = CVPixelBufferUnlockBaseAddress(buf, 0)
        self.assertEqual(rv, 0)

        v = CVPixelBufferGetBytesPerRow(buf)
        self.assertIsInstance(v, (int, long))

        v = CVPixelBufferGetDataSize(buf)
        self.assertIsInstance(v, (int, long))

        v = CVPixelBufferGetPlaneCount(buf)
        self.assertIsInstance(v, (int, long))

        v = CVPixelBufferGetWidthOfPlane(buf, 0)
        self.assertIsInstance(v, (int, long))

        v = CVPixelBufferGetHeightOfPlane(buf, 0)
        self.assertIsInstance(v, (int, long))

        v = CVPixelBufferGetBytesPerRowOfPlane(buf, 0)
        self.assertIsInstance(v, (int, long))

        self.assertArgIsOut(CVPixelBufferGetExtendedPixels, 1)
        self.assertArgIsOut(CVPixelBufferGetExtendedPixels, 2)
        self.assertArgIsOut(CVPixelBufferGetExtendedPixels, 3)
        self.assertArgIsOut(CVPixelBufferGetExtendedPixels, 4)
        v = CVPixelBufferGetExtendedPixels(buf, None, None, None, None)
        self.assertEqual(len(v), 4)
        for i in range(4):
            self.assertIsInstance(v[i], (int, long))

        rv = CVPixelBufferFillExtendedPixels(buf)
        self.assertIsInstance(rv, (int, long))



    def testManual(self):
        self.fail("CVPixelBufferCreate requires manual wrapper") 
        self.fail("CVPixelBufferCreateWithBytes requires manual wrapper")
        self.fail("CVPixelBufferCreateWithPlanarBytes requires manual wrapper")




    def makeBuffer(self):
        # Helper function for creating a buffer, needed until we write the
        # manual wrappers for creating a buffer without a pool
        rv, pool = CVPixelBufferPoolCreate(None, {
                kCVPixelBufferPoolMinimumBufferCountKey: 1,
                kCVPixelBufferPoolMaximumBufferAgeKey: 300,
            }, {
                kCVPixelBufferWidthKey: 100,
                kCVPixelBufferHeightKey: 100,
                kCVPixelBufferPixelFormatTypeKey: kCVPixelFormatType_32ARGB,
            }, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(pool, CVPixelBufferPoolRef)

        rv, image = CVPixelBufferPoolCreatePixelBuffer(None, pool, None)
        self.assertEqual(rv, 0)
        return image

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCVPixelBufferLock_ReadOnly, 1)

        self.assertIsInstance(kCVPixelBufferPlaneAlignmentKey, unicode)
        self.assertIsInstance(kCVPixelBufferIOSurfacePropertiesKey, unicode)
        self.assertIsInstance(kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey, unicode)
        self.assertIsInstance(kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey, unicode)
        self.assertIsInstance(kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey, unicode)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.assertResultHasType(CVPixelBufferGetIOSurface, b'^{__IOSurfaceRef=}')
        self.assertArgHasType(CVPixelBufferGetIOSurface, 0, b'^{__CVPixelBuffer=}')
        self.assertArgHasType(CVPixelBufferCreateWithIOSurface, 1, b'^{__IOSurfaceRef=}')
        self.assertArgIsOut(CVPixelBufferCreateWithIOSurface, 3)



if __name__ == "__main__":
    main()
