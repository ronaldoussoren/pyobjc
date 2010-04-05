
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGColor (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGColorRef)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        self.assertResultIsCFRetained(CGColorCreateGenericGray)
        color = CGColorCreateGenericGray(0.75, 0.8)
        self.assertIsInstance(color, CGColorRef)

        self.assertResultIsCFRetained(CGColorCreateGenericRGB)
        color = CGColorCreateGenericRGB(0.75, 0.8, 1.0, 0.5)
        self.assertIsInstance(color, CGColorRef)

        self.assertResultIsCFRetained(CGColorCreateGenericCMYK)
        color = CGColorCreateGenericCMYK(0.75, 0.8, 0.5, 1.0, 0.5)
        self.assertIsInstance(color, CGColorRef)

        color = CGColorGetConstantColor(kCGColorWhite)
        self.assertIsInstance(color, CGColorRef)

    def testFunctions(self):
        self.assertResultIsCFRetained(CGColorCreate)
        color = CGColorCreate(CGColorSpaceCreateDeviceRGB(),
                [1.0, 0.5, 0.5])
        self.assertIsInstance(color, CGColorRef)

        self.assertResultIsCFRetained(CGColorCreateCopy)
        v = CGColorCreateCopy(color)
        self.assertIsInstance(v, CGColorRef)

        self.assertResultIsCFRetained(CGColorCreateCopyWithAlpha)
        v = CGColorCreateCopyWithAlpha(color, 0.7)
        self.assertIsInstance(v, CGColorRef)

        CGColorRetain(color)
        CGColorRelease(color)

        self.assertResultHasType(CGColorEqualToColor, objc._C_BOOL)
        self.assertTrue(CGColorEqualToColor(color, color) is True)
        self.assertTrue(CGColorEqualToColor(color, v) is False)

        self.assertEqual(CGColorGetNumberOfComponents(color), 4)
        v = CGColorGetComponents(color)
        self.assertIsInstance(v, objc.varlist)
        self.assertIsInstance(v[0], float)

        v = CGColorGetAlpha(color)
        self.assertIsInstance(v, float)

        v = CGColorGetColorSpace(color)
        self.assertIsInstance(v, CGColorSpaceRef)

        v = CGColorGetPattern(color)
        self.assertTrue(v is None)

        self.assertIsInstance(CGColorGetTypeID(), (int, long))

        # CGColorCreateWithPattern, CGColorGetPattern: tested in test_cgpattern

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(kCGColorWhite, unicode)
        self.assertIsInstance(kCGColorBlack, unicode)
        self.assertIsInstance(kCGColorClear, unicode)

if __name__ == "__main__":
    main()
