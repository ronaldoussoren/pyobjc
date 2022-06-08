from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCVPixelFormatDescription(TestCase):
    def testConstants(self):
        self.assertIsInstance(Quartz.kCVPixelFormatName, str)
        self.assertIsInstance(Quartz.kCVPixelFormatConstant, str)
        self.assertIsInstance(Quartz.kCVPixelFormatCodecType, str)
        self.assertIsInstance(Quartz.kCVPixelFormatFourCC, str)
        self.assertIsInstance(Quartz.kCVPixelFormatPlanes, str)

        self.assertIsInstance(Quartz.kCVPixelFormatBlockWidth, str)
        self.assertIsInstance(Quartz.kCVPixelFormatBlockHeight, str)
        self.assertIsInstance(Quartz.kCVPixelFormatBitsPerBlock, str)
        self.assertIsInstance(Quartz.kCVPixelFormatBlockHorizontalAlignment, str)
        self.assertIsInstance(Quartz.kCVPixelFormatBlockVerticalAlignment, str)
        self.assertIsInstance(Quartz.kCVPixelFormatHorizontalSubsampling, str)
        self.assertIsInstance(Quartz.kCVPixelFormatVerticalSubsampling, str)
        self.assertIsInstance(Quartz.kCVPixelFormatOpenGLFormat, str)
        self.assertIsInstance(Quartz.kCVPixelFormatOpenGLType, str)
        self.assertIsInstance(Quartz.kCVPixelFormatOpenGLInternalFormat, str)
        self.assertIsInstance(Quartz.kCVPixelFormatCGBitmapInfo, str)
        self.assertIsInstance(Quartz.kCVPixelFormatQDCompatibility, str)
        self.assertIsInstance(Quartz.kCVPixelFormatCGBitmapContextCompatibility, str)
        self.assertIsInstance(Quartz.kCVPixelFormatCGImageCompatibility, str)
        self.assertIsInstance(Quartz.kCVPixelFormatOpenGLCompatibility, str)
        self.assertIsInstance(Quartz.kCVPixelFormatFillExtendedPixelsCallback, str)

    def testFunctions(self):
        self.assertResultIsCFRetained(
            Quartz.CVPixelFormatDescriptionCreateWithPixelFormatType
        )
        v = Quartz.CVPixelFormatDescriptionCreateWithPixelFormatType(
            None, Quartz.kCVPixelFormatType_32ARGB
        )
        self.assertIsInstance(v, Quartz.CFDictionaryRef)

        self.assertResultIsCFRetained(
            Quartz.CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes
        )
        v = Quartz.CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(None)
        self.assertIsInstance(v, Quartz.CFArrayRef)
        self.assertNotEqual(len(v), 0)
        self.assertIsInstance(v[0], int)

        tp = 42
        while tp in v:
            tp += 1

        Quartz.CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType({}, tp)

    @min_os_level("12.0")
    def testFunctions12_0(self):
        self.assertResultIsBOOL(Quartz.CVIsCompressedPixelFormatAvailable)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCVPixelFormatBlackBlock, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Quartz.kCVPixelFormatContainsAlpha, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Quartz.kCVPixelFormatContainsYCbCr, str)
        self.assertIsInstance(Quartz.kCVPixelFormatContainsRGB, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCVPixelFormatComponentRange, str)
        self.assertIsInstance(Quartz.kCVPixelFormatComponentRange_VideoRange, str)
        self.assertIsInstance(Quartz.kCVPixelFormatComponentRange_FullRange, str)
        self.assertIsInstance(Quartz.kCVPixelFormatComponentRange_WideRange, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(Quartz.kCVPixelFormatContainsGrayscale, str)

    @min_os_level("13.0")
    def testConstants13_0(self):
        self.assertIsInstance(Quartz.kCVPixelFormatContainsSenselArray, str)
