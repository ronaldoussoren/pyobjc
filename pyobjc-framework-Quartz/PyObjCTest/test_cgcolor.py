from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCGColor(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGColorRef)

    @min_os_level("10.15")
    def testFunctions10_15(self):
        self.assertResultIsCFRetained(Quartz.CGColorCreateGenericGrayGamma2_2)
        color = Quartz.CGColorCreateGenericGrayGamma2_2(1.5, 0.3)
        self.assertIsInstance(color, Quartz.CGColorRef)

    @min_os_level("10.11")
    def testFunctions10_11(self):
        self.assertResultIsCFRetained(Quartz.CGColorCreateCopyByMatchingToColorSpace)
        color = Quartz.CGColorCreateCopyByMatchingToColorSpace(
            Quartz.CGColorSpaceCreateDeviceGray(),
            Quartz.kCGRenderingIntentDefault,
            Quartz.CGColorCreateGenericGray(0.75, 0.8),
            None,
        )
        self.assertIsInstance(color, Quartz.CGColorRef)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        self.assertResultIsCFRetained(Quartz.CGColorCreateGenericGray)
        color = Quartz.CGColorCreateGenericGray(0.75, 0.8)
        self.assertIsInstance(color, Quartz.CGColorRef)

        self.assertResultIsCFRetained(Quartz.CGColorCreateGenericRGB)
        color = Quartz.CGColorCreateGenericRGB(0.75, 0.8, 1.0, 0.5)
        self.assertIsInstance(color, Quartz.CGColorRef)

        self.assertResultIsCFRetained(Quartz.CGColorCreateGenericCMYK)
        color = Quartz.CGColorCreateGenericCMYK(0.75, 0.8, 0.5, 1.0, 0.5)
        self.assertIsInstance(color, Quartz.CGColorRef)

        color = Quartz.CGColorGetConstantColor(Quartz.kCGColorWhite)
        self.assertIsInstance(color, Quartz.CGColorRef)

    def testFunctions(self):
        self.assertResultIsCFRetained(Quartz.CGColorCreate)
        color = Quartz.CGColorCreate(
            Quartz.CGColorSpaceCreateDeviceRGB(), [1.0, 0.5, 0.5]
        )
        self.assertIsInstance(color, Quartz.CGColorRef)

        self.assertResultIsCFRetained(Quartz.CGColorCreateCopy)
        v = Quartz.CGColorCreateCopy(color)
        self.assertIsInstance(v, Quartz.CGColorRef)

        self.assertResultIsCFRetained(Quartz.CGColorCreateCopyWithAlpha)
        v = Quartz.CGColorCreateCopyWithAlpha(color, 0.7)
        self.assertIsInstance(v, Quartz.CGColorRef)

        Quartz.CGColorRetain(color)
        Quartz.CGColorRelease(color)

        self.assertResultHasType(Quartz.CGColorEqualToColor, objc._C_BOOL)
        self.assertTrue(Quartz.CGColorEqualToColor(color, color) is True)
        self.assertTrue(Quartz.CGColorEqualToColor(color, v) is False)

        self.assertEqual(Quartz.CGColorGetNumberOfComponents(color), 4)
        v = Quartz.CGColorGetComponents(color)
        self.assertIsInstance(v, objc.varlist)
        self.assertIsInstance(v[0], float)

        v = Quartz.CGColorGetAlpha(color)
        self.assertIsInstance(v, float)

        v = Quartz.CGColorGetColorSpace(color)
        self.assertIsInstance(v, Quartz.CGColorSpaceRef)

        v = Quartz.CGColorGetPattern(color)
        self.assertTrue(v is None)

        self.assertIsInstance(Quartz.CGColorGetTypeID(), int)

        # Quartz.CGColorCreateWithPattern, Quartz.CGColorGetPattern: tested in test_cgpattern

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.kCGColorWhite, str)
        self.assertIsInstance(Quartz.kCGColorBlack, str)
        self.assertIsInstance(Quartz.kCGColorClear, str)
