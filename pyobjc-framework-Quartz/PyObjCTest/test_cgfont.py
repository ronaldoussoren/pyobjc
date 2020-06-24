from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCGFont(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGFontRef)

    def testConstants(self):
        self.assertEqual(Quartz.kCGFontPostScriptFormatType1, 1)
        self.assertEqual(Quartz.kCGFontPostScriptFormatType3, 3)
        self.assertEqual(Quartz.kCGFontPostScriptFormatType42, 42)

        self.assertEqual(Quartz.kCGFontIndexMax, ((1 << 16) - 2))
        self.assertEqual(Quartz.kCGFontIndexInvalid, ((1 << 16) - 1))
        self.assertEqual(Quartz.kCGGlyphMax, Quartz.kCGFontIndexMax)

        self.assertIsInstance(Quartz.kCGFontVariationAxisName, str)
        self.assertIsInstance(Quartz.kCGFontVariationAxisMinValue, str)
        self.assertIsInstance(Quartz.kCGFontVariationAxisMaxValue, str)
        self.assertIsInstance(Quartz.kCGFontVariationAxisDefaultValue, str)

        self.assertEqual(Quartz.CGGlyphMin, 0)
        self.assertEqual(Quartz.CGGlyphMax, Quartz.kCGGlyphMax)

    @min_os_level("10.5")
    # Most functions should work on 10.4 as well, except for the convenient
    # contruction functions
    def testFunctions(self):
        self.assertIsInstance(Quartz.CGFontGetTypeID(), int)

        self.assertResultIsCFRetained(Quartz.CGFontCreateWithFontName)
        font = Quartz.CGFontCreateWithFontName("Helvetica")
        self.assertIsInstance(font, Quartz.CGFontRef)

        self.assertResultIsCFRetained(Quartz.CGFontCreateCopyWithVariations)
        font = Quartz.CGFontCreateCopyWithVariations(font, None)
        self.assertIsInstance(font, Quartz.CGFontRef)

        v = Quartz.CGFontRetain(font)
        self.assertTrue(v is font)
        Quartz.CGFontRelease(font)

        v = Quartz.CGFontGetNumberOfGlyphs(font)
        self.assertIsInstance(v, int)

        v = Quartz.CGFontGetUnitsPerEm(font)
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(Quartz.CGFontCopyPostScriptName)
        v = Quartz.CGFontCopyPostScriptName(font)
        self.assertIsInstance(v, str)

        self.assertResultIsCFRetained(Quartz.CGFontCopyFullName)
        v = Quartz.CGFontCopyFullName(font)
        self.assertIsInstance(v, str)

        v = Quartz.CGFontGetAscent(font)
        self.assertIsInstance(v, int)

        v = Quartz.CGFontGetDescent(font)
        self.assertIsInstance(v, int)

        v = Quartz.CGFontGetLeading(font)
        self.assertIsInstance(v, int)

        v = Quartz.CGFontGetCapHeight(font)
        self.assertIsInstance(v, int)

        v = Quartz.CGFontGetXHeight(font)
        self.assertIsInstance(v, int)

        v = Quartz.CGFontGetFontBBox(font)
        self.assertIsInstance(v, Quartz.CGRect)

        v = Quartz.CGFontGetItalicAngle(font)
        self.assertIsInstance(v, float)

        v = Quartz.CGFontGetStemV(font)
        self.assertIsInstance(v, float)

        v = Quartz.CGFontCopyVariationAxes(font)
        self.assertTrue(v is None or isinstance(v, Quartz.CFArrayRef))

        v = Quartz.CGFontCopyVariations(font)
        self.assertTrue(v is None or isinstance(v, Quartz.CFDictionaryRef))

        self.assertResultHasType(Quartz.CGFontCanCreatePostScriptSubset, objc._C_BOOL)
        v = Quartz.CGFontCanCreatePostScriptSubset(
            font, Quartz.kCGFontPostScriptFormatType1
        )
        self.assertIsInstance(v, bool)

        # PyObjC doesn't wrap ATSUI, therefore we cannot actually call
        # the function.
        # self.fail('CGFontCreateWithPlatformFont')
        self.assertArgHasType(
            Quartz.CGFontCreateWithPlatformFont, 0, objc._C_PTR + objc._C_VOID
        )
        self.assertResultIsCFRetained(Quartz.CGFontCreateWithPlatformFont)

        # data = open('/Library/Fonts/Webdings.ttf', 'rb').read()
        # with open('/Library/Fonts/Courier New.ttf', 'rb') as fp:
        #    data = fp.read()
        with open("/System/Library/Fonts/Symbol.ttf", "rb") as fp:
            data = fp.read()
        self.assertResultIsCFRetained(Quartz.CGFontCreateWithDataProvider)
        font = Quartz.CGFontCreateWithDataProvider(
            Quartz.CGDataProviderCreateWithCFData(data)
        )
        self.assertIsInstance(font, Quartz.CGFontRef)

        tags = Quartz.CGFontCopyTableTags(font)
        self.assertIsInstance(tags, tuple)
        self.assertNotEqual(len(tags), 0)
        self.assertIsInstance(tags[0], int)

        self.assertResultIsCFRetained(Quartz.CGFontCopyTableForTag)
        for _ in tags:
            data = Quartz.CGFontCopyTableForTag(font, 0)
            if data is None:
                continue
            self.assertIsInstance(data, Quartz.CFDataRef)

        v = Quartz.CGFontCopyGlyphNameForGlyph(font, ord("A"))
        self.assertIsInstance(v, str)

        glyphnames = ["chat", "conference", "woman"]

        v = Quartz.CGFontGetGlyphWithGlyphName(font, glyphnames[0])
        self.assertIsInstance(v, int)

        glyphs = [Quartz.CGFontGetGlyphWithGlyphName(font, nm) for nm in glyphnames]

        self.assertResultHasType(Quartz.CGFontGetGlyphAdvances, objc._C_BOOL)
        v, advances = Quartz.CGFontGetGlyphAdvances(font, glyphs, len(glyphs), None)
        self.assertIsInstance(v, bool)
        self.assertEqual(len(advances), 3)
        for v in advances:
            self.assertIsInstance(v, int)

        self.assertResultHasType(Quartz.CGFontGetGlyphBBoxes, objc._C_BOOL)
        v, bboxes = Quartz.CGFontGetGlyphBBoxes(font, glyphs, len(glyphs), None)
        self.assertIsInstance(v, bool)
        self.assertEqual(len(bboxes), 3)
        for v in bboxes:
            self.assertIsInstance(v, Quartz.CGRect)

        self.assertResultIsCFRetained(Quartz.CGFontCreatePostScriptSubset)
        psfont = Quartz.CGFontCreatePostScriptSubset(
            font,
            "pyobjc-characters",
            Quartz.kCGFontPostScriptFormatType42,
            glyphs,
            len(glyphs),
            None,
        )
        if psfont is not None:
            self.assertIsInstance(psfont, Quartz.CFDataRef)

        self.assertResultIsCFRetained(Quartz.CGFontCreatePostScriptEncoding)
        glyph_map = glyphs + [0] * (256 - len(glyphs))
        psfont = Quartz.CGFontCreatePostScriptEncoding(font, glyph_map)
        self.assertIsInstance(psfont, Quartz.CFDataRef)
