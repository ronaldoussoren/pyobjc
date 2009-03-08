
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
        

        # PyObjC doesn't wrap ATSUI, therefore we cannot actually call
        # the function.
        #self.fail('CGFontCreateWithPlatformFont')
        self.failUnlessArgHasType(CGFontCreateWithPlatformFont, 0,
                objc._C_UINT)
        self.failUnlessResultIsCFRetained(CGFontCreateWithPlatformFont)


        data = open('/Library/Fonts/Webdings.ttf', 'rb').read()
        self.failUnlessResultIsCFRetained(CGFontCreateWithDataProvider)
        font = CGFontCreateWithDataProvider(
                CGDataProviderCreateWithCFData(buffer(data))
        )
        self.failUnlessIsInstance(font, CGFontRef)

        tags = CGFontCopyTableTags(font)
        self.failUnlessIsInstance(tags, tuple)
        self.failIfEqual(len(tags), 0)
        self.failUnlessIsInstance(tags[0], (int, long))

        self.failUnlessResultIsCFRetained(CGFontCopyTableForTag)
        for tg in tags:
            data = CGFontCopyTableForTag(font, 0)
            if data is None:
                continue
            self.failUnlessIsInstance(data, CFDataRef)

        v = CGFontCopyGlyphNameForGlyph(font, ord('A'))
        self.failUnlessIsInstance(v, unicode)

        glyphnames = ['chat', 'conference', 'woman' ]

        v = CGFontGetGlyphWithGlyphName(font, glyphnames[0])
        self.failUnlessIsInstance(v, (int, long))

        glyphs = [ CGFontGetGlyphWithGlyphName(font, nm)
                    for nm in glyphnames ]

        self.failUnlessResultHasType(CGFontGetGlyphAdvances, objc._C_BOOL)
        v, advances = CGFontGetGlyphAdvances(
                font, glyphs, len(glyphs), None)
        self.failUnlessIsInstance(v, bool)
        self.failUnlessEqual(len(advances), 3)
        for v in advances:
            self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultHasType(CGFontGetGlyphBBoxes, objc._C_BOOL)
        v, bboxes = CGFontGetGlyphBBoxes(
                font, glyphs, len(glyphs), None)
        self.failUnlessIsInstance(v, bool)
        self.failUnlessEqual(len(bboxes), 3)
        for v in bboxes:
            self.failUnlessIsInstance(v, CGRect)

        self.failUnlessResultIsCFRetained(CGFontCreatePostScriptSubset)
        psfont = CGFontCreatePostScriptSubset(
                font, "pybobjc-characters",
                kCGFontPostScriptFormatType42,
                glyphs, len(glyphs), None)
        self.failUnlessIsInstance(psfont, CFDataRef)


        self.failUnlessResultIsCFRetained(CGFontCreatePostScriptEncoding)
        map = glyphs + [0]*(256-len(glyphs))
        psfont = CGFontCreatePostScriptEncoding(
                font, map)
        self.failUnlessIsInstance(psfont, CFDataRef)
    


if __name__ == "__main__":
    main()
