import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level

try:
    import Quartz
except ImportError:
    Quartz = None


class TestNSGraphicsContext(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSGraphicsContextAttributeKey, str)
        self.assertIsTypedEnum(AppKit.NSGraphicsContextRepresentationFormatName, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSImageInterpolation)

    def testConstants(self):
        self.assertIsInstance(AppKit.NSGraphicsContextDestinationAttributeName, str)
        self.assertIsInstance(
            AppKit.NSGraphicsContextRepresentationFormatAttributeName, str
        )
        self.assertIsInstance(AppKit.NSGraphicsContextPSFormat, str)
        self.assertIsInstance(AppKit.NSGraphicsContextPDFFormat, str)

        self.assertEqual(AppKit.NSImageInterpolationDefault, 0)
        self.assertEqual(AppKit.NSImageInterpolationNone, 1)
        self.assertEqual(AppKit.NSImageInterpolationLow, 2)
        self.assertEqual(AppKit.NSImageInterpolationHigh, 3)
        self.assertEqual(AppKit.NSImageInterpolationMedium, 4)

        self.assertEqual(AppKit.NSColorRenderingIntentDefault, 0)
        self.assertEqual(AppKit.NSColorRenderingIntentAbsoluteColorimetric, 1)
        self.assertEqual(AppKit.NSColorRenderingIntentRelativeColorimetric, 2)
        self.assertEqual(AppKit.NSColorRenderingIntentPerceptual, 3)
        self.assertEqual(AppKit.NSColorRenderingIntentSaturation, 4)

    def testMethods(self):
        self.assertArgIsBOOL(
            AppKit.NSGraphicsContext.graphicsContextWithGraphicsPort_flipped_, 1
        )
        self.assertResultIsBOOL(AppKit.NSGraphicsContext.currentContextDrawingToScreen)
        self.assertResultIsBOOL(AppKit.NSGraphicsContext.isDrawingToScreen)
        self.assertResultIsBOOL(AppKit.NSGraphicsContext.isFlipped)
        self.assertResultIsBOOL(AppKit.NSGraphicsContext.shouldAntialias)
        self.assertArgIsBOOL(AppKit.NSGraphicsContext.setShouldAntialias_, 0)

        img = AppKit.NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(  # noqa: B950
            None, 255, 255, 8, 4, True, False, AppKit.NSCalibratedRGBColorSpace, 0, 0, 0
        )
        context = AppKit.NSGraphicsContext.graphicsContextWithBitmapImageRep_(img)
        self.assertIsInstance(context, AppKit.NSGraphicsContext)
        if Quartz is not None:
            port = context.graphicsPort()
            self.assertIsInstance(port, Quartz.CGContextRef)

        self.assertArgHasType(
            AppKit.NSGraphicsContext.graphicsContextWithGraphicsPort_flipped_,
            0,
            b"^{CGContext=}",
        )
        self.assertResultHasType(
            AppKit.NSGraphicsContext.graphicsPort, b"^{CGContext=}"
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBOOL(
            AppKit.NSGraphicsContext.graphicsContextWithCGContext_flipped_, 1
        )
