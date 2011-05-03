
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

import sys

if sys.version_info[0] != 2:
    def buffer(value):
        if isinstance(value, bytes):
            return value
        return value.encode('latin1')

class TestCGFont (TestCase):

    def testTypes(self):
        self.assertIsCFType(CGFontRef)

    def testConstants(self):
        self.assertEqual(kCGFontPostScriptFormatType1, 1)
        self.assertEqual(kCGFontPostScriptFormatType3, 3)
        self.assertEqual(kCGFontPostScriptFormatType42, 42)

        self.assertEqual(kCGFontIndexMax, ((1 << 16) - 2))
        self.assertEqual(kCGFontIndexInvalid, ((1 << 16) - 1))
        self.assertEqual(kCGGlyphMax, kCGFontIndexMax)


        self.assertIsInstance(kCGFontVariationAxisName, unicode)
        self.assertIsInstance(kCGFontVariationAxisMinValue, unicode)
        self.assertIsInstance(kCGFontVariationAxisMaxValue, unicode)
        self.assertIsInstance(kCGFontVariationAxisDefaultValue, unicode)

        self.assertEqual(CGGlyphMin, 0)
        self.assertEqual(CGGlyphMax, kCGGlyphMax)



    @min_os_level('10.5')
    # Most functions should work on 10.4 as well, except for the convenient 
    # contruction functions
    def testFunctions(self):
        self.assertIsInstance(CGFontGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CGFontCreateWithFontName)
        font = CGFontCreateWithFontName("Helvetica")
        self.assertIsInstance(font, CGFontRef)

        self.assertResultIsCFRetained(CGFontCreateCopyWithVariations)
        font = CGFontCreateCopyWithVariations(font, None)
        self.assertIsInstance(font, CGFontRef)

        v = CGFontRetain(font)
        self.assertTrue(v is font)
        CGFontRelease(font)

        v = CGFontGetNumberOfGlyphs(font)
        self.assertIsInstance(v, (int, long))

        v = CGFontGetUnitsPerEm(font)
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(CGFontCopyPostScriptName)
        v = CGFontCopyPostScriptName(font)
        self.assertIsInstance(v, unicode)

        self.assertResultIsCFRetained(CGFontCopyFullName)
        v = CGFontCopyFullName(font)
        self.assertIsInstance(v, unicode)

        v = CGFontGetAscent(font)
        self.assertIsInstance(v, (int, long))

        v = CGFontGetDescent(font)
        self.assertIsInstance(v, (int, long))

        v = CGFontGetLeading(font)
        self.assertIsInstance(v, (int, long))

        v = CGFontGetCapHeight(font)
        self.assertIsInstance(v, (int, long))

        v = CGFontGetXHeight(font)
        self.assertIsInstance(v, (int, long))

        v = CGFontGetFontBBox(font)
        self.assertIsInstance(v, CGRect)

        v = CGFontGetItalicAngle(font)
        self.assertIsInstance(v, float)

        v = CGFontGetStemV(font)
        self.assertIsInstance(v, float)

        v = CGFontCopyVariationAxes(font)
        self.assertTrue(v is None or isinstance(v, CFArrayRef))

        v = CGFontCopyVariations(font)
        self.assertTrue(v is None or isinstance(v, CFDictionaryRef))

        self.assertResultHasType(CGFontCanCreatePostScriptSubset, objc._C_BOOL)
        v = CGFontCanCreatePostScriptSubset(font, kCGFontPostScriptFormatType1)
        self.assertIsInstance(v, bool)
        

        # PyObjC doesn't wrap ATSUI, therefore we cannot actually call
        # the function.
        #self.fail('CGFontCreateWithPlatformFont')
        self.assertArgHasType(CGFontCreateWithPlatformFont, 0,
                objc._C_UINT)
        self.assertResultIsCFRetained(CGFontCreateWithPlatformFont)


        data = open('/Library/Fonts/Webdings.ttf', 'rb').read()
        self.assertResultIsCFRetained(CGFontCreateWithDataProvider)
        font = CGFontCreateWithDataProvider(
                CGDataProviderCreateWithCFData(buffer(data))
        )
        self.assertIsInstance(font, CGFontRef)

        tags = CGFontCopyTableTags(font)
        self.assertIsInstance(tags, tuple)
        self.failIfEqual(len(tags), 0)
        self.assertIsInstance(tags[0], (int, long))

        self.assertResultIsCFRetained(CGFontCopyTableForTag)
        for tg in tags:
            data = CGFontCopyTableForTag(font, 0)
            if data is None:
                continue
            self.assertIsInstance(data, CFDataRef)

        v = CGFontCopyGlyphNameForGlyph(font, ord('A'))
        self.assertIsInstance(v, unicode)

        glyphnames = ['chat', 'conference', 'woman' ]

        v = CGFontGetGlyphWithGlyphName(font, glyphnames[0])
        self.assertIsInstance(v, (int, long))

        glyphs = [ CGFontGetGlyphWithGlyphName(font, nm)
                    for nm in glyphnames ]

        self.assertResultHasType(CGFontGetGlyphAdvances, objc._C_BOOL)
        v, advances = CGFontGetGlyphAdvances(
                font, glyphs, len(glyphs), None)
        self.assertIsInstance(v, bool)
        self.assertEqual(len(advances), 3)
        for v in advances:
            self.assertIsInstance(v, (int, long))

        self.assertResultHasType(CGFontGetGlyphBBoxes, objc._C_BOOL)
        v, bboxes = CGFontGetGlyphBBoxes(
                font, glyphs, len(glyphs), None)
        self.assertIsInstance(v, bool)
        self.assertEqual(len(bboxes), 3)
        for v in bboxes:
            self.assertIsInstance(v, CGRect)

        self.assertResultIsCFRetained(CGFontCreatePostScriptSubset)
        psfont = CGFontCreatePostScriptSubset(
                font, "pybobjc-characters",
                kCGFontPostScriptFormatType42,
                glyphs, len(glyphs), None)
        self.assertIsInstance(psfont, CFDataRef)


        self.assertResultIsCFRetained(CGFontCreatePostScriptEncoding)
        map = glyphs + [0]*(256-len(glyphs))
        psfont = CGFontCreatePostScriptEncoding(
                font, map)
        self.assertIsInstance(psfont, CFDataRef)
    


if __name__ == "__main__":
    main()
