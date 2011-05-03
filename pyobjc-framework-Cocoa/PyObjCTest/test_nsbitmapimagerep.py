from PyObjCTools.TestSupport import *
import objc
import array
import sys

from objc import YES, NO
from AppKit import *

class TestNSBitmapImageRep(TestCase):
    def testInstantiation(self):
        # widthxheight RGB 24bpp image
        width = 256
        height = 256
        dataPlanes = (None, None, None, None, None)
        dataPlanes = None
        i1 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(dataPlanes, width, height, 8, 3, NO, NO, NSDeviceRGBColorSpace, 0, 0)
        self.assert_(i1)

        i2 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(None, width, height, 8, 3, NO, NO, NSDeviceRGBColorSpace, 0, 0)
        self.assert_(i2)

    def testPixelFormat(self):
        width = 16
        height = 16

        i1 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(None, width, height, 8, 3, NO, NO, NSDeviceRGBColorSpace, NSAlphaFirstBitmapFormat, 0, 0)
        self.assertIsInstance(i1, NSBitmapImageRep)

        singlePlane = objc.allocateBuffer(width*height*4)
        for i in range(0, width*height):
            si = i * 4
            singlePlane[si] = 1
            singlePlane[si+1] = 2
            singlePlane[si+2] = 3
            singlePlane[si+3] = 4
        dataPlanes = (singlePlane, None, None, None, None)
        # test non-planar, premade buffer
        i2 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(dataPlanes, width, height, 8, 3, NO, NO, NSDeviceRGBColorSpace, NSAlphaFirstBitmapFormat, 0, 0)
        self.assertIsInstance(i2, NSBitmapImageRep)

        bitmapData = i2.bitmapData()

        self.assertEqual(len(bitmapData), width * height * 4)

    def testImageData(self):
        width = 256
        height = 256

        rPlane = array.array('B')
        rPlane.fromlist( [y%256 for y in range(0,height) for x in range(0,width)] )
        if sys.version_info[0] == 3:
            buffer = memoryview
        else:
            from __builtin__ import buffer
        rPlane = buffer(rPlane)

        gPlane = array.array('B')
        gPlane.fromlist( [y%256 for y in range(0,height) for x in range(width,0,-1)] )
        gPlane = buffer(gPlane)

        bPlane = array.array('B')
        bPlane.fromlist( [x%256 for y in range(0,height) for x in range(0,width)] )
        bPlane = buffer(bPlane)

        dataPlanes = (rPlane, gPlane, bPlane, None, None)

        # test planar, pre-made buffer
        i1 = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(dataPlanes, width, height, 8, 3, NO, YES, NSDeviceRGBColorSpace, 0, 0)
        self.assert_(i1)

        singlePlane = objc.allocateBuffer(width*height*3)
        for i in range(0, width*height):
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

        self.assertEqual(len(r), len(rPlane))
        self.assertEqual(len(g), len(gPlane))
        self.assertEqual(len(b), len(bPlane))

        r[0:len(r)] = rPlane[0:len(rPlane)]
        g[0:len(g)] = gPlane[0:len(gPlane)]
        b[0:len(b)] = bPlane[0:len(bPlane)]

        bitmapData = i2.bitmapData()

        self.assertEqual(len(bitmapData), len(singlePlane))
        try:
            memoryview
        except NameError:
            self.assertEqual(bitmapData, singlePlane)
        else:
            self.assertEquals(bitmapData.tobytes(),
                singlePlane)
        
        a = array.array('L', [255]*4)
        self.assertArgIsOut(NSBitmapImageRep.getPixel_atX_y_, 0)
        d = i2.getPixel_atX_y_(a, 1, 1)
        self.assertIs(a, d)

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
        self.assertEqual(NSTIFFCompressionNone, 1)
        self.assertEqual(NSTIFFCompressionCCITTFAX3, 3)
        self.assertEqual(NSTIFFCompressionCCITTFAX4, 4)
        self.assertEqual(NSTIFFCompressionLZW, 5)
        self.assertEqual(NSTIFFCompressionJPEG, 6)
        self.assertEqual(NSTIFFCompressionNEXT, 32766)
        self.assertEqual(NSTIFFCompressionPackBits, 32773)
        self.assertEqual(NSTIFFCompressionOldJPEG, 32865)
        self.assertEqual(NSTIFFFileType, 0)
        self.assertEqual(NSBMPFileType, 1)
        self.assertEqual(NSGIFFileType, 2)
        self.assertEqual(NSJPEGFileType, 3)
        self.assertEqual(NSPNGFileType, 4)
        self.assertEqual(NSJPEG2000FileType, 5)
        self.assertEqual(NSImageRepLoadStatusUnknownType, -1)
        self.assertEqual(NSImageRepLoadStatusReadingHeader, -2)
        self.assertEqual(NSImageRepLoadStatusWillNeedAllData, -3)
        self.assertEqual(NSImageRepLoadStatusInvalidData, -4)
        self.assertEqual(NSImageRepLoadStatusUnexpectedEOF, -5)
        self.assertEqual(NSImageRepLoadStatusCompleted, -6)
        self.assertEqual(NSAlphaFirstBitmapFormat, 1 << 0)
        self.assertEqual(NSAlphaNonpremultipliedBitmapFormat, 1 << 1)
        self.assertEqual(NSFloatingPointSamplesBitmapFormat, 1 << 2)

        self.assertIsInstance(NSImageCompressionMethod, unicode)
        self.assertIsInstance(NSImageCompressionFactor, unicode)
        self.assertIsInstance(NSImageDitherTransparency, unicode)
        self.assertIsInstance(NSImageRGBColorTable, unicode)
        self.assertIsInstance(NSImageInterlaced, unicode)
        self.assertIsInstance(NSImageColorSyncProfileData, unicode)
        self.assertIsInstance(NSImageFrameCount, unicode)
        self.assertIsInstance(NSImageCurrentFrame, unicode)
        self.assertIsInstance(NSImageCurrentFrameDuration, unicode)
        self.assertIsInstance(NSImageLoopCount, unicode)
        self.assertIsInstance(NSImageGamma, unicode)
        self.assertIsInstance(NSImageProgressive, unicode)
        self.assertIsInstance(NSImageEXIFData, unicode)
        self.assertIsInstance(NSImageFallbackBackgroundColor, unicode)

    def testTiffCompression(self):
        lst, nr = NSBitmapImageRep.getTIFFCompressionTypes_count_(None, None)
        self.assertIsInstance(lst, tuple)
        self.assertIsInstance(nr, (int, long))
        self.assertEqual(len(lst), nr)
        self.assertNotEqual(len(lst), 0)
        self.assertIsInstance(lst[0], (int, long))

    def testMethods(self):
        self.assertResultIsBOOL(NSBitmapImageRep.isPlanar)
        self.assertResultIsBOOL(NSBitmapImageRep.canBeCompressedUsing_)
        self.assertArgIsBOOL(NSBitmapImageRep.incrementalLoadFromData_complete_, 1)

        self.assertArgIsOut(NSBitmapImageRep.getCompression_factor_, 0)
        self.assertArgIsOut(NSBitmapImageRep.getCompression_factor_, 1)



if __name__ == '__main__':
    main( )
