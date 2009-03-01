
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGGradient (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGGradientRef)

    def testConstants(self):
        self.failUnlessEqual(kCGGradientDrawsBeforeStartLocation, 1)
        self.failUnlessEqual(kCGGradientDrawsAfterEndLocation, 2)

    def testFunctions(self):
        self.failUnlessIsInstance(CGGradientGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(CGGradientCreateWithColorComponents)
        gradient = CGGradientCreateWithColorComponents(CGColorSpaceCreateDeviceRGB(),
                (0, 0, 0, 1, 0.2, 0.4, 0.2, 1, 0.8, 0.8, 0.8, 1), (0, 0.8, 0.95), 3)
        self.failUnlessIsInstance(gradient, CGGradientRef)

        self.failUnlessResultIsCFRetained(CGGradientCreateWithColors)
        gradient = CGGradientCreateWithColors(CGColorSpaceCreateDeviceRGB(),
                (CGColorCreateGenericRGB(0, 0, 0, 1), CGColorCreateGenericRGB(0, 0.2, 0.2, 1.0)),
                (0.2, 0.9))

        v = CGGradientRetain(gradient)
        self.failUnless(v is gradient)

        CGGradientRelease(gradient)

if __name__ == "__main__":
    main()
