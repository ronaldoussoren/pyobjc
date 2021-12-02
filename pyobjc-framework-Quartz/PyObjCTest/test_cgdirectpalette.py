from PyObjCTools.TestSupport import TestCase
import Quartz
import objc


class TestCGDirectPalette(TestCase):
    def testStructs(self):
        v = Quartz.CGDeviceByteColor()
        self.assertTrue(hasattr(v, "red"))
        self.assertTrue(hasattr(v, "green"))
        self.assertTrue(hasattr(v, "blue"))
        self.assertPickleRoundTrips(v)

        v = Quartz.CGDeviceColor()
        self.assertTrue(hasattr(v, "red"))
        self.assertTrue(hasattr(v, "green"))
        self.assertTrue(hasattr(v, "blue"))
        self.assertPickleRoundTrips(v)

    def testTypes(self):
        self.assertIsOpaquePointer(Quartz.CGDirectPaletteRef)

    def testFunctions(self):
        self.assertResultIsCFRetained(Quartz.CGPaletteCreateDefaultColorPalette)
        v = Quartz.CGPaletteCreateDefaultColorPalette()
        self.assertIsInstance(v, Quartz.CGDirectPaletteRef)

        self.assertResultIsCFRetained(Quartz.CGPaletteCreateWithDisplay)
        v = Quartz.CGPaletteCreateWithDisplay(Quartz.CGMainDisplayID())
        if v is not None:
            self.assertIsInstance(v, Quartz.CGDirectPaletteRef)

        self.assertResultIsCFRetained(Quartz.CGPaletteCreateWithCapacity)
        v = Quartz.CGPaletteCreateWithCapacity(128)
        self.assertIsInstance(v, Quartz.CGDirectPaletteRef)

        self.assertResultIsCFRetained(Quartz.CGPaletteCreateWithSamples)
        v = Quartz.CGPaletteCreateWithSamples(
            [(0, 0, 0), (0.5, 0.5, 0.5), (1, 1, 1)], 3
        )
        self.assertIsInstance(v, Quartz.CGDirectPaletteRef)

        self.assertResultIsCFRetained(Quartz.CGPaletteCreateWithByteSamples)
        v = Quartz.CGPaletteCreateWithByteSamples(
            [(0, 0, 0), (100, 100, 100), (255, 255, 255)], 3
        )
        self.assertIsInstance(v, Quartz.CGDirectPaletteRef)

        Quartz.CFRetain(v)
        Quartz.CGPaletteRelease(v)

        palette = Quartz.CGPaletteCreateDefaultColorPalette()
        v = Quartz.CGPaletteGetColorAtIndex(palette, 0)
        self.assertIsInstance(palette, Quartz.CGDirectPaletteRef)

        v = Quartz.CGPaletteGetIndexForColor(palette, v)
        self.assertIsInstance(v, int)

        v = Quartz.CGPaletteGetNumberOfSamples(palette)
        self.assertIsInstance(v, int)

        Quartz.CGPaletteSetColorAtIndex(palette, (0.5, 0.5, 0.5), 0)

        self.assertResultIsCFRetained(Quartz.CGPaletteCreateCopy)
        v = Quartz.CGPaletteCreateCopy(palette)
        self.assertIsInstance(v, Quartz.CGDirectPaletteRef)

        self.assertResultHasType(Quartz.CGPaletteIsEqualToPalette, objc._C_BOOL)
        v = Quartz.CGPaletteIsEqualToPalette(palette, v)
        self.assertTrue(v is True)

        self.assertResultIsCFRetained(Quartz.CGPaletteCreateFromPaletteBlendedWithColor)
        v = Quartz.CGPaletteCreateFromPaletteBlendedWithColor(
            palette, 0.5, (0.3, 0.7, 0.1)
        )
        self.assertIsInstance(v, Quartz.CGDirectPaletteRef)
