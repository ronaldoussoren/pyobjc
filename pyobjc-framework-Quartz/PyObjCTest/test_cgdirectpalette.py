
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGDirectPalette (TestCase):
    def testStructs(self):
        v = CGDeviceByteColor()
        self.assertTrue(hasattr(v, 'red'))
        self.assertTrue(hasattr(v, 'green'))
        self.assertTrue(hasattr(v, 'blue'))

        v = CGDeviceColor()
        self.assertTrue(hasattr(v, 'red'))
        self.assertTrue(hasattr(v, 'green'))
        self.assertTrue(hasattr(v, 'blue'))

    def testTypes(self):
        self.assertIsOpaquePointer(CGDirectPaletteRef)

    def testFunctions(self):
        self.assertResultIsCFRetained(CGPaletteCreateDefaultColorPalette)
        v = CGPaletteCreateDefaultColorPalette()
        self.assertIsInstance(v, CGDirectPaletteRef)

        self.assertResultIsCFRetained(CGPaletteCreateWithDisplay)
        v = CGPaletteCreateWithDisplay(CGMainDisplayID())
        if v is not None:
            self.assertIsInstance(v, CGDirectPaletteRef)

        self.assertResultIsCFRetained(CGPaletteCreateWithCapacity)
        v = CGPaletteCreateWithCapacity(128)
        self.assertIsInstance(v, CGDirectPaletteRef)

        self.assertResultIsCFRetained(CGPaletteCreateWithSamples)
        v = CGPaletteCreateWithSamples([(0, 0, 0), (0.5, 0.5, 0.5), (1, 1, 1)], 3)
        self.assertIsInstance(v, CGDirectPaletteRef)

        self.assertResultIsCFRetained(CGPaletteCreateWithByteSamples)
        v = CGPaletteCreateWithByteSamples([(0, 0, 0), (100, 100, 100), (255, 255, 255)], 3)
        self.assertIsInstance(v, CGDirectPaletteRef)

        CFRetain(v)
        CGPaletteRelease(v)

        palette = CGPaletteCreateDefaultColorPalette()
        v = CGPaletteGetColorAtIndex(palette, 0)
        self.assertIsInstance(palette, CGDirectPaletteRef)

        v = CGPaletteGetIndexForColor(palette, v)
        self.assertIsInstance(v, (int, long))

        v = CGPaletteGetNumberOfSamples(palette)
        self.assertIsInstance(v, (int, long))

        CGPaletteSetColorAtIndex(palette, (0.5, 0.5, 0.5), 0)

        self.assertResultIsCFRetained(CGPaletteCreateCopy)
        v = CGPaletteCreateCopy(palette)
        self.assertIsInstance(v, CGDirectPaletteRef)

        self.assertResultHasType(CGPaletteIsEqualToPalette, objc._C_BOOL)
        v = CGPaletteIsEqualToPalette(palette, v)
        self.assertTrue(v is True)

        self.assertResultIsCFRetained(CGPaletteCreateFromPaletteBlendedWithColor)
        v = CGPaletteCreateFromPaletteBlendedWithColor(palette,
                0.5, (0.3, 0.7, 0.1))
        self.assertIsInstance(v, CGDirectPaletteRef)


if __name__ == "__main__":
    main()
