from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGGradient(TestCase):
    @min_os_level("10.5")
    def testTypes(self):
        self.assertIsCFType(Quartz.CGGradientRef)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(Quartz.kCGGradientDrawsBeforeStartLocation, 1)
        self.assertEqual(Quartz.kCGGradientDrawsAfterEndLocation, 2)

    @min_os_level("10.5")
    def testFunctions(self):
        self.assertIsInstance(Quartz.CGGradientGetTypeID(), int)

        self.assertResultIsCFRetained(Quartz.CGGradientCreateWithColorComponents)
        gradient = Quartz.CGGradientCreateWithColorComponents(
            Quartz.CGColorSpaceCreateDeviceRGB(),
            (0, 0, 0, 1, 0.2, 0.4, 0.2, 1, 0.8, 0.8, 0.8, 1),
            (0, 0.8, 0.95),
            3,
        )
        self.assertIsInstance(gradient, Quartz.CGGradientRef)

        self.assertResultIsCFRetained(Quartz.CGGradientCreateWithColors)
        gradient = Quartz.CGGradientCreateWithColors(
            Quartz.CGColorSpaceCreateDeviceRGB(),
            (
                Quartz.CGColorCreateGenericRGB(0, 0, 0, 1),
                Quartz.CGColorCreateGenericRGB(0, 0.2, 0.2, 1.0),
            ),
            (0.2, 0.9),
        )

        v = Quartz.CGGradientRetain(gradient)
        self.assertTrue(v is gradient)

        Quartz.CGGradientRelease(gradient)
