from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGGradient(TestCase):
    def test_types(self):
        self.assertIsCFType(Quartz.CGGradientRef)

    def test_constants(self):
        self.assertEqual(Quartz.kCGGradientDrawsBeforeStartLocation, 1)
        self.assertEqual(Quartz.kCGGradientDrawsAfterEndLocation, 2)

    def test_functions(self):
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
