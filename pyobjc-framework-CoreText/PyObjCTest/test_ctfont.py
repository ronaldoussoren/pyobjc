import CoreText
import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level, fourcc
import objc


class TestCTFont(TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreText.CTFontRef, objc.objc_class)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreText.kCTFontOptionsDefault, 0)
        self.assertEqual(CoreText.kCTFontOptionsPreventAutoActivation, 1 << 0)
        self.assertEqual(CoreText.kCTFontOptionsPreferSystemFont, 1 << 2)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(CoreText.kCTBaselineClassHanging, str)
        self.assertIsInstance(CoreText.kCTBaselineClassIdeographicCentered, str)
        self.assertIsInstance(CoreText.kCTBaselineClassIdeographicHigh, str)
        self.assertIsInstance(CoreText.kCTBaselineClassIdeographicLow, str)
        self.assertIsInstance(CoreText.kCTBaselineClassMath, str)
        self.assertIsInstance(CoreText.kCTBaselineClassRoman, str)
        self.assertIsInstance(CoreText.kCTBaselineOriginalFont, str)
        self.assertIsInstance(CoreText.kCTBaselineReferenceFont, str)

        self.assertEqual(CoreText.kCTFontTableAnkr, fourcc(b"ankr"))

        self.assertEqual(CoreText.kCTFontUIFontNone, 0xFFFFFFFF)
        self.assertEqual(CoreText.kCTFontUIFontUser, 0)
        self.assertEqual(CoreText.kCTFontUIFontUserFixedPitch, 1)
        self.assertEqual(CoreText.kCTFontUIFontSystem, 2)
        self.assertEqual(CoreText.kCTFontUIFontEmphasizedSystem, 3)
        self.assertEqual(CoreText.kCTFontUIFontSmallSystem, 4)
        self.assertEqual(CoreText.kCTFontUIFontSmallEmphasizedSystem, 5)
        self.assertEqual(CoreText.kCTFontUIFontMiniSystem, 6)
        self.assertEqual(CoreText.kCTFontUIFontMiniEmphasizedSystem, 7)
        self.assertEqual(CoreText.kCTFontUIFontViews, 8)
        self.assertEqual(CoreText.kCTFontUIFontApplication, 9)
        self.assertEqual(CoreText.kCTFontUIFontLabel, 10)
        self.assertEqual(CoreText.kCTFontUIFontMenuTitle, 11)
        self.assertEqual(CoreText.kCTFontUIFontMenuItem, 12)
        self.assertEqual(CoreText.kCTFontUIFontMenuItemMark, 13)
        self.assertEqual(CoreText.kCTFontUIFontMenuItemCmdKey, 14)
        self.assertEqual(CoreText.kCTFontUIFontWindowTitle, 15)
        self.assertEqual(CoreText.kCTFontUIFontPushButton, 16)
        self.assertEqual(CoreText.kCTFontUIFontUtilityWindowTitle, 17)
        self.assertEqual(CoreText.kCTFontUIFontAlertHeader, 18)
        self.assertEqual(CoreText.kCTFontUIFontSystemDetail, 19)
        self.assertEqual(CoreText.kCTFontUIFontEmphasizedSystemDetail, 20)
        self.assertEqual(CoreText.kCTFontUIFontToolbar, 21)
        self.assertEqual(CoreText.kCTFontUIFontSmallToolbar, 22)
        self.assertEqual(CoreText.kCTFontUIFontMessage, 23)
        self.assertEqual(CoreText.kCTFontUIFontPalette, 24)
        self.assertEqual(CoreText.kCTFontUIFontToolTip, 25)
        self.assertEqual(CoreText.kCTFontUIFontControlContent, 26)

    def testConstants(self):
        self.assertIsInstance(CoreText.kCTFontCopyrightNameKey, str)
        self.assertIsInstance(CoreText.kCTFontFamilyNameKey, str)
        self.assertIsInstance(CoreText.kCTFontSubFamilyNameKey, str)
        self.assertIsInstance(CoreText.kCTFontStyleNameKey, str)
        self.assertIsInstance(CoreText.kCTFontUniqueNameKey, str)
        self.assertIsInstance(CoreText.kCTFontFullNameKey, str)
        self.assertIsInstance(CoreText.kCTFontVersionNameKey, str)
        self.assertIsInstance(CoreText.kCTFontPostScriptNameKey, str)
        self.assertIsInstance(CoreText.kCTFontTrademarkNameKey, str)
        self.assertIsInstance(CoreText.kCTFontManufacturerNameKey, str)
        self.assertIsInstance(CoreText.kCTFontDesignerNameKey, str)
        self.assertIsInstance(CoreText.kCTFontDescriptionNameKey, str)
        self.assertIsInstance(CoreText.kCTFontVendorURLNameKey, str)
        self.assertIsInstance(CoreText.kCTFontDesignerURLNameKey, str)
        self.assertIsInstance(CoreText.kCTFontLicenseNameKey, str)
        self.assertIsInstance(CoreText.kCTFontLicenseURLNameKey, str)
        self.assertIsInstance(CoreText.kCTFontSampleTextNameKey, str)
        self.assertIsInstance(CoreText.kCTFontPostScriptCIDNameKey, str)

        self.assertEqual(CoreText.kCTFontNoFontType, 4_294_967_295)  # (uint32_t)-1
        self.assertEqual(CoreText.kCTFontUserFontType, 0)
        self.assertEqual(CoreText.kCTFontUserFixedPitchFontType, 1)
        self.assertEqual(CoreText.kCTFontSystemFontType, 2)
        self.assertEqual(CoreText.kCTFontEmphasizedSystemFontType, 3)
        self.assertEqual(CoreText.kCTFontSmallSystemFontType, 4)
        self.assertEqual(CoreText.kCTFontSmallEmphasizedSystemFontType, 5)
        self.assertEqual(CoreText.kCTFontMiniSystemFontType, 6)
        self.assertEqual(CoreText.kCTFontMiniEmphasizedSystemFontType, 7)
        self.assertEqual(CoreText.kCTFontViewsFontType, 8)
        self.assertEqual(CoreText.kCTFontApplicationFontType, 9)
        self.assertEqual(CoreText.kCTFontLabelFontType, 10)
        self.assertEqual(CoreText.kCTFontMenuTitleFontType, 11)
        self.assertEqual(CoreText.kCTFontMenuItemFontType, 12)
        self.assertEqual(CoreText.kCTFontMenuItemMarkFontType, 13)
        self.assertEqual(CoreText.kCTFontMenuItemCmdKeyFontType, 14)
        self.assertEqual(CoreText.kCTFontWindowTitleFontType, 15)
        self.assertEqual(CoreText.kCTFontPushButtonFontType, 16)
        self.assertEqual(CoreText.kCTFontUtilityWindowTitleFontType, 17)
        self.assertEqual(CoreText.kCTFontAlertHeaderFontType, 18)
        self.assertEqual(CoreText.kCTFontSystemDetailFontType, 19)
        self.assertEqual(CoreText.kCTFontEmphasizedSystemDetailFontType, 20)
        self.assertEqual(CoreText.kCTFontToolbarFontType, 21)
        self.assertEqual(CoreText.kCTFontSmallToolbarFontType, 22)
        self.assertEqual(CoreText.kCTFontMessageFontType, 23)
        self.assertEqual(CoreText.kCTFontPaletteFontType, 24)
        self.assertEqual(CoreText.kCTFontToolTipFontType, 25)
        self.assertEqual(CoreText.kCTFontControlContentFontType, 26)

        self.assertIsInstance(CoreText.kCTFontVariationAxisIdentifierKey, str)
        self.assertIsInstance(CoreText.kCTFontVariationAxisMinimumValueKey, str)
        self.assertIsInstance(CoreText.kCTFontVariationAxisMaximumValueKey, str)
        self.assertIsInstance(CoreText.kCTFontVariationAxisDefaultValueKey, str)
        self.assertIsInstance(CoreText.kCTFontVariationAxisNameKey, str)

        self.assertIsInstance(CoreText.kCTFontFeatureTypeIdentifierKey, str)
        self.assertIsInstance(CoreText.kCTFontFeatureTypeNameKey, str)
        self.assertIsInstance(CoreText.kCTFontFeatureTypeExclusiveKey, str)
        self.assertIsInstance(CoreText.kCTFontFeatureTypeSelectorsKey, str)
        self.assertIsInstance(CoreText.kCTFontFeatureSelectorIdentifierKey, str)
        self.assertIsInstance(CoreText.kCTFontFeatureSelectorNameKey, str)
        self.assertIsInstance(CoreText.kCTFontFeatureSelectorDefaultKey, str)
        self.assertIsInstance(CoreText.kCTFontFeatureSelectorSettingKey, str)

        self.assertEqual(CoreText.kCTFontTableBASE, fourcc(b"BASE"))
        self.assertEqual(CoreText.kCTFontTableCBDT, fourcc(b"CBDT"))
        self.assertEqual(CoreText.kCTFontTableCBLC, fourcc(b"CBLC"))
        self.assertEqual(CoreText.kCTFontTableCFF, fourcc(b"CFF "))
        self.assertEqual(CoreText.kCTFontTableCFF2, fourcc(b"CFF2"))
        self.assertEqual(CoreText.kCTFontTableCOLR, fourcc(b"COLR"))
        self.assertEqual(CoreText.kCTFontTableCPAL, fourcc(b"CPAL"))
        self.assertEqual(CoreText.kCTFontTableCFF, fourcc(b"CFF "))
        self.assertEqual(CoreText.kCTFontTableDSIG, fourcc(b"DSIG"))
        self.assertEqual(CoreText.kCTFontTableEBDT, fourcc(b"EBDT"))
        self.assertEqual(CoreText.kCTFontTableEBLC, fourcc(b"EBLC"))
        self.assertEqual(CoreText.kCTFontTableEBSC, fourcc(b"EBSC"))
        self.assertEqual(CoreText.kCTFontTableGDEF, fourcc(b"GDEF"))
        self.assertEqual(CoreText.kCTFontTableGPOS, fourcc(b"GPOS"))
        self.assertEqual(CoreText.kCTFontTableGSUB, fourcc(b"GSUB"))
        self.assertEqual(CoreText.kCTFontTableHVAR, fourcc(b"HVAR"))
        self.assertEqual(CoreText.kCTFontTableJSTF, fourcc(b"JSTF"))
        self.assertEqual(CoreText.kCTFontTableLTSH, fourcc(b"LTSH"))
        self.assertEqual(CoreText.kCTFontTableMATH, fourcc(b"MATH"))
        self.assertEqual(CoreText.kCTFontTableMVAR, fourcc(b"MVAR"))
        self.assertEqual(CoreText.kCTFontTableOS2, fourcc(b"OS/2"))
        self.assertEqual(CoreText.kCTFontTablePCLT, fourcc(b"PCLT"))
        self.assertEqual(CoreText.kCTFontTableSTAT, fourcc(b"STAT"))
        self.assertEqual(CoreText.kCTFontTableSVG, fourcc(b"SVG "))
        self.assertEqual(CoreText.kCTFontTableVDMX, fourcc(b"VDMX"))
        self.assertEqual(CoreText.kCTFontTableVORG, fourcc(b"VORG"))
        self.assertEqual(CoreText.kCTFontTableVVAR, fourcc(b"VVAR"))
        self.assertEqual(CoreText.kCTFontTableZapf, fourcc(b"Zapf"))
        self.assertEqual(CoreText.kCTFontTableAcnt, fourcc(b"acnt"))
        self.assertEqual(CoreText.kCTFontTableAnkr, fourcc(b"ankr"))
        self.assertEqual(CoreText.kCTFontTableAvar, fourcc(b"avar"))
        self.assertEqual(CoreText.kCTFontTableBdat, fourcc(b"bdat"))
        self.assertEqual(CoreText.kCTFontTableBhed, fourcc(b"bhed"))
        self.assertEqual(CoreText.kCTFontTableBloc, fourcc(b"bloc"))
        self.assertEqual(CoreText.kCTFontTableBsln, fourcc(b"bsln"))
        self.assertEqual(CoreText.kCTFontTableCidg, fourcc(b"cidg"))
        self.assertEqual(CoreText.kCTFontTableCmap, fourcc(b"cmap"))
        self.assertEqual(CoreText.kCTFontTableCvar, fourcc(b"cvar"))
        self.assertEqual(CoreText.kCTFontTableCvt, fourcc(b"cvt "))
        self.assertEqual(CoreText.kCTFontTableFdsc, fourcc(b"fdsc"))
        self.assertEqual(CoreText.kCTFontTableFeat, fourcc(b"feat"))
        self.assertEqual(CoreText.kCTFontTableFmtx, fourcc(b"fmtx"))
        self.assertEqual(CoreText.kCTFontTableFond, fourcc(b"fond"))
        self.assertEqual(CoreText.kCTFontTableFpgm, fourcc(b"fpgm"))
        self.assertEqual(CoreText.kCTFontTableFvar, fourcc(b"fvar"))
        self.assertEqual(CoreText.kCTFontTableGasp, fourcc(b"gasp"))
        self.assertEqual(CoreText.kCTFontTableGlyf, fourcc(b"glyf"))
        self.assertEqual(CoreText.kCTFontTableGvar, fourcc(b"gvar"))
        self.assertEqual(CoreText.kCTFontTableHdmx, fourcc(b"hdmx"))
        self.assertEqual(CoreText.kCTFontTableHead, fourcc(b"head"))
        self.assertEqual(CoreText.kCTFontTableHhea, fourcc(b"hhea"))
        self.assertEqual(CoreText.kCTFontTableHmtx, fourcc(b"hmtx"))
        self.assertEqual(CoreText.kCTFontTableHsty, fourcc(b"hsty"))
        self.assertEqual(CoreText.kCTFontTableJust, fourcc(b"just"))
        self.assertEqual(CoreText.kCTFontTableKern, fourcc(b"kern"))
        self.assertEqual(CoreText.kCTFontTableKerx, fourcc(b"kerx"))
        self.assertEqual(CoreText.kCTFontTableLcar, fourcc(b"lcar"))
        self.assertEqual(CoreText.kCTFontTableLtag, fourcc(b"ltag"))
        self.assertEqual(CoreText.kCTFontTableLoca, fourcc(b"loca"))
        self.assertEqual(CoreText.kCTFontTableMaxp, fourcc(b"maxp"))
        self.assertEqual(CoreText.kCTFontTableMeta, fourcc(b"meta"))
        self.assertEqual(CoreText.kCTFontTableMort, fourcc(b"mort"))
        self.assertEqual(CoreText.kCTFontTableMorx, fourcc(b"morx"))
        self.assertEqual(CoreText.kCTFontTableName, fourcc(b"name"))
        self.assertEqual(CoreText.kCTFontTableOpbd, fourcc(b"opbd"))
        self.assertEqual(CoreText.kCTFontTablePost, fourcc(b"post"))
        self.assertEqual(CoreText.kCTFontTablePrep, fourcc(b"prep"))
        self.assertEqual(CoreText.kCTFontTableProp, fourcc(b"prop"))
        self.assertEqual(CoreText.kCTFontTableSbit, fourcc(b"sbit"))
        self.assertEqual(CoreText.kCTFontTableTrak, fourcc(b"trak"))
        self.assertEqual(CoreText.kCTFontTableVhea, fourcc(b"vhea"))
        self.assertEqual(CoreText.kCTFontTableVmtx, fourcc(b"vmtx"))
        self.assertEqual(CoreText.kCTFontTableXref, fourcc(b"xref"))

        self.assertEqual(CoreText.kCTFontTableOptionNoOptions, 0)
        self.assertEqual(CoreText.kCTFontTableOptionExcludeSynthetic, (1 << 0))

    def testFunctions(self):
        font = CoreText.CTFontCreateWithName("Optima Bold", 14, None)
        self.assertIsInstance(font, CoreText.CTFontRef)
        self.assertResultIsCFRetained(CoreText.CTFontCreateWithName)

        descriptor = CoreText.CTFontDescriptorCreateWithNameAndSize("Optima Bold", 14.0)
        self.assertIsInstance(descriptor, CoreText.CTFontDescriptorRef)

        font = CoreText.CTFontCreateWithFontDescriptor(descriptor, 5.0, None)
        self.assertIsInstance(font, CoreText.CTFontRef)
        self.assertResultIsCFRetained(CoreText.CTFontCreateWithFontDescriptor)

        font = CoreText.CTFontCreateUIFontForLanguage(
            CoreText.kCTFontMiniSystemFontType, 10.0, "nl_NL"
        )
        self.assertIsInstance(font, CoreText.CTFontRef)
        self.assertResultIsCFRetained(CoreText.CTFontCreateUIFontForLanguage)

        font2 = CoreText.CTFontCreateCopyWithAttributes(font, 9.0, None, None)

        self.assertIsInstance(font2, CoreText.CTFontRef)
        self.assertResultIsCFRetained(CoreText.CTFontCreateCopyWithAttributes)

        font2 = CoreText.CTFontCreateCopyWithSymbolicTraits(
            font, 14.0, None, CoreText.kCTFontBoldTrait, CoreText.kCTFontBoldTrait
        )
        self.assertIsInstance(font2, CoreText.CTFontRef)
        self.assertResultIsCFRetained(CoreText.CTFontCreateCopyWithAttributes)

        font2 = CoreText.CTFontCreateCopyWithFamily(font, 14.0, None, "Lucida Grande")
        self.assertIsInstance(font2, CoreText.CTFontRef)
        self.assertResultIsCFRetained(CoreText.CTFontCreateCopyWithFamily)

        font2 = CoreText.CTFontCreateForString(
            font, "hello world", CoreText.CFRange(1, 4)
        )
        self.assertIsInstance(font2, CoreText.CTFontRef)
        self.assertResultIsCFRetained(CoreText.CTFontCreateForString)

        descriptor = CoreText.CTFontCopyFontDescriptor(font)
        self.assertIsInstance(descriptor, CoreText.CTFontDescriptorRef)

        v = CoreText.CTFontCopyAttribute(font, "size")
        self.assertIsNone(v)
        self.assertResultIsCFRetained(CoreText.CTFontCopyAttribute)

        v = CoreText.CTFontGetSize(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetMatrix(font)
        self.assertIsInstance(v, Quartz.CGAffineTransform)

        v = CoreText.CTFontGetSymbolicTraits(font)
        self.assertIsInstance(v, int)

        v = CoreText.CTFontCopyTraits(font)
        self.assertIsInstance(v, CoreText.CFDictionaryRef)

        v = CoreText.CTFontCopyPostScriptName(font)
        self.assertIsInstance(v, str)

        v = CoreText.CTFontCopyFamilyName(font)
        self.assertIsInstance(v, str)

        v = CoreText.CTFontCopyFullName(font)
        self.assertIsInstance(v, str)

        v = CoreText.CTFontCopyDisplayName(font)
        self.assertIsInstance(v, str)

        v = CoreText.CTFontCopyName(font, CoreText.kCTFontCopyrightNameKey)
        self.assertIsInstance(v, str)

        v, locname = CoreText.CTFontCopyLocalizedName(
            font, CoreText.kCTFontCopyrightNameKey, None
        )
        self.assertIsInstance(v, (str, type(None)))
        self.assertIsInstance(locname, (str, type(None)))
        self.assertArgIsOut(CoreText.CTFontCopyLocalizedName, 2)

        v = CoreText.CTFontCopyCharacterSet(font)
        # self.assertIsInstance(v, CoreText.CFCharacterSetRef)
        self.assertIn("CharacterSet", type(v).__name__)

        v = CoreText.CTFontGetStringEncoding(font)
        self.assertIsInstance(v, int)

        v = CoreText.CTFontCopySupportedLanguages(font)
        self.assertIsInstance(v, CoreText.CFArrayRef)

        self.assertArgIsOut(CoreText.CTFontGetGlyphsForCharacters, 2)
        v, gl = CoreText.CTFontGetGlyphsForCharacters(font, "hello", None, 5)

        self.assertTrue(v is True)
        self.assertIsInstance(gl, tuple)
        self.assertEqual(len(gl), 5)
        self.assertIsInstance(gl[0], int)

        v = CoreText.CTFontGetAscent(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetDescent(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetLeading(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetUnitsPerEm(font)
        self.assertIsInstance(v, int)

        v = CoreText.CTFontGetGlyphCount(font)
        self.assertIsInstance(v, int)

        v = CoreText.CTFontGetBoundingBox(font)
        self.assertIsInstance(v, CoreText.CGRect)

        v = CoreText.CTFontGetUnderlinePosition(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetUnderlineThickness(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetSlantAngle(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetCapHeight(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetXHeight(font)
        self.assertIsInstance(v, float)

        v = CoreText.CTFontGetGlyphWithName(font, "A")
        self.assertIsInstance(v, int)

        v, r = CoreText.CTFontGetBoundingRectsForGlyphs(
            font, CoreText.kCTFontDefaultOrientation, gl, None, 5
        )
        self.assertIsInstance(v, Quartz.CGRect)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 5)
        self.assertIsInstance(r[0], Quartz.CGRect)

        v, r = CoreText.CTFontGetAdvancesForGlyphs(
            font, CoreText.kCTFontDefaultOrientation, gl, None, 5
        )
        self.assertIsInstance(v, float)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 5)
        self.assertIsInstance(r[0], Quartz.CGSize)

        r = CoreText.CTFontGetVerticalTranslationsForGlyphs(font, gl, None, 5)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 5)
        self.assertIsInstance(r[0], Quartz.CGSize)

        v = CoreText.CTFontCreatePathForGlyph(font, gl[0], None)
        self.assertIsInstance(v, CoreText.CGPathRef)

        self.assertResultIsCFRetained(CoreText.CTFontCopyVariationAxes)
        v = CoreText.CTFontCopyVariationAxes(font)
        if v is not None:
            self.assertIsInstance(v, CoreText.CFArrayRef)

        self.assertResultIsCFRetained(CoreText.CTFontCopyVariation)
        v = CoreText.CTFontCopyVariation(font)
        if v is not None:
            self.assertIsInstance(v, CoreText.CFDictionaryRef)

        v = CoreText.CTFontCopyFeatures(font)
        self.assertIsInstance(v, CoreText.CFArrayRef)
        self.assertResultIsCFRetained(CoreText.CTFontCopyFeatures)

        self.assertResultIsCFRetained(CoreText.CTFontCopyFeatureSettings)
        v = CoreText.CTFontCopyFeatureSettings(font)
        if v is not None:
            self.assertIsInstance(v, CoreText.CFArrayRef)

        v, o = CoreText.CTFontCopyGraphicsFont(font, None)
        self.assertIsInstance(v, CoreText.CGFontRef)
        if o is not None:
            self.assertIsInstance(o, CoreText.CTFontDescriptorRef)
        self.assertResultIsCFRetained(CoreText.CTFontCopyGraphicsFont)
        self.assertArgIsCFRetained(CoreText.CTFontCopyGraphicsFont, 1)
        self.assertArgIsOut(CoreText.CTFontCopyGraphicsFont, 1)

        v = CoreText.CTFontCreateWithGraphicsFont(v, 20.5, None, None)
        self.assertIsInstance(v, CoreText.CTFontRef)
        self.assertResultIsCFRetained(CoreText.CTFontCreateWithGraphicsFont)

        if 0:
            # Cannot tests these because the ATS framework is not
            # wrapped.
            v, o = CoreText.CTFontGetPlatformFont(font, None)
            self.assertIsInstance(v, CoreText.ATSFontRef)
            self.assertIsInstance(o, CoreText.CTFontDescriptorRef)

            v = CoreText.CTFontCreateWithPlatformFont(v, 22.5, None, None)
            self.assertIsInstance(v, CoreText.CGFontRef)

        self.assertArgIsCFRetained(CoreText.CTFontGetPlatformFont, 1)
        self.assertResultIsCFRetained(CoreText.CTFontCreateWithPlatformFont)

        v = CoreText.CTFontCopyAvailableTables(
            font, CoreText.kCTFontTableOptionNoOptions
        )
        self.assertIsInstance(v, tuple)

        v = CoreText.CTFontCopyTable(font, v[0], 0)
        self.assertIsInstance(v, CoreText.CFDataRef)

        v = CoreText.CTFontGetTypeID()
        self.assertIsInstance(v, int)

        v, a = CoreText.CTFontGetLigatureCaretPositions(font, gl[0], None, 5)
        self.assertIsInstance(v, int)
        self.assertIsInstance(a, tuple)
        self.assertEqual(len(a), 5)
        self.assertTrue(all(isinstance(x, float) for x in a))

    @min_os_level("10.6")
    def testFunctions10_6(self):
        self.assertResultIsCFRetained(CoreText.CTFontCreateWithNameAndOptions)
        v = CoreText.CTFontCreateWithNameAndOptions("Times", 15, None, 0)
        self.assertIsInstance(v, CoreText.CTFontRef)

    @min_os_level("10.6")
    def testFunctions10_6_crash(self):
        descr = CoreText.CTFontDescriptorCreateWithNameAndSize("Courier", 14.0)
        self.assertNotEqual(descr, None)

        self.assertResultIsCFRetained(CoreText.CTFontCreateWithFontDescriptorAndOptions)

        v = CoreText.CTFontCreateWithFontDescriptorAndOptions(descr, 14.0, None, 0)
        self.assertIsInstance(v, CoreText.CTFontRef)

    @min_os_level("10.7")
    def testFunctions10_7(self):
        self.assertArgHasType(CoreText.CTFontDrawGlyphs, 0, b"^{__CTFont=}")
        self.assertArgHasType(CoreText.CTFontDrawGlyphs, 1, b"n^S")
        self.assertArgSizeInArg(CoreText.CTFontDrawGlyphs, 1, 3)
        self.assertArgHasType(
            CoreText.CTFontDrawGlyphs, 2, b"n^" + CoreText.CGPoint.__typestr__
        )
        self.assertArgSizeInArg(CoreText.CTFontDrawGlyphs, 2, 3)
        self.assertArgHasType(CoreText.CTFontDrawGlyphs, 3, objc._C_NSUInteger)
        self.assertArgHasType(CoreText.CTFontDrawGlyphs, 4, b"^{CGContext=}")

    @min_os_level("10.8")
    def testFunctions10_8(self):

        font = CoreText.CTFontCreateUIFontForLanguage(
            CoreText.kCTFontMiniSystemFontType, 10.0, "nl_NL"
        )
        self.assertTrue(font is not None)
        v, gl = CoreText.CTFontGetGlyphsForCharacters(font, "hello", None, 5)
        self.assertTrue(v)
        self.assertIsInstance(gl, tuple)

        v, r = CoreText.CTFontGetOpticalBoundsForGlyphs(font, gl, None, 5, 0)
        self.assertIsInstance(v, Quartz.CGRect)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 5)
        self.assertIsInstance(r[0], Quartz.CGRect)

        self.assertResultIsCFRetained(CoreText.CTFontCopyDefaultCascadeListForLanguages)

        # XXX: Introduced in the macOS 11 SDK headers
        CoreText.CTFontCopyNameForGlyph

    @min_os_level("10.9")
    def testFunctions10_9(self):
        self.assertResultIsCFRetained(CoreText.CTFontCreateForStringWithLanguage)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(CoreText.kCTFontOpenTypeFeatureTag, str)
        self.assertIsInstance(CoreText.kCTFontOpenTypeFeatureValue, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(CoreText.kCTFontVariationAxisHiddenKey, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(CoreText.kCTFontFeatureSampleTextKey, str)
        self.assertIsInstance(CoreText.kCTFontFeatureTooltipTextKey, str)
