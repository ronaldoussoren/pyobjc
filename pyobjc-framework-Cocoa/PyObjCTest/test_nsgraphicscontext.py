
from PyObjCTools.TestSupport import *
from AppKit import *

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
        self.fail("+ (NSGraphicsContext *)graphicsContextWithGraphicsPort:(void *)graphicsPort flipped:(BOOL)initialFlippedState;")
        self.fail("+ (NSGraphicsContext *)currentContext;")
        self.fail("- (void *)graphicsPort;")


if __name__ == "__main__":
    main()
