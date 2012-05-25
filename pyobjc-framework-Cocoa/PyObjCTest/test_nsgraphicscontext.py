
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

try:
    import Quartz
except ImportError:
    Quartz = None


class TestNSGraphicsContext (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSGraphicsContextDestinationAttributeName, unicode)
        self.assertIsInstance(NSGraphicsContextRepresentationFormatAttributeName, unicode)
        self.assertIsInstance(NSGraphicsContextPSFormat, unicode)
        self.assertIsInstance(NSGraphicsContextPDFFormat, unicode)

        self.assertEqual(NSImageInterpolationDefault, 0)
        self.assertEqual(NSImageInterpolationNone, 1)
        self.assertEqual(NSImageInterpolationLow, 2)
        self.assertEqual(NSImageInterpolationHigh, 3)

        self.assertEqual(NSColorRenderingIntentDefault, 0)
        self.assertEqual(NSColorRenderingIntentAbsoluteColorimetric, 1)
        self.assertEqual(NSColorRenderingIntentRelativeColorimetric, 2)
        self.assertEqual(NSColorRenderingIntentPerceptual, 3)
        self.assertEqual(NSColorRenderingIntentSaturation, 4)


    def testMethods(self):
        self.assertArgIsBOOL(NSGraphicsContext.graphicsContextWithGraphicsPort_flipped_, 1)
        self.assertResultIsBOOL(NSGraphicsContext.currentContextDrawingToScreen)
        self.assertResultIsBOOL(NSGraphicsContext.isDrawingToScreen)
        self.assertResultIsBOOL(NSGraphicsContext.isFlipped)
        self.assertResultIsBOOL(NSGraphicsContext.shouldAntialias)
        self.assertArgIsBOOL(NSGraphicsContext.setShouldAntialias_, 0)

        img = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(
            None, 255, 255, 8, 4, True, False, NSCalibratedRGBColorSpace, 0, 0, 0)
        context = NSGraphicsContext.graphicsContextWithBitmapImageRep_(img)
        self.assertIsInstance(context, NSGraphicsContext)
        if Quartz is not None:
            port = context.graphicsPort()
            self.assertIsInstance(port, Quartz.CGContextRef)

        self.assertArgHasType(NSGraphicsContext.graphicsContextWithGraphicsPort_flipped_, 0, b'^{CGContext=}')
        self.assertResultHasType(NSGraphicsContext.graphicsPort, b'^{CGContext=}')


if __name__ == "__main__":
    main()
