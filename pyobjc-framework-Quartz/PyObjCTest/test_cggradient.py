
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *


try:
    long
except NameError:
    long = int
class TestCGGradient (TestCase):
    @min_os_level('10.5')
    def testTypes(self):
        self.assertIsCFType(CGGradientRef)

    @min_os_level('10.5')
    def testConstants(self):
        self.assertEqual(kCGGradientDrawsBeforeStartLocation, 1)
        self.assertEqual(kCGGradientDrawsAfterEndLocation, 2)

    @min_os_level('10.5')
    def testFunctions(self):
        self.assertIsInstance(CGGradientGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CGGradientCreateWithColorComponents)
        gradient = CGGradientCreateWithColorComponents(CGColorSpaceCreateDeviceRGB(),
                (0, 0, 0, 1, 0.2, 0.4, 0.2, 1, 0.8, 0.8, 0.8, 1), (0, 0.8, 0.95), 3)
        self.assertIsInstance(gradient, CGGradientRef)

        self.assertResultIsCFRetained(CGGradientCreateWithColors)
        gradient = CGGradientCreateWithColors(CGColorSpaceCreateDeviceRGB(),
                (CGColorCreateGenericRGB(0, 0, 0, 1), CGColorCreateGenericRGB(0, 0.2, 0.2, 1.0)),
                (0.2, 0.9))

        v = CGGradientRetain(gradient)
        self.assertTrue(v is gradient)

        CGGradientRelease(gradient)

if __name__ == "__main__":
    main()
