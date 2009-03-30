from PyObjCTools.TestSupport import *
import objc
import array

from objc import YES, NO
from AppKit import *

class TestNSBitmapImageRep(TestCase):
    def testInstantiation(self):
        # widthxheight RGB 24bpp image
        width = 256
        height = 256
        dataPlanes = (None, None, None, None, None)
        i1 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(dataPlanes, width, height, 8, 3, NO, NO, NSDeviceRGBColorSpace, 0, 0)
        self.assert_(i1)

        i2 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(None, width, height, 8, 3, NO, NO, NSDeviceRGBColorSpace, 0, 0)
        self.assert_(i2)

    def testImageData(self):
        width = 256
        height = 256

        rPlane = array.array('B')
        rPlane.fromlist( [y%256 for y in range(0,height) for x in range(0,width)] )
        rPlane = buffer(rPlane)

        gPlane = array.array('B')
        gPlane.fromlist( [y%256 for x in range(0,height) for x in range(width,0,-1)] )
        gPlane = buffer(gPlane)

        bPlane = array.array('B')
        bPlane.fromlist( [x%256 for x in range(0,height) for x in range(0,width)] )
        bPlane = buffer(bPlane)

        dataPlanes = (rPlane, gPlane, bPlane, None, None)

        # test planar, pre-made buffer
        i1 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(dataPlanes, width, height, 8, 3, NO, YES, NSDeviceRGBColorSpace, 0, 0)
        self.assert_(i1)

        singlePlane = objc.allocateBuffer(width*height*3)
        for i in range(0, 256*256):
            si = i * 3
            singlePlane[si] = rPlane[i]
            singlePlane[si+1] = gPlane[i]
            singlePlane[si+2] = bPlane[i]

        dataPlanes = (singlePlane, None, None, None, None)
        # test non-planar, premade buffer
        i2 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(dataPlanes, width, height, 8, 3, NO, NO, NSDeviceRGBColorSpace, 0, 0)

        # test grey scale
        greyPlane = array.array('B')
        greyPlane.fromlist( [x%256 for x in range(0,height) for x in range(0,width)] )
        greyPlanes = (greyPlane, None, None, None, None)
        greyImage = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(greyPlanes, width, height, 8, 1, NO, YES, NSCalibratedWhiteColorSpace, width, 8)

        # test planar, NSBIR allocated buffer
        i3 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(None, width, height, 8, 3, NO, YES, NSDeviceRGBColorSpace, 0, 0)

        r,g,b,a,o = i3.getBitmapDataPlanes_()
        self.assert_(r)
        self.assert_(g)
        self.assert_(b)
        self.assert_(not a)
        self.assert_(not o)

        self.assertEquals(len(r), len(rPlane))
        self.assertEquals(len(g), len(gPlane))
        self.assertEquals(len(b), len(bPlane))

        r[0:len(r)] = rPlane[0:len(rPlane)]
        g[0:len(g)] = gPlane[0:len(gPlane)]
        b[0:len(b)] = bPlane[0:len(bPlane)]

        bitmapData = i2.bitmapData()
        self.assertEquals(len(bitmapData), len(singlePlane))
        self.assertEquals(bitmapData, singlePlane)
        
        a = array.array('I', [255]*4)
        self.failUnlessArgIsOut(NSBitmapImageRep.getPixel_atX_y_, 0)
        d = i2.getPixel_atX_y_(a, 1, 1)
        self.failUnless(a is d)


class TestBadCreation(TestCase):

    # Redirect stderr to /dev/null for the duration of this test, 
    # NSBitmapImageRep will write an error message to stderr.

    def setUp(self):
        import os
        self.duppedStderr = os.dup(2)
        fp = os.open('/dev/null', os.O_RDWR)
        os.dup2(fp, 2)
        os.close(fp)

    def tearDown(self):
        import os
        os.dup2(self.duppedStderr, 2)



    def test_AllocInit(self):
        y = NSBitmapImageRep.alloc()
        try:
            self.assertRaises(ValueError, y.init)
        finally:
            width = 256
            height = 256
            dataPlanes = (None, None, None, None, None)
            y = y.initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(dataPlanes, width, height, 8, 3, NO, NO, NSDeviceRGBColorSpace, 0, 0)

    def testConstants(self):
        self.failUnlessEqual(NSTIFFCompressionNone, 1)
        self.failUnlessEqual(NSTIFFCompressionCCITTFAX3, 3)
        self.failUnlessEqual(NSTIFFCompressionCCITTFAX4, 4)
        self.failUnlessEqual(NSTIFFCompressionLZW, 5)
        self.failUnlessEqual(NSTIFFCompressionJPEG, 6)
        self.failUnlessEqual(NSTIFFCompressionNEXT, 32766)
        self.failUnlessEqual(NSTIFFCompressionPackBits, 32773)
        self.failUnlessEqual(NSTIFFCompressionOldJPEG, 32865)
        self.failUnlessEqual(NSTIFFFileType, 0)
        self.failUnlessEqual(NSBMPFileType, 1)
        self.failUnlessEqual(NSGIFFileType, 2)
        self.failUnlessEqual(NSJPEGFileType, 3)
        self.failUnlessEqual(NSPNGFileType, 4)
        self.failUnlessEqual(NSJPEG2000FileType, 5)
        self.failUnlessEqual(NSImageRepLoadStatusUnknownType, -1)
        self.failUnlessEqual(NSImageRepLoadStatusReadingHeader, -2)
        self.failUnlessEqual(NSImageRepLoadStatusWillNeedAllData, -3)
        self.failUnlessEqual(NSImageRepLoadStatusInvalidData, -4)
        self.failUnlessEqual(NSImageRepLoadStatusUnexpectedEOF, -5)
        self.failUnlessEqual(NSImageRepLoadStatusCompleted, -6)
        self.failUnlessEqual(NSAlphaFirstBitmapFormat, 1 << 0)
        self.failUnlessEqual(NSAlphaNonpremultipliedBitmapFormat, 1 << 1)
        self.failUnlessEqual(NSFloatingPointSamplesBitmapFormat, 1 << 2)

        self.failUnlessIsInstance(NSImageCompressionMethod, unicode)
        self.failUnlessIsInstance(NSImageCompressionFactor, unicode)
        self.failUnlessIsInstance(NSImageDitherTransparency, unicode)
        self.failUnlessIsInstance(NSImageRGBColorTable, unicode)
        self.failUnlessIsInstance(NSImageInterlaced, unicode)
        self.failUnlessIsInstance(NSImageColorSyncProfileData, unicode)
        self.failUnlessIsInstance(NSImageFrameCount, unicode)
        self.failUnlessIsInstance(NSImageCurrentFrame, unicode)
        self.failUnlessIsInstance(NSImageCurrentFrameDuration, unicode)
        self.failUnlessIsInstance(NSImageLoopCount, unicode)
        self.failUnlessIsInstance(NSImageGamma, unicode)
        self.failUnlessIsInstance(NSImageProgressive, unicode)
        self.failUnlessIsInstance(NSImageEXIFData, unicode)
        self.failUnlessIsInstance(NSImageFallbackBackgroundColor, unicode)

    def testTiffCompression(self):
        lst, nr = NSBitmapImageRep.getTIFFCompressionTypes_count_(None, None)
        self.failUnlessIsInstance(lst, tuple)
        self.failUnlessIsInstance(nr, (int, long))
        self.failUnlessEqual(len(lst), nr)
        self.failIfEqual(len(lst), 0)
        self.failUnlessIsInstance(lst[0], (int, long))

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSBitmapImageRep.isPlanar)
        self.failUnlessResultIsBOOL(NSBitmapImageRep.canBeCompressedUsing_)
        self.failUnlessArgIsBOOL(NSBitmapImageRep.incrementalLoadFromData_complete_, 1)

        self.failUnlessArgIsOut(NSBitmapImageRep.getCompression_factor_, 0)
        self.failUnlessArgIsOut(NSBitmapImageRep.getCompression_factor_, 1)

        self.fail("- (id)initWithBitmapDataPlanes:(unsigned char **)planes pixelsWide:(NSInteger)width pixelsHigh:(NSInteger)height bitsPerSample:(NSInteger)bps samplesPerPixel:(NSInteger)spp hasAlpha:(BOOL)alpha isPlanar:(BOOL)isPlanar colorSpaceName:(NSString *)colorSpaceName  bitmapFormat:(NSBitmapFormat)bitmapFormat bytesPerRow:(NSInteger)rBytes bitsPerPixel:(NSInteger)pBits;")



if __name__ == '__main__':
    main( )
