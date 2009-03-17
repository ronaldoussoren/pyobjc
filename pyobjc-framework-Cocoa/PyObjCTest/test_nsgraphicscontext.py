
from PyObjCTools.TestSupport import *
from AppKit import *
import Quartz.CoreGraphics

class TestNSGraphicsContext (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSGraphicsContextDestinationAttributeName, unicode)
        self.failUnlessIsInstance(NSGraphicsContextRepresentationFormatAttributeName, unicode)
        self.failUnlessIsInstance(NSGraphicsContextPSFormat, unicode)
        self.failUnlessIsInstance(NSGraphicsContextPDFFormat, unicode)

        self.failUnlessEqual(NSImageInterpolationDefault, 0)
        self.failUnlessEqual(NSImageInterpolationNone, 1)
        self.failUnlessEqual(NSImageInterpolationLow, 2)
        self.failUnlessEqual(NSImageInterpolationHigh, 3)

        self.failUnlessEqual(NSColorRenderingIntentDefault, 0)
        self.failUnlessEqual(NSColorRenderingIntentAbsoluteColorimetric, 1)
        self.failUnlessEqual(NSColorRenderingIntentRelativeColorimetric, 2)
        self.failUnlessEqual(NSColorRenderingIntentPerceptual, 3)
        self.failUnlessEqual(NSColorRenderingIntentSaturation, 4)


    def testMethods(self):
        self.failUnlessArgIsBOOL(NSGraphicsContext.graphicsContextWithGraphicsPort_flipped_, 1)
        self.failUnlessResultIsBOOL(NSGraphicsContext.currentContextDrawingToScreen)
        self.failUnlessResultIsBOOL(NSGraphicsContext.isDrawingToScreen)
        self.failUnlessResultIsBOOL(NSGraphicsContext.isFlipped)
        self.failUnlessResultIsBOOL(NSGraphicsContext.shouldAntialias)
        self.failUnlessArgIsBOOL(NSGraphicsContext.setShouldAntialias_, 0)

        img = NSBitmapImageRep.alloc().initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bitmapFormat_bytesPerRow_bitsPerPixel_(
            None, 255, 255, 8, 4, True, False, NSCalibratedRGBColorSpace, 0, 0, 0)
        context = NSGraphicsContext.graphicsContextWithBitmapImageRep_(img)
        self.failUnlessIsInstance(context, NSGraphicsContext)
        port = context.graphicsPort()
        self.failUnlessIsInstance(port, Quartz.CoreGraphics.CGContextRef)

        self.failUnlessArgHasType(NSGraphicsContext.graphicsContextWithGraphicsPort_flipped_, 0, '^{CGContext=}')
        self.failUnlessResultHasType(NSGraphicsContext.graphicsPort, '^{CGContext=}')


if __name__ == "__main__":
    main()
