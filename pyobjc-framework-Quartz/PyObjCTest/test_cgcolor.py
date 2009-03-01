
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGColor (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGColorRef)

    def testFunctions(self):
        self.failUnlessResultIsCFRetained(CGColorCreate)
        color = CGColorCreate(CGColorSpaceCreateDeviceRGB(),
                [1.0, 0.5, 0.5])
        self.failUnlessIsInstance(color, CGColorRef)

        self.failUnlessResultIsCFRetained(CGColorCreateGenericGray)
        color = CGColorCreateGenericGray(0.75, 0.8)
        self.failUnlessIsInstance(color, CGColorRef)

        self.failUnlessResultIsCFRetained(CGColorCreateGenericCMYK)
        color = CGColorCreateGenericCMYK(0.75, 0.8, 0.5, 1.0, 0.5)
        self.failUnlessIsInstance(color, CGColorRef)

        color = CGColorGetConstantColor(kCGColorWhite)
        self.failUnlessIsInstance(color, CGColorRef)

        self.failUnlessResultIsCFRetained(CGColorCreateGenericRGB)
        color = CGColorCreateGenericRGB(0.75, 0.8, 1.0, 0.5)
        self.failUnlessIsInstance(color, CGColorRef)

        self.failUnlessResultIsCFRetained(CGColorCreateCopy)
        v = CGColorCreateCopy(color)
        self.failUnlessIsInstance(v, CGColorRef)

        self.failUnlessResultIsCFRetained(CGColorCreateCopyWithAlpha)
        v = CGColorCreateCopyWithAlpha(color, 0.7)
        self.failUnlessIsInstance(v, CGColorRef)

        CGColorRetain(color)
        CGColorRelease(color)

        self.failUnlessResultHasType(CGColorEqualToColor, objc._C_BOOL)
        self.failUnless(CGColorEqualToColor(color, color) is True)
        self.failUnless(CGColorEqualToColor(color, v) is False)

        self.failUnlessEqual(CGColorGetNumberOfComponents(color), 4)
        v = CGColorGetComponents(color)
        self.failUnlessIsInstance(v, objc.varlist)
        self.failUnlessIsInstance(v[0], float)

        v = CGColorGetAlpha(color)
        self.failUnlessIsInstance(v, float)

        v = CGColorGetColorSpace(color)
        self.failUnlessIsInstance(v, CGColorSpaceRef)

        v = CGColorGetPattern(color)
        self.failUnless(v is None)

        self.failUnlessIsInstance(CGColorGetTypeID(), (int, long))

        # CGColorCreateWithPattern, CGColorGetPattern: tested in test_cgpattern

    def testConstants(self):
        self.failUnlessIsInstance(kCGColorWhite, unicode)
        self.failUnlessIsInstance(kCGColorBlack, unicode)
        self.failUnlessIsInstance(kCGColorClear, unicode)

if __name__ == "__main__":
    main()
