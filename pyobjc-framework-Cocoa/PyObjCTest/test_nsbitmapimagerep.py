import array
import sys

import AppKit
from objc import NO, YES
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSBitmapImageRep(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSBitmapImageRepPropertyKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSBitmapFormat)
        self.assertIsEnumType(AppKit.NSBitmapImageFileType)
        self.assertIsEnumType(AppKit.NSImageRepLoadStatus)
        self.assertIsEnumType(AppKit.NSTIFFCompression)

    def testInstantiation(self):
        # widthxheight RGB 24bpp image
        width = 256
        height = 256
        dataPlanes = (None, None, None, None, None)
        dataPlanes = None
        i1 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
            dataPlanes, width, height, 8, 3, NO, NO, AppKit.NSDeviceRGBColorSpace, 0, 0
        )
        self.assertTrue(i1)

        i2 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
            None, width, height, 8, 3, NO, NO, AppKit.NSDeviceRGBColorSpace, 0, 0
        )
        self.assertTrue(i2)

    def testPixelFormat(self):
        width = 16
        height = 16

        i1 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
            None,
            width,
            height,
            8,
            3,
            NO,
            NO,
            AppKit.NSDeviceRGBColorSpace,
            AppKit.NSAlphaFirstBitmapFormat,
            0,
            0,
        )
        self.assertIsInstance(i1, AppKit.NSBitmapImageRep)

        singlePlane = bytearray(width * height * 4)
        for i in range(0, width * height):
            si = i * 4
            singlePlane[si] = 1
            singlePlane[si + 1] = 2
            singlePlane[si + 2] = 3
            singlePlane[si + 3] = 4
        dataPlanes = (singlePlane, None, None, None, None)
        # test non-planar, premade buffer
        i2 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
            dataPlanes,
            width,
            height,
            8,
            3,
            NO,
            NO,
            AppKit.NSDeviceRGBColorSpace,
            AppKit.NSAlphaFirstBitmapFormat,
            0,
            0,
        )
        self.assertIsInstance(i2, AppKit.NSBitmapImageRep)

        bitmapData = i2.bitmapData()

        self.assertEqual(len(bitmapData), width * height * 4)

    def testImageData(self):
        width = 256
        height = 256

        rPlane = array.array("B")
        rPlane.fromlist([y % 256 for y in range(0, height) for x in range(0, width)])
        if sys.version_info[0] == 3:
            buffer = memoryview
        else:
            from __builtin__ import buffer
        rPlane = buffer(rPlane)

        gPlane = array.array("B")
        gPlane.fromlist(
            [y % 256 for y in range(0, height) for x in range(width, 0, -1)]
        )
        gPlane = buffer(gPlane)

        bPlane = array.array("B")
        bPlane.fromlist([x % 256 for y in range(0, height) for x in range(0, width)])
        bPlane = buffer(bPlane)

        dataPlanes = (rPlane, gPlane, bPlane, None, None)

        # test planar, pre-made buffer
        i1 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
            dataPlanes, width, height, 8, 3, NO, YES, AppKit.NSDeviceRGBColorSpace, 0, 0
        )
        self.assertTrue(i1)

        singlePlane = bytearray(width * height * 3)
        for i in range(0, width * height):
            si = i * 3
            if sys.version_info[0] == 2:
                singlePlane[si] = rPlane[i]
                singlePlane[si + 1] = gPlane[i]
                singlePlane[si + 2] = bPlane[i]
            else:

                def as_byte(v):
                    if isinstance(v, int):
                        return v
                    else:
                        return ord(v)

                singlePlane[si] = as_byte(rPlane[i])
                singlePlane[si + 1] = as_byte(gPlane[i])
                singlePlane[si + 2] = as_byte(bPlane[i])

        dataPlanes = (singlePlane, None, None, None, None)
        # test non-planar, premade buffer
        i2 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
            dataPlanes, width, height, 8, 3, NO, NO, AppKit.NSDeviceRGBColorSpace, 0, 0
        )

        # test grey scale
        greyPlane = array.array("B")
        greyPlane.fromlist([x % 256 for x in range(0, height) for x in range(0, width)])
        greyPlanes = (greyPlane, None, None, None, None)
        greyImage = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
            greyPlanes,
            width,
            height,
            8,
            1,
            NO,
            YES,
            AppKit.NSCalibratedWhiteColorSpace,
            width,
            8,
        )
        self.assertIsNot(greyImage, None)

        # test planar, AppKit.NSBIR allocated buffer
        i3 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
            None, width, height, 8, 3, NO, YES, AppKit.NSDeviceRGBColorSpace, 0, 0
        )

        r, g, b, a, o = i3.getBitmapDataPlanes_()
        self.assertTrue(r)
        self.assertTrue(g)
        self.assertTrue(b)
        self.assertTrue(not a)
        self.assertTrue(not o)

        self.assertEqual(len(r), len(rPlane))
        self.assertEqual(len(g), len(gPlane))
        self.assertEqual(len(b), len(bPlane))

        r[0 : len(r)] = rPlane[0 : len(rPlane)]
        g[0 : len(g)] = gPlane[0 : len(gPlane)]
        b[0 : len(b)] = bPlane[0 : len(bPlane)]

        bitmapData = i2.bitmapData()

        self.assertEqual(len(bitmapData), len(singlePlane))
        self.assertEqual(bitmapData.tobytes(), singlePlane)

        a = array.array("L", [255] * 4)
        self.assertArgIsOut(AppKit.NSBitmapImageRep.getPixel_atX_y_, 0)
        d = i2.getPixel_atX_y_(a, 1, 1)
        self.assertIs(a, d)


class TestBadCreation(TestCase):
    # Redirect stderr to /dev/null for the duration of this test,
    # AppKit.NSBitmapImageRep will write an error message to stderr.

    def setUp(self):
        import os

        self.duppedStderr = os.dup(2)
        fp = os.open("/dev/null", os.O_RDWR)
        os.dup2(fp, 2)
        os.close(fp)

    def tearDown(self):
        import os

        os.dup2(self.duppedStderr, 2)

    def test_AllocInit(self):
        y = AppKit.NSBitmapImageRep.alloc()
        try:
            self.assertRaises(ValueError, y.init)
        finally:
            width = 256
            height = 256
            dataPlanes = (None, None, None, None, None)
            y = y.initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                width,
                height,
                8,
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                0,
                0,
            )

    def testConstants(self):
        self.assertEqual(AppKit.NSTIFFCompressionNone, 1)
        self.assertEqual(AppKit.NSTIFFCompressionCCITTFAX3, 3)
        self.assertEqual(AppKit.NSTIFFCompressionCCITTFAX4, 4)
        self.assertEqual(AppKit.NSTIFFCompressionLZW, 5)
        self.assertEqual(AppKit.NSTIFFCompressionJPEG, 6)
        self.assertEqual(AppKit.NSTIFFCompressionNEXT, 32766)
        self.assertEqual(AppKit.NSTIFFCompressionPackBits, 32773)
        self.assertEqual(AppKit.NSTIFFCompressionOldJPEG, 32865)

        self.assertEqual(AppKit.NSTIFFFileType, 0)
        self.assertEqual(AppKit.NSBMPFileType, 1)
        self.assertEqual(AppKit.NSGIFFileType, 2)
        self.assertEqual(AppKit.NSJPEGFileType, 3)
        self.assertEqual(AppKit.NSPNGFileType, 4)
        self.assertEqual(AppKit.NSJPEG2000FileType, 5)

        self.assertEqual(AppKit.NSBitmapImageFileTypeTIFF, 0)
        self.assertEqual(AppKit.NSBitmapImageFileTypeBMP, 1)
        self.assertEqual(AppKit.NSBitmapImageFileTypeGIF, 2)
        self.assertEqual(AppKit.NSBitmapImageFileTypeJPEG, 3)
        self.assertEqual(AppKit.NSBitmapImageFileTypePNG, 4)
        self.assertEqual(AppKit.NSBitmapImageFileTypeJPEG2000, 5)

        self.assertEqual(AppKit.NSBitmapFormatAlphaFirst, 1 << 0)
        self.assertEqual(AppKit.NSBitmapFormatAlphaNonpremultiplied, 1 << 1)
        self.assertEqual(AppKit.NSBitmapFormatFloatingPointSamples, 1 << 2)
        self.assertEqual(AppKit.NSBitmapFormatSixteenBitLittleEndian, 1 << 8)
        self.assertEqual(AppKit.NSBitmapFormatThirtyTwoBitLittleEndian, 1 << 9)
        self.assertEqual(AppKit.NSBitmapFormatSixteenBitBigEndian, 1 << 10)
        self.assertEqual(AppKit.NSBitmapFormatThirtyTwoBitBigEndian, 1 << 11)

        self.assertEqual(AppKit.NSImageRepLoadStatusUnknownType, -1)
        self.assertEqual(AppKit.NSImageRepLoadStatusReadingHeader, -2)
        self.assertEqual(AppKit.NSImageRepLoadStatusWillNeedAllData, -3)
        self.assertEqual(AppKit.NSImageRepLoadStatusInvalidData, -4)
        self.assertEqual(AppKit.NSImageRepLoadStatusUnexpectedEOF, -5)
        self.assertEqual(AppKit.NSImageRepLoadStatusCompleted, -6)

        self.assertEqual(AppKit.NSAlphaFirstBitmapFormat, 1 << 0)
        self.assertEqual(AppKit.NSAlphaNonpremultipliedBitmapFormat, 1 << 1)
        self.assertEqual(AppKit.NSFloatingPointSamplesBitmapFormat, 1 << 2)

        self.assertIsInstance(AppKit.NSImageCompressionMethod, str)
        self.assertIsInstance(AppKit.NSImageCompressionFactor, str)
        self.assertIsInstance(AppKit.NSImageDitherTransparency, str)
        self.assertIsInstance(AppKit.NSImageRGBColorTable, str)
        self.assertIsInstance(AppKit.NSImageInterlaced, str)
        self.assertIsInstance(AppKit.NSImageColorSyncProfileData, str)
        self.assertIsInstance(AppKit.NSImageFrameCount, str)
        self.assertIsInstance(AppKit.NSImageCurrentFrame, str)
        self.assertIsInstance(AppKit.NSImageCurrentFrameDuration, str)
        self.assertIsInstance(AppKit.NSImageLoopCount, str)
        self.assertIsInstance(AppKit.NSImageGamma, str)
        self.assertIsInstance(AppKit.NSImageProgressive, str)
        self.assertIsInstance(AppKit.NSImageEXIFData, str)
        self.assertIsInstance(AppKit.NSImageFallbackBackgroundColor, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(AppKit.NS16BitLittleEndianBitmapFormat, (1 << 8))
        self.assertEqual(AppKit.NS32BitLittleEndianBitmapFormat, (1 << 9))
        self.assertEqual(AppKit.NS16BitBigEndianBitmapFormat, (1 << 10))
        self.assertEqual(AppKit.NS32BitBigEndianBitmapFormat, (1 << 11))

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(AppKit.NSImageIPTCData, str)

    def testTiffCompression(self):
        lst, nr = AppKit.NSBitmapImageRep.getTIFFCompressionTypes_count_(None, None)
        self.assertIsInstance(lst, tuple)
        self.assertIsInstance(nr, int)
        self.assertEqual(len(lst), nr)
        self.assertNotEqual(len(lst), 0)
        self.assertIsInstance(lst[0], int)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSBitmapImageRep.isPlanar)
        self.assertResultIsBOOL(AppKit.NSBitmapImageRep.canBeCompressedUsing_)
        self.assertArgIsBOOL(
            AppKit.NSBitmapImageRep.incrementalLoadFromData_complete_, 1
        )

        self.assertArgIsOut(AppKit.NSBitmapImageRep.getCompression_factor_, 0)
        self.assertArgIsOut(AppKit.NSBitmapImageRep.getCompression_factor_, 1)
