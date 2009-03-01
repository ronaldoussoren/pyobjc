
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGFont (TestCase):

    def testTypes(self):
        self.failUnlessIsCFType(CGFontRef)

    def testConstants(self):
        self.failUnlessEqual(kCGFontPostScriptFormatType1, 1)
        self.failUnlessEqual(kCGFontPostScriptFormatType3, 3)
        self.failUnlessEqual(kCGFontPostScriptFormatType42, 42)

        self.failUnlessEqual(kCGFontIndexMax, ((1 << 16) - 2))
        self.failUnlessEqual(kCGFontIndexInvalid, ((1 << 16) - 1))
        self.failUnlessEqual(kCGGlyphMax, kCGFontIndexMax)


        self.failUnlessIsInstance(kCGFontVariationAxisName, unicode)
        self.failUnlessIsInstance(kCGFontVariationAxisMinValue, unicode)
        self.failUnlessIsInstance(kCGFontVariationAxisMaxValue, unicode)
        self.failUnlessIsInstance(kCGFontVariationAxisDefaultValue, unicode)

        self.failUnlessEqual(CGGlyphMin, 0)
        self.failUnlessEqual(CGGlyphMax, kCGGlyphMax)



    def testFunctions(self):
        self.failUnlessIsInstance(CGFontGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(CGFontCreateWithFontName)
        font = CGFontCreateWithFontName("Helvetica")
        self.failUnlessIsInstance(font, CGFontRef)

        self.failUnlessResultIsCFRetained(CGFontCreateCopyWithVariations)
        font = CGFontCreateCopyWithVariations(font, None)
        self.failUnlessIsInstance(font, CGFontRef)

        v = CGFontRetain(font)
        self.failUnless(v is font)
        CGFontRelease(font)

        v = CGFontGetNumberOfGlyphs(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CGFontGetUnitsPerEm(font)
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsCFRetained(CGFontCopyPostScriptName)
        v = CGFontCopyPostScriptName(font)
        self.failUnlessIsInstance(v, unicode)

        self.failUnlessResultIsCFRetained(CGFontCopyFullName)
        v = CGFontCopyFullName(font)
        self.failUnlessIsInstance(v, unicode)

        v = CGFontGetAscent(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CGFontGetDescent(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CGFontGetLeading(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CGFontGetCapHeight(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CGFontGetXHeight(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CGFontGetFontBBox(font)
        self.failUnlessIsInstance(v, CGRect)

        v = CGFontGetItalicAngle(font)
        self.failUnlessIsInstance(v, float)

        v = CGFontGetStemV(font)
        self.failUnlessIsInstance(v, float)

        v = CGFontCopyVariationAxes(font)
        self.failUnless(v is None or isinstance(v, CFArrayRef))

        v = CGFontCopyVariations(font)
        self.failUnless(v is None or isinstance(v, CFDictionaryRef))

        self.failUnlessResultHasType(CGFontCanCreatePostScriptSubset, objc._C_BOOL)
        v = CGFontCanCreatePostScriptSubset(font, kCGFontPostScriptFormatType1)
        self.failUnlessIsInstance(v, bool)
        




    def testMissing(self):
        self.fail('GFontCreateWithPlatformFont')
        self.fail('CGFontCreateWithDataProvider')
        self.fail('CGFontGetGlyphAdvances')
        self.fail('CGFontGetGlyphBBoxes')
        self.fail('CGFontGetGlyphWithGlyphName')
        self.fail('CGFontCopyGlyphNameForGlyph')
        self.fail('CGFontCreatePostScriptSubset')
        self.fail('CGFontCreatePostScriptEncoding')
        self.fail('CGFontCopyTableTags')
        self.fail('CGFontCopyTableForTag')
    


if __name__ == "__main__":
    main()
