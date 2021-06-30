import os

from Foundation import NSMutableData
from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


def buffer(value):
    if isinstance(value, bytes):
        return value
    return value.encode("latin1")


class TestCGImageDestination(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGImageDestinationRef)

    def testConstants(self):
        self.assertIsInstance(Quartz.kCGImageDestinationLossyCompressionQuality, str)
        self.assertIsInstance(Quartz.kCGImageDestinationBackgroundColor, str)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGImageDestinationGetTypeID(), int)

        self.assertResultIsCFRetained(Quartz.CGImageDestinationCopyTypeIdentifiers)
        v = Quartz.CGImageDestinationCopyTypeIdentifiers()
        self.assertIsInstance(v, Quartz.CFArrayRef)
        if v:
            self.assertIsInstance(v[0], str)

        data = NSMutableData.dataWithCapacity_(1024 * 1024 * 50)
        self.assertResultIsCFRetained(Quartz.CGImageDestinationCreateWithData)
        dest = Quartz.CGImageDestinationCreateWithData(data, v[0], 1, None)
        self.assertIsInstance(dest, Quartz.CGImageDestinationRef)

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertResultIsCFRetained(Quartz.CGImageDestinationCreateWithURL)
        dest = Quartz.CGImageDestinationCreateWithURL(url, "public.tiff", 2, None)
        self.assertIsInstance(dest, Quartz.CGImageDestinationRef)

        Quartz.CGImageDestinationSetProperties(dest, {"key": "value"})

        provider = Quartz.CGDataProviderCreateWithCFData(buffer("1" * 4 * 100 * 80))
        img = Quartz.CGImageCreate(
            100,
            80,
            8,
            32,
            400,
            Quartz.CGColorSpaceCreateDeviceRGB(),
            Quartz.kCGImageAlphaPremultipliedLast,
            provider,
            None,
            False,
            Quartz.kCGRenderingIntentDefault,
        )
        self.assertIsInstance(img, Quartz.CGImageRef)

        Quartz.CGImageDestinationAddImage(dest, img, None)

        image_path = "/System/Library/ColorSync/Calibrators/Display Calibrator.app/Contents/Resources/bullet.tif"
        if not os.path.exists(image_path):
            image_path = "/System/Library/ColorSync/Calibrators/Display Calibrator.app/Contents/Resources/brightness.png"
        if not os.path.exists(image_path):
            image_path = "/System/Library/ColorSync/Calibrators/Display Calibrator.app/Contents/Resources/brightness.tiff"

        self.assertTrue(os.path.exists(image_path))

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, image_path, Quartz.kCFURLPOSIXPathStyle, False
        )

        isrc = Quartz.CGImageSourceCreateWithURL(url, None)
        Quartz.CGImageDestinationAddImageFromSource(dest, isrc, 0, None)

        self.assertResultHasType(Quartz.CGImageDestinationFinalize, objc._C_BOOL)
        v = Quartz.CGImageDestinationFinalize(dest)
        self.assertIsInstance(v, bool)
        self.assertIs(v, True)

        dta = NSMutableData.alloc().init()
        cons = Quartz.CGDataConsumerCreateWithCFData(dta)

        self.assertResultIsCFRetained(Quartz.CGImageDestinationCreateWithDataConsumer)
        c = Quartz.CGImageDestinationCreateWithDataConsumer(
            cons, "public.tiff", 1, None
        )
        self.assertIsInstance(c, Quartz.CGImageDestinationRef)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(Quartz.kCGImageDestinationMetadata, str)
        self.assertIsInstance(Quartz.kCGImageDestinationMergeMetadata, str)
        self.assertIsInstance(Quartz.kCGImageMetadataShouldExcludeXMP, str)
        self.assertIsInstance(Quartz.kCGImageDestinationDateTime, str)
        self.assertIsInstance(Quartz.kCGImageDestinationOrientation, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Quartz.kCGImageDestinationImageMaxPixelSize, str)
        self.assertIsInstance(Quartz.kCGImageDestinationEmbedThumbnail, str)
        self.assertIsInstance(Quartz.kCGImageMetadataShouldExcludeGPS, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCGImageDestinationOptimizeColorForSharing, str)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(Quartz.kCGImageDestinationPreserveGainMap, str)

    @min_os_level("10.8")
    def testFunctions10_8(self):
        Quartz.CGImageDestinationAddImageAndMetadata
        self.assertResultHasType(Quartz.CGImageDestinationCopyImageSource, objc._C_BOOL)
        self.assertArgIsOut(Quartz.CGImageDestinationCopyImageSource, 3)

    @min_os_level("10.13")
    def testFunctions10_13(self):
        Quartz.CGImageDestinationAddAuxiliaryDataInfo
