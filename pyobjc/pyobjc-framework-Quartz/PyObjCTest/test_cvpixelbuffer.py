
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *

class TestCVPixelBuffer (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCVPixelFormatType_1Monochrome, 0x00000001)
        self.failUnlessEqual(kCVPixelFormatType_2Indexed, 0x00000002)
        self.failUnlessEqual(kCVPixelFormatType_4Indexed, 0x00000004)
        self.failUnlessEqual(kCVPixelFormatType_8Indexed, 0x00000008)
        self.failUnlessEqual(kCVPixelFormatType_1IndexedGray_WhiteIsZero, 0x00000021)
        self.failUnlessEqual(kCVPixelFormatType_2IndexedGray_WhiteIsZero, 0x00000022)
        self.failUnlessEqual(kCVPixelFormatType_4IndexedGray_WhiteIsZero, 0x00000024)
        self.failUnlessEqual(kCVPixelFormatType_8IndexedGray_WhiteIsZero, 0x00000028)
        self.failUnlessEqual(kCVPixelFormatType_16BE555, 0x00000010)
        self.failUnlessEqual(kCVPixelFormatType_16LE555, fourcc('L555'))
        self.failUnlessEqual(kCVPixelFormatType_16LE5551, fourcc('5551'))
        self.failUnlessEqual(kCVPixelFormatType_16BE565, fourcc('B565'))
        self.failUnlessEqual(kCVPixelFormatType_16LE565, fourcc('L565'))
        self.failUnlessEqual(kCVPixelFormatType_24RGB, 0x00000018)
        self.failUnlessEqual(kCVPixelFormatType_24BGR, fourcc('24BG'))
        self.failUnlessEqual(kCVPixelFormatType_32ARGB, 0x00000020)
        self.failUnlessEqual(kCVPixelFormatType_32BGRA, fourcc('BGRA'))
        self.failUnlessEqual(kCVPixelFormatType_32ABGR, fourcc('ABGR'))
        self.failUnlessEqual(kCVPixelFormatType_32RGBA, fourcc('RGBA'))
        self.failUnlessEqual(kCVPixelFormatType_64ARGB, fourcc('b64a'))
        self.failUnlessEqual(kCVPixelFormatType_48RGB, fourcc('b48r'))
        self.failUnlessEqual(kCVPixelFormatType_32AlphaGray, fourcc('b32a'))
        self.failUnlessEqual(kCVPixelFormatType_16Gray, fourcc('b16g'))
        self.failUnlessEqual(kCVPixelFormatType_422YpCbCr8, fourcc('2vuy'))
        self.failUnlessEqual(kCVPixelFormatType_4444YpCbCrA8, fourcc('v408'))
        self.failUnlessEqual(kCVPixelFormatType_4444YpCbCrA8R, fourcc('r408'))
        self.failUnlessEqual(kCVPixelFormatType_444YpCbCr8, fourcc('v308'))
        self.failUnlessEqual(kCVPixelFormatType_422YpCbCr16, fourcc('v216'))
        self.failUnlessEqual(kCVPixelFormatType_422YpCbCr10, fourcc('v210'))
        self.failUnlessEqual(kCVPixelFormatType_444YpCbCr10, fourcc('v410'))
        self.failUnlessEqual(kCVPixelFormatType_420YpCbCr8Planar, fourcc('y420'))

        self.failUnlessIsInstance(kCVPixelBufferPixelFormatTypeKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferMemoryAllocatorKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferWidthKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferHeightKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferExtendedPixelsLeftKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferExtendedPixelsTopKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferExtendedPixelsRightKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferExtendedPixelsBottomKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferBytesPerRowAlignmentKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferCGBitmapContextCompatibilityKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferCGImageCompatibilityKey, unicode)
        self.failUnlessIsInstance(kCVPixelBufferOpenGLCompatibilityKey, unicode)

    def testTypes(self):
        self.failUnlessIsCFType(CVPixelBufferRef)

    def testStructures(self):
        v = CVPlanarComponentInfo()
        self.failUnlessIsInstance(v.offset, (int, long))
        self.failUnlessIsInstance(v.rowBytes, (int, long))

        v = CVPlanarPixelBufferInfo_YCbCrPlanar()
        self.failUnlessIsInstance(v.componentInfoY, CVPlanarComponentInfo)
        self.failUnlessIsInstance(v.componentInfoCb, CVPlanarComponentInfo)
        self.failUnlessIsInstance(v.componentInfoCr, CVPlanarComponentInfo)

    def testFunctions(self):
        self.failUnlessIsInstance(CVPixelBufferGetTypeID(), (int, long))


        buf = self.makeBuffer()
        self.failUnlessIsInstance(buf, CVPixelBufferRef)


        v = CVPixelBufferRetain(buf)
        self.failUnless(v is buf)
        CVPixelBufferRelease(v)

        self.failUnlessArgIsOut(CVPixelBufferCreateResolvedAttributesDictionary, 2)
        rv, v = CVPixelBufferCreateResolvedAttributesDictionary(None, [], None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(v, CFDictionaryRef)



        v = CVPixelBufferGetWidth(buf)
        self.failUnlessIsInstance(v, (int, long))

        v = CVPixelBufferGetHeight(buf)
        self.failUnlessIsInstance(v, (int, long))

        v = CVPixelBufferGetPixelFormatType(buf)
        self.failUnlessIsInstance(v, (int, long))

        rv = CVPixelBufferLockBaseAddress(buf, 0)
        self.failUnlessEqual(rv, 0)

        self.failUnlessResultHasType(CVPixelBufferGetBaseAddress, '^v')
        self.failUnlessResultIsVariableSize(CVPixelBufferGetBaseAddress)
        v = CVPixelBufferGetBaseAddress(buf)
        self.failUnlessIsInstance(v, objc.varlist)
        self.failUnlessIsInstance(v[0], str)

        self.failUnlessResultHasType(CVPixelBufferGetBaseAddressOfPlane, '^v')
        self.failUnlessResultIsVariableSize(CVPixelBufferGetBaseAddressOfPlane)
        v = CVPixelBufferGetBaseAddressOfPlane(buf, 0)
        if v is not objc.NULL:
            self.failUnlessIsInstance(v, objc.varlist)
            self.failUnlessIsInstance(v[0], str)

        rv = CVPixelBufferUnlockBaseAddress(buf, 0)
        self.failUnlessEqual(rv, 0)

        v = CVPixelBufferGetBytesPerRow(buf)
        self.failUnlessIsInstance(v, (int, long))

        v = CVPixelBufferGetDataSize(buf)
        self.failUnlessIsInstance(v, (int, long))

        v = CVPixelBufferGetPlaneCount(buf)
        self.failUnlessIsInstance(v, (int, long))

        v = CVPixelBufferGetWidthOfPlane(buf, 0)
        self.failUnlessIsInstance(v, (int, long))

        v = CVPixelBufferGetHeightOfPlane(buf, 0)
        self.failUnlessIsInstance(v, (int, long))

        v = CVPixelBufferGetBytesPerRowOfPlane(buf, 0)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessArgIsOut(CVPixelBufferGetExtendedPixels, 1)
        self.failUnlessArgIsOut(CVPixelBufferGetExtendedPixels, 2)
        self.failUnlessArgIsOut(CVPixelBufferGetExtendedPixels, 3)
        self.failUnlessArgIsOut(CVPixelBufferGetExtendedPixels, 4)
        v = CVPixelBufferGetExtendedPixels(buf, None, None, None, None)
        self.failUnlessEqual(len(v), 4)
        for i in range(4):
            self.failUnlessIsInstance(v[i], (int, long))

        rv = CVPixelBufferFillExtendedPixels(buf)
        self.failUnlessIsInstance(rv, (int, long))



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
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(pool, CVPixelBufferPoolRef)

        rv, image = CVPixelBufferPoolCreatePixelBuffer(None, pool, None)
        self.failUnlessEqual(rv, 0)
        return image






if __name__ == "__main__":
    main()
