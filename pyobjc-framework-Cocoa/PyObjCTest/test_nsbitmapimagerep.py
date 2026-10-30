import array
import warnings

import AppKit
from objc import NO, YES
from PyObjCTools.TestSupport import TestCase, min_os_level, NotBool, NoObjCClass


class TestNSBitmapImageRep(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSBitmapFormat)
        self.assertEqual(AppKit.NSBitmapFormatAlphaFirst, 1 << 0)
        self.assertEqual(AppKit.NSBitmapFormatAlphaNonpremultiplied, 1 << 1)
        self.assertEqual(AppKit.NSBitmapFormatFloatingPointSamples, 1 << 2)
        self.assertEqual(AppKit.NSBitmapFormatSixteenBitLittleEndian, 1 << 8)
        self.assertEqual(AppKit.NSBitmapFormatThirtyTwoBitLittleEndian, 1 << 9)
        self.assertEqual(AppKit.NSBitmapFormatSixteenBitBigEndian, 1 << 10)
        self.assertEqual(AppKit.NSBitmapFormatThirtyTwoBitBigEndian, 1 << 11)

        # Legacy alias:
        self.assertEqual(AppKit.NSAlphaFirstBitmapFormat, 1 << 0)
        self.assertEqual(AppKit.NSAlphaNonpremultipliedBitmapFormat, 1 << 1)
        self.assertEqual(AppKit.NSFloatingPointSamplesBitmapFormat, 1 << 2)
        self.assertEqual(AppKit.NS16BitLittleEndianBitmapFormat, (1 << 8))
        self.assertEqual(AppKit.NS32BitLittleEndianBitmapFormat, (1 << 9))
        self.assertEqual(AppKit.NS16BitBigEndianBitmapFormat, (1 << 10))
        self.assertEqual(AppKit.NS32BitBigEndianBitmapFormat, (1 << 11))

        self.assertIsEnumType(AppKit.NSBitmapImageFileType)
        self.assertEqual(AppKit.NSBitmapImageFileTypeTIFF, 0)
        self.assertEqual(AppKit.NSBitmapImageFileTypeBMP, 1)
        self.assertEqual(AppKit.NSBitmapImageFileTypeGIF, 2)
        self.assertEqual(AppKit.NSBitmapImageFileTypeJPEG, 3)
        self.assertEqual(AppKit.NSBitmapImageFileTypePNG, 4)
        self.assertEqual(AppKit.NSBitmapImageFileTypeJPEG2000, 5)

        # Legacy alias:
        self.assertEqual(AppKit.NSTIFFFileType, 0)
        self.assertEqual(AppKit.NSBMPFileType, 1)
        self.assertEqual(AppKit.NSGIFFileType, 2)
        self.assertEqual(AppKit.NSJPEGFileType, 3)
        self.assertEqual(AppKit.NSPNGFileType, 4)
        self.assertEqual(AppKit.NSJPEG2000FileType, 5)

        self.assertIsEnumType(AppKit.NSImageRepLoadStatus)
        self.assertEqual(AppKit.NSImageRepLoadStatusUnknownType, -1)
        self.assertEqual(AppKit.NSImageRepLoadStatusReadingHeader, -2)
        self.assertEqual(AppKit.NSImageRepLoadStatusWillNeedAllData, -3)
        self.assertEqual(AppKit.NSImageRepLoadStatusInvalidData, -4)
        self.assertEqual(AppKit.NSImageRepLoadStatusUnexpectedEOF, -5)
        self.assertEqual(AppKit.NSImageRepLoadStatusCompleted, -6)

        self.assertIsEnumType(AppKit.NSTIFFCompression)
        self.assertEqual(AppKit.NSTIFFCompressionNone, 1)
        self.assertEqual(AppKit.NSTIFFCompressionCCITTFAX3, 3)
        self.assertEqual(AppKit.NSTIFFCompressionCCITTFAX4, 4)
        self.assertEqual(AppKit.NSTIFFCompressionLZW, 5)
        self.assertEqual(AppKit.NSTIFFCompressionJPEG, 6)
        self.assertEqual(AppKit.NSTIFFCompressionNEXT, 32766)
        self.assertEqual(AppKit.NSTIFFCompressionPackBits, 32773)
        self.assertEqual(AppKit.NSTIFFCompressionOldJPEG, 32865)

    def test_typed_enums(self):
        self.assertIsTypedEnum(AppKit.NSBitmapImageRepPropertyKey, str)

    def test_constants(self):
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

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(AppKit.NSImageIPTCData, str)

    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSBitmapImageRep.isPlanar)
        self.assertResultIsBOOL(AppKit.NSBitmapImageRep.canBeCompressedUsing_)
        self.assertArgIsBOOL(
            AppKit.NSBitmapImageRep.incrementalLoadFromData_complete_, 1
        )

        self.assertArgIsOut(AppKit.NSBitmapImageRep.getCompression_factor_, 0)
        self.assertArgIsOut(AppKit.NSBitmapImageRep.getCompression_factor_, 1)


class TestNSBitmapImageRepUsage(TestCase):
    def test_creation(self):
        # widthxheight RGB 24bpp image
        width = 256
        height = 256
        dataPlanes = (None, None, None, None, None)

        with self.assertRaisesRegex(TypeError, "expected 10 arguments, got 0"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_()  # noqa: B950

        with self.assertRaisesRegex(
            TypeError, "First argument must be a 5 element sequence or None."
        ):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                42, width, height, 8, 3, NO, NO, AppKit.NSDeviceRGBColorSpace, 0, 0
            )
        with self.assertRaisesRegex(
            TypeError, "First argument must be a 5 element sequence or None."
        ):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes + dataPlanes,
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
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'int'"
        ):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                (42,) + dataPlanes[:4],
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
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'int'"
        ):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                (
                    b"\x00" * 4000,
                    42,
                )
                + dataPlanes[:3],
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
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'int'"
        ):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                (
                    b"x" * 4000,
                    42,
                )
                + dataPlanes[:3],
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
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                "width",
                height,
                8,
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                0,
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                width,
                "height",
                8,
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                0,
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                width,
                height,
                "8",
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                0,
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                width,
                height,
                8,
                "3",
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                0,
                0,
            )
        with self.assertRaisesRegex(TypeError, "this is not a bool"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                width,
                height,
                8,
                3,
                NotBool(),
                NO,
                AppKit.NSDeviceRGBColorSpace,
                0,
                0,
            )
        with self.assertRaisesRegex(TypeError, "this is not a bool"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                width,
                height,
                8,
                3,
                NO,
                NotBool(),
                AppKit.NSDeviceRGBColorSpace,
                0,
                0,
            )
        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes, width, height, 8, 3, NO, NO, NoObjCClass(), 0, 0
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                width,
                height,
                8,
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                "0",
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
                dataPlanes,
                width,
                height,
                8,
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                0,
                "0",
            )

        i1 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
            dataPlanes, width, height, 8, 3, NO, NO, AppKit.NSDeviceRGBColorSpace, 0, 0
        )
        self.assertIsInstance(i1, AppKit.NSBitmapImageRep)
        self.assertEqual(i1.size(), (width, height))

        i2 = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_(  # noqa: B950
            None, width, height, 8, 3, NO, NO, AppKit.NSDeviceRGBColorSpace, 0, 0
        )
        self.assertIsInstance(i2, AppKit.NSBitmapImageRep)

    def test_pixelformat(self):
        width = 16
        height = 16

        with self.assertRaisesRegex(TypeError, "expected 11 arguments, got 0"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_()  # noqa: B950

        with self.assertRaisesRegex(
            TypeError, "First argument must be a 5 element sequence or None."
        ):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                42,
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
        with self.assertRaisesRegex(
            TypeError, "First argument must be a 5 element sequence or None."
        ):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                (),
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
        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'int'"
        ):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                (None, None, b"x" * 4096, None, 42),
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
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                "width",
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
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                width,
                "height",
                8,
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                AppKit.NSAlphaFirstBitmapFormat,
                0,
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                width,
                height,
                "8",
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                AppKit.NSAlphaFirstBitmapFormat,
                0,
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                width,
                height,
                8,
                "3",
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                AppKit.NSAlphaFirstBitmapFormat,
                0,
                0,
            )
        with self.assertRaisesRegex(TypeError, "this is not a bool"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                width,
                height,
                8,
                3,
                NotBool(),
                NO,
                AppKit.NSDeviceRGBColorSpace,
                AppKit.NSAlphaFirstBitmapFormat,
                0,
                0,
            )
        with self.assertRaisesRegex(TypeError, "this is not a bool"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                width,
                height,
                8,
                3,
                NO,
                NotBool(),
                AppKit.NSDeviceRGBColorSpace,
                AppKit.NSAlphaFirstBitmapFormat,
                0,
                0,
            )
        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                width,
                height,
                8,
                3,
                NO,
                NO,
                NoObjCClass(),
                AppKit.NSAlphaFirstBitmapFormat,
                0,
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                width,
                height,
                8,
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                "AppKit.NSAlphaFirstBitmapFormat",
                0,
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
                None,
                width,
                height,
                8,
                3,
                NO,
                NO,
                AppKit.NSDeviceRGBColorSpace,
                AppKit.NSAlphaFirstBitmapFormat,
                "0",
                0,
            )
        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
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
                "0",
            )

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

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            i2.bitmapData(42)

        bitmapData = i2.bitmapData()

        self.assertEqual(len(bitmapData), width * height * 4)

    def test_image_data(self):
        width = 256
        height = 256

        rPlane = array.array("B")
        rPlane.fromlist([y % 256 for y in range(0, height) for x in range(0, width)])
        buffer = memoryview
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

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
            i3.getBitmapDataPlanes_(None, 42)

        with self.assertRaisesRegex(ValueError, "buffer must be None"):
            i3.getBitmapDataPlanes_(42)

        r, g, b, a, o = i3.getBitmapDataPlanes_(None)
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

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=DeprecationWarning)
            with self.assertRaisesRegex(
                DeprecationWarning, "leaving of the buffer argument is deprecated"
            ):
                i3.getBitmapDataPlanes_()

        with warnings.catch_warnings(record=True) as wrn:
            warnings.simplefilter("always", category=DeprecationWarning)
            r1 = i3.getBitmapDataPlanes_()
        self.assertEqual(len(wrn), 1)
        r2 = i3.getBitmapDataPlanes_(None)
        self.assertEqual(r1, r2)


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

    def test_alloc_init(self):
        y = AppKit.NSBitmapImageRep.alloc()
        try:
            self.assertRaises(ValueError, y.init)
        finally:
            with self.assertRaisesRegex(TypeError, "expected 10 arguments, got 0"):
                y.initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_()

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
