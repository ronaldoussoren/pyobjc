
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGDirectPalette (TestCase):
    def testStructs(self):
        v = CGDeviceByteColor()
        self.failUnless(hasattr(v, 'red'))
        self.failUnless(hasattr(v, 'green'))
        self.failUnless(hasattr(v, 'blue'))

        v = CGDeviceColor()
        self.failUnless(hasattr(v, 'red'))
        self.failUnless(hasattr(v, 'green'))
        self.failUnless(hasattr(v, 'blue'))

    def testTypes(self):
        self.failUnlessIsCFType(CGDirectPaletteRef)

    def testFunctions(self):
        self.failUnlessResultIsCFRetained(CGPaletteCreateDefaultColorPalette)
        v = CGPaletteCreateDefaultColorPalette()
        self.failUnlessIsInstance(v, CGDirectPaletteRef)

        self.failUnlessResultIsCFRetained(CGPaletteCreateWithDisplay)
        v = CGPaletteCreateWithDisplay(CGMainDisplayID())
        if v is not None:
            self.failUnlessIsInstance(v, CGDirectPaletteRef)

        self.failUnlessResultIsCFRetained(CGPaletteCreateWithCapacity)
        v = CGPaletteCreateWithCapacity(128)
        self.failUnlessIsInstance(v, CGDirectPaletteRef)

        self.failUnlessResultIsCFRetained(CGPaletteCreateWithSamples)
        v = CGPaletteCreateWithSamples([(0, 0, 0), (0.5, 0.5, 0.5), (1, 1, 1)], 3)
        self.failUnlessIsInstance(v, CGDirectPaletteRef)

        self.failUnlessResultIsCFRetained(CGPaletteCreateWithByteSamples)
        v = CGPaletteCreateWithByteSamples([(0, 0, 0), (100, 100, 100), (255, 255, 255)], 3)
        self.failUnlessIsInstance(v, CGDirectPaletteRef)

        CFRetain(v)
        CGPaletteRelease(v)

        palette = CGPaletteCreateDefaultColorPalette()
        v = CGPaletteGetColorAtIndex(palette, 0)
        self.failUnlessIsInstance(palette, CGDirectPaletteRef)

        v = CGPaletteGetIndexForColor(palette, v)
        self.failUnlessIsInstance(v, (int, long))

        v = CGPaletteGetNumberOfSamples(palette)
        self.failUnlessIsInstance(v, (int, long))

        CGPaletteSetColorAtIndex(palette, (0.5, 0.5, 0.5), 0)

        self.failUnlessResultIsCFRetained(CGPaletteCreateCopy)
        v = CGPaletteCreateCopy(palette)
        self.failUnlessIsInstance(v, CGDirectPaletteRef)

        self.failUnlessResultIsBOOL(CGPaletteIsEqualToPalette)
        v = CGPaletteIsEqualToPalette(palette, v)
        self.failUnless(v is True)

        self.failUnlessResultIsCFRetained(CGPaletteCreateFromPaletteBlendedWithColor)
        v = CGPaletteCreateFromPaletteBlendedWithColor(palette,
                0.5, (0.3, 0.7, 0.1))
        self.failUnlessIsInstance(v, CGDirectPaletteRef)


if __name__ == "__main__":
    main()
