
from PyObjCTools.TestSupport import *
from CoreText import *
from Quartz import *

class TestCTFont (TestCase):
    def testTypes(self):
        self.assertIsInstance(CTFontRef, objc.objc_class)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCTFontOptionsDefault, 0)
        self.assertEqual(kCTFontOptionsPreventAutoActivation, 1 << 0)
        self.assertEqual(kCTFontOptionsPreferSystemFont, 1 << 2)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(kCTBaselineClassHanging, unicode)
        self.assertIsInstance(kCTBaselineClassIdeographicCentered, unicode)
        self.assertIsInstance(kCTBaselineClassIdeographicHigh, unicode)
        self.assertIsInstance(kCTBaselineClassIdeographicLow, unicode)
        self.assertIsInstance(kCTBaselineClassMath, unicode)
        self.assertIsInstance(kCTBaselineClassRoman, unicode)
        self.assertIsInstance(kCTBaselineOriginalFont, unicode)
        self.assertIsInstance(kCTBaselineReferenceFont, unicode)

        self.assertEqual(kCTFontTableAnkr, fourcc(b'ankr'))

        self.assertEqual(kCTFontUIFontNone, 0xffffffff)
        self.assertEqual(kCTFontUIFontUser, 0)
        self.assertEqual(kCTFontUIFontUserFixedPitch, 1)
        self.assertEqual(kCTFontUIFontSystem, 2)
        self.assertEqual(kCTFontUIFontEmphasizedSystem, 3)
        self.assertEqual(kCTFontUIFontSmallSystem, 4)
        self.assertEqual(kCTFontUIFontSmallEmphasizedSystem, 5)
        self.assertEqual(kCTFontUIFontMiniSystem, 6)
        self.assertEqual(kCTFontUIFontMiniEmphasizedSystem, 7)
        self.assertEqual(kCTFontUIFontViews, 8)
        self.assertEqual(kCTFontUIFontApplication, 9)
        self.assertEqual(kCTFontUIFontLabel, 10)
        self.assertEqual(kCTFontUIFontMenuTitle, 11)
        self.assertEqual(kCTFontUIFontMenuItem, 12)
        self.assertEqual(kCTFontUIFontMenuItemMark, 13)
        self.assertEqual(kCTFontUIFontMenuItemCmdKey, 14)
        self.assertEqual(kCTFontUIFontWindowTitle, 15)
        self.assertEqual(kCTFontUIFontPushButton, 16)
        self.assertEqual(kCTFontUIFontUtilityWindowTitle, 17)
        self.assertEqual(kCTFontUIFontAlertHeader, 18)
        self.assertEqual(kCTFontUIFontSystemDetail, 19)
        self.assertEqual(kCTFontUIFontEmphasizedSystemDetail, 20)
        self.assertEqual(kCTFontUIFontToolbar, 21)
        self.assertEqual(kCTFontUIFontSmallToolbar, 22)
        self.assertEqual(kCTFontUIFontMessage, 23)
        self.assertEqual(kCTFontUIFontPalette, 24)
        self.assertEqual(kCTFontUIFontToolTip, 25)
        self.assertEqual(kCTFontUIFontControlContent, 26)

    def testConstants(self):
        self.assertIsInstance(kCTFontCopyrightNameKey, unicode)
        self.assertIsInstance(kCTFontFamilyNameKey, unicode)
        self.assertIsInstance(kCTFontSubFamilyNameKey, unicode)
        self.assertIsInstance(kCTFontStyleNameKey, unicode)
        self.assertIsInstance(kCTFontUniqueNameKey, unicode)
        self.assertIsInstance(kCTFontFullNameKey, unicode)
        self.assertIsInstance(kCTFontVersionNameKey, unicode)
        self.assertIsInstance(kCTFontPostScriptNameKey, unicode)
        self.assertIsInstance(kCTFontTrademarkNameKey, unicode)
        self.assertIsInstance(kCTFontManufacturerNameKey, unicode)
        self.assertIsInstance(kCTFontDesignerNameKey, unicode)
        self.assertIsInstance(kCTFontDescriptionNameKey, unicode)
        self.assertIsInstance(kCTFontVendorURLNameKey, unicode)
        self.assertIsInstance(kCTFontDesignerURLNameKey, unicode)
        self.assertIsInstance(kCTFontLicenseNameKey, unicode)
        self.assertIsInstance(kCTFontLicenseURLNameKey, unicode)
        self.assertIsInstance(kCTFontSampleTextNameKey, unicode)
        self.assertIsInstance(kCTFontPostScriptCIDNameKey, unicode)

        self.assertEqual(kCTFontNoFontType, 4294967295) # (uint32_t)-1
        self.assertEqual(kCTFontUserFontType, 0)
        self.assertEqual(kCTFontUserFixedPitchFontType, 1)
        self.assertEqual(kCTFontSystemFontType, 2)
        self.assertEqual(kCTFontEmphasizedSystemFontType, 3)
        self.assertEqual(kCTFontSmallSystemFontType, 4)
        self.assertEqual(kCTFontSmallEmphasizedSystemFontType, 5)
        self.assertEqual(kCTFontMiniSystemFontType, 6)
        self.assertEqual(kCTFontMiniEmphasizedSystemFontType, 7)
        self.assertEqual(kCTFontViewsFontType, 8)
        self.assertEqual(kCTFontApplicationFontType, 9)
        self.assertEqual(kCTFontLabelFontType, 10)
        self.assertEqual(kCTFontMenuTitleFontType, 11)
        self.assertEqual(kCTFontMenuItemFontType, 12)
        self.assertEqual(kCTFontMenuItemMarkFontType, 13)
        self.assertEqual(kCTFontMenuItemCmdKeyFontType, 14)
        self.assertEqual(kCTFontWindowTitleFontType, 15)
        self.assertEqual(kCTFontPushButtonFontType, 16)
        self.assertEqual(kCTFontUtilityWindowTitleFontType, 17)
        self.assertEqual(kCTFontAlertHeaderFontType, 18)
        self.assertEqual(kCTFontSystemDetailFontType, 19)
        self.assertEqual(kCTFontEmphasizedSystemDetailFontType, 20)
        self.assertEqual(kCTFontToolbarFontType, 21)
        self.assertEqual(kCTFontSmallToolbarFontType, 22)
        self.assertEqual(kCTFontMessageFontType, 23)
        self.assertEqual(kCTFontPaletteFontType, 24)
        self.assertEqual(kCTFontToolTipFontType, 25)
        self.assertEqual(kCTFontControlContentFontType, 26)

        self.assertIsInstance(kCTFontVariationAxisIdentifierKey, unicode)
        self.assertIsInstance(kCTFontVariationAxisMinimumValueKey, unicode)
        self.assertIsInstance(kCTFontVariationAxisMaximumValueKey, unicode)
        self.assertIsInstance(kCTFontVariationAxisDefaultValueKey, unicode)
        self.assertIsInstance(kCTFontVariationAxisNameKey, unicode)

        self.assertIsInstance(kCTFontFeatureTypeIdentifierKey, unicode)
        self.assertIsInstance(kCTFontFeatureTypeNameKey, unicode)
        self.assertIsInstance(kCTFontFeatureTypeExclusiveKey, unicode)
        self.assertIsInstance(kCTFontFeatureTypeSelectorsKey, unicode)
        self.assertIsInstance(kCTFontFeatureSelectorIdentifierKey, unicode)
        self.assertIsInstance(kCTFontFeatureSelectorNameKey, unicode)
        self.assertIsInstance(kCTFontFeatureSelectorDefaultKey, unicode)
        self.assertIsInstance(kCTFontFeatureSelectorSettingKey, unicode)


        self.assertEqual(kCTFontTableBASE, fourcc(b'BASE'))
        self.assertEqual(kCTFontTableCBDT, fourcc(b'CBDT'))
        self.assertEqual(kCTFontTableCBLC, fourcc(b'CBLC'))
        self.assertEqual(kCTFontTableCFF, fourcc(b'CFF '))
        self.assertEqual(kCTFontTableCFF2, fourcc(b'CFF2'))
        self.assertEqual(kCTFontTableCOLR, fourcc(b'COLR'))
        self.assertEqual(kCTFontTableCPAL, fourcc(b'CPAL'))
        self.assertEqual(kCTFontTableCFF, fourcc(b'CFF '))
        self.assertEqual(kCTFontTableDSIG, fourcc(b'DSIG'))
        self.assertEqual(kCTFontTableEBDT, fourcc(b'EBDT'))
        self.assertEqual(kCTFontTableEBLC, fourcc(b'EBLC'))
        self.assertEqual(kCTFontTableEBSC, fourcc(b'EBSC'))
        self.assertEqual(kCTFontTableGDEF, fourcc(b'GDEF'))
        self.assertEqual(kCTFontTableGPOS, fourcc(b'GPOS'))
        self.assertEqual(kCTFontTableGSUB, fourcc(b'GSUB'))
        self.assertEqual(kCTFontTableHVAR, fourcc(b'HVAR'))
        self.assertEqual(kCTFontTableJSTF, fourcc(b'JSTF'))
        self.assertEqual(kCTFontTableLTSH, fourcc(b'LTSH'))
        self.assertEqual(kCTFontTableMATH, fourcc(b'MATH'))
        self.assertEqual(kCTFontTableMVAR, fourcc(b'MVAR'))
        self.assertEqual(kCTFontTableOS2, fourcc(b'OS/2'))
        self.assertEqual(kCTFontTablePCLT, fourcc(b'PCLT'))
        self.assertEqual(kCTFontTableSTAT, fourcc(b'STAT'))
        self.assertEqual(kCTFontTableSVG, fourcc(b'SVG '))
        self.assertEqual(kCTFontTableVDMX, fourcc(b'VDMX'))
        self.assertEqual(kCTFontTableVORG, fourcc(b'VORG'))
        self.assertEqual(kCTFontTableVVAR, fourcc(b'VVAR'))
        self.assertEqual(kCTFontTableZapf, fourcc(b'Zapf'))
        self.assertEqual(kCTFontTableAcnt, fourcc(b'acnt'))
        self.assertEqual(kCTFontTableAnkr, fourcc(b'ankr'))
        self.assertEqual(kCTFontTableAvar, fourcc(b'avar'))
        self.assertEqual(kCTFontTableBdat, fourcc(b'bdat'))
        self.assertEqual(kCTFontTableBhed, fourcc(b'bhed'))
        self.assertEqual(kCTFontTableBloc, fourcc(b'bloc'))
        self.assertEqual(kCTFontTableBsln, fourcc(b'bsln'))
        self.assertEqual(kCTFontTableCidg, fourcc(b'cidg'))
        self.assertEqual(kCTFontTableCmap, fourcc(b'cmap'))
        self.assertEqual(kCTFontTableCvar, fourcc(b'cvar'))
        self.assertEqual(kCTFontTableCvt, fourcc(b'cvt '))
        self.assertEqual(kCTFontTableFdsc, fourcc(b'fdsc'))
        self.assertEqual(kCTFontTableFeat, fourcc(b'feat'))
        self.assertEqual(kCTFontTableFmtx, fourcc(b'fmtx'))
        self.assertEqual(kCTFontTableFond, fourcc(b'fond'))
        self.assertEqual(kCTFontTableFpgm, fourcc(b'fpgm'))
        self.assertEqual(kCTFontTableFvar, fourcc(b'fvar'))
        self.assertEqual(kCTFontTableGasp, fourcc(b'gasp'))
        self.assertEqual(kCTFontTableGlyf, fourcc(b'glyf'))
        self.assertEqual(kCTFontTableGvar, fourcc(b'gvar'))
        self.assertEqual(kCTFontTableHdmx, fourcc(b'hdmx'))
        self.assertEqual(kCTFontTableHead, fourcc(b'head'))
        self.assertEqual(kCTFontTableHhea, fourcc(b'hhea'))
        self.assertEqual(kCTFontTableHmtx, fourcc(b'hmtx'))
        self.assertEqual(kCTFontTableHsty, fourcc(b'hsty'))
        self.assertEqual(kCTFontTableJust, fourcc(b'just'))
        self.assertEqual(kCTFontTableKern, fourcc(b'kern'))
        self.assertEqual(kCTFontTableKerx, fourcc(b'kerx'))
        self.assertEqual(kCTFontTableLcar, fourcc(b'lcar'))
        self.assertEqual(kCTFontTableLtag, fourcc(b'ltag'))
        self.assertEqual(kCTFontTableLoca, fourcc(b'loca'))
        self.assertEqual(kCTFontTableMaxp, fourcc(b'maxp'))
        self.assertEqual(kCTFontTableMeta, fourcc(b'meta'))
        self.assertEqual(kCTFontTableMort, fourcc(b'mort'))
        self.assertEqual(kCTFontTableMorx, fourcc(b'morx'))
        self.assertEqual(kCTFontTableName, fourcc(b'name'))
        self.assertEqual(kCTFontTableOpbd, fourcc(b'opbd'))
        self.assertEqual(kCTFontTablePost, fourcc(b'post'))
        self.assertEqual(kCTFontTablePrep, fourcc(b'prep'))
        self.assertEqual(kCTFontTableProp, fourcc(b'prop'))
        self.assertEqual(kCTFontTableSbit, fourcc(b'sbit'))
        self.assertEqual(kCTFontTableTrak, fourcc(b'trak'))
        self.assertEqual(kCTFontTableVhea, fourcc(b'vhea'))
        self.assertEqual(kCTFontTableVmtx, fourcc(b'vmtx'))
        self.assertEqual(kCTFontTableXref, fourcc(b'xref'))

        self.assertEqual(kCTFontTableOptionNoOptions, 0)
        self.assertEqual(kCTFontTableOptionExcludeSynthetic, (1 << 0))

    def testFunctions(self):
        font = CTFontCreateWithName(b"Optima Bold".decode('latin1'),
                14,
                None)
        self.assertIsInstance(font, CTFontRef)
        self.assertResultIsCFRetained(CTFontCreateWithName)

        descriptor = CTFontDescriptorCreateWithNameAndSize(
                "Optima Bold", 14.0)
        self.assertIsInstance(descriptor, CTFontDescriptorRef)

        font = CTFontCreateWithFontDescriptor(
                descriptor, 5.0, None)
        self.assertIsInstance(font, CTFontRef)
        self.assertResultIsCFRetained(CTFontCreateWithFontDescriptor)

        font = CTFontCreateUIFontForLanguage(
                kCTFontMiniSystemFontType,
                10.0, "nl_NL")
        self.assertIsInstance(font, CTFontRef)
        self.assertResultIsCFRetained(CTFontCreateUIFontForLanguage)

        font2 = CTFontCreateCopyWithAttributes(
                font,
                9.0,
                None,
                None)

        self.assertIsInstance(font2, CTFontRef)
        self.assertResultIsCFRetained(CTFontCreateCopyWithAttributes)

        font2 = CTFontCreateCopyWithSymbolicTraits(
                font, 14.0, None,
                kCTFontBoldTrait, kCTFontBoldTrait)
        self.assertIsInstance(font2, CTFontRef)
        self.assertResultIsCFRetained(CTFontCreateCopyWithAttributes)


        font2 = CTFontCreateCopyWithFamily(
                font, 14.0, None, "Lucida Grande")
        self.assertIsInstance(font2, CTFontRef)
        self.assertResultIsCFRetained(CTFontCreateCopyWithFamily)

        font2 = CTFontCreateForString(
                font, b"hello world".decode('latin1'), CFRange(1, 4))
        self.assertIsInstance(font2, CTFontRef)
        self.assertResultIsCFRetained(CTFontCreateForString)

        descriptor = CTFontCopyFontDescriptor(font)
        self.assertIsInstance(descriptor, CTFontDescriptorRef)

        v = CTFontCopyAttribute(font, "size")
        self.assertIsNone(v)
        self.assertResultIsCFRetained(CTFontCopyAttribute)

        v = CTFontGetSize(font)
        self.assertIsInstance(v, float)

        v = CTFontGetMatrix(font)
        self.assertIsInstance(v, CGAffineTransform)

        v = CTFontGetSymbolicTraits(font)
        self.assertIsInstance(v, (int, long))

        v = CTFontCopyTraits(font)
        self.assertIsInstance(v, CFDictionaryRef)

        v = CTFontCopyPostScriptName(font)
        self.assertIsInstance(v, unicode)

        v = CTFontCopyFamilyName(font)
        self.assertIsInstance(v, unicode)

        v = CTFontCopyFullName(font)
        self.assertIsInstance(v, unicode)

        v = CTFontCopyDisplayName(font)
        self.assertIsInstance(v, unicode)

        v = CTFontCopyName(font, kCTFontCopyrightNameKey)
        self.assertIsInstance(v, unicode)

        v, l = CTFontCopyLocalizedName(font, kCTFontCopyrightNameKey, None)
        self.assertIsInstance(v, unicode)
        self.assertIsInstance(l, (unicode, type(None)))
        self.assertArgIsOut(CTFontCopyLocalizedName, 2)

        v = CTFontCopyCharacterSet(font)
        #self.assertIsInstance(v, CFCharacterSetRef)
        self.assertIn('CharacterSet', type(v).__name__)

        v = CTFontGetStringEncoding(font)
        self.assertIsInstance(v, (int, long))

        v = CTFontCopySupportedLanguages(font)
        self.assertIsInstance(v, CFArrayRef)

        self.assertArgIsOut(CTFontGetGlyphsForCharacters, 2)
        v, gl = CTFontGetGlyphsForCharacters(font,
                b"hello".decode('latin1'), None, 5)

        self.assertTrue(v is True)
        self.assertIsInstance(gl, tuple)
        self.assertEqual(len(gl), 5)
        self.assertIsInstance(gl[0], (int, long))

        v = CTFontGetAscent(font)
        self.assertIsInstance(v, float)

        v = CTFontGetDescent(font)
        self.assertIsInstance(v, float)

        v = CTFontGetLeading(font)
        self.assertIsInstance(v, float)

        v = CTFontGetUnitsPerEm(font)
        self.assertIsInstance(v, (int, long))

        v = CTFontGetGlyphCount(font)
        self.assertIsInstance(v, (int, long))

        v = CTFontGetBoundingBox(font)
        self.assertIsInstance(v, CGRect)

        v = CTFontGetUnderlinePosition(font)
        self.assertIsInstance(v, float)

        v = CTFontGetUnderlineThickness(font)
        self.assertIsInstance(v, float)

        v = CTFontGetSlantAngle(font)
        self.assertIsInstance(v, float)

        v = CTFontGetCapHeight(font)
        self.assertIsInstance(v, float)

        v = CTFontGetXHeight(font)
        self.assertIsInstance(v, float)

        v = CTFontGetGlyphWithName(font, "A")
        self.assertIsInstance(v, (int, long))


        v, r = CTFontGetBoundingRectsForGlyphs(font,
                kCTFontDefaultOrientation, gl, None, 5)
        self.assertIsInstance(v, CGRect)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 5)
        self.assertIsInstance(r[0], CGRect)


        v, r = CTFontGetAdvancesForGlyphs(font,
                kCTFontDefaultOrientation, gl, None, 5)
        self.assertIsInstance(v, float)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 5)
        self.assertIsInstance(r[0], CGSize)

        r = CTFontGetVerticalTranslationsForGlyphs(font, gl, None, 5)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 5)
        self.assertIsInstance(r[0], CGSize)

        v = CTFontCreatePathForGlyph(font, gl[0], None)
        self.assertIsInstance(v, CGPathRef)

        self.assertResultIsCFRetained(CTFontCopyVariationAxes)
        v = CTFontCopyVariationAxes(font)
        if v is not None:
            self.assertIsInstance(v, CFArrayRef)

        self.assertResultIsCFRetained(CTFontCopyVariation)
        v = CTFontCopyVariation(font)
        if v is not None:
            self.assertIsInstance(v, CFDictionaryRef)

        v = CTFontCopyFeatures(font)
        self.assertIsInstance(v, CFArrayRef)
        self.assertResultIsCFRetained(CTFontCopyFeatures)

        self.assertResultIsCFRetained(CTFontCopyFeatureSettings)
        v = CTFontCopyFeatureSettings(font)
        if v is not None:
            self.assertIsInstance(v, CFArrayRef)

        v, o = CTFontCopyGraphicsFont(font, None)
        self.assertIsInstance(v, CGFontRef)
        if o is not None:
            self.assertIsInstance(o, CTFontDescriptorRef)
        self.assertResultIsCFRetained(CTFontCopyGraphicsFont)
        self.assertArgIsCFRetained(CTFontCopyGraphicsFont, 1)
        self.assertArgIsOut(CTFontCopyGraphicsFont, 1)

        v = CTFontCreateWithGraphicsFont(v, 20.5, None, None)
        self.assertIsInstance(v, CTFontRef)
        self.assertResultIsCFRetained(CTFontCreateWithGraphicsFont)

        if 0:
            # Cannot tests these because the ATS framework is not
            # wrapped.
            v, o = CTFontGetPlatformFont(font, None)
            self.assertIsInstance(v, ATSFontRef)
            self.assertIsInstance(o, CTFontDescriptorRef)

            v = CTFontCreateWithPlatformFont(v, 22.5, None, None)
            self.assertIsInstance(v, CGFontRef)

        self.assertArgIsCFRetained(CTFontGetPlatformFont, 1)
        self.assertResultIsCFRetained(CTFontCreateWithPlatformFont)

        v = CTFontCopyAvailableTables(font, kCTFontTableOptionNoOptions)
        self.assertIsInstance(v, tuple)

        v = CTFontCopyTable(font, v[0], 0)
        self.assertIsInstance(v, CFDataRef)

        v = CTFontGetTypeID()
        self.assertIsInstance(v, (int, long))

        v, a = CTFontGetLigatureCaretPositions(font, gl[0], None, 5)
        self.assertIsInstance(v, int)
        self.assertIsInstance(a, tuple)
        self.assertEqual(len(a), 5)
        self.assertTrue(all(isinstance(x, float) for x in a))

    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.assertResultIsCFRetained(CTFontCreateWithNameAndOptions)
        v = CTFontCreateWithNameAndOptions(b"Times".decode('latin1'), 15, None, 0)
        self.assertIsInstance(v, CTFontRef)


    @expectedFailureIf(os_release().rsplit('.', 1)[0] == '10.6')
    @min_os_level('10.6')
    def testFunctions10_6_crash(self):
        descr = CTFontDescriptorCreateWithNameAndSize(
                b"Courier".decode('latin1'), 14.0)
        self.assertNotEqual(descr, None)

        self.assertResultIsCFRetained(CTFontCreateWithFontDescriptorAndOptions)

        # FIXME: this crashes the interpreter, without a clear reason
        if os_release().rsplit('.', 1)[0] == '10.6':
            self.fail("hard crash in test for CTFontCreateWithFontDescriptorAndOptions")
        v = CTFontCreateWithFontDescriptorAndOptions(descr, 14.0, None, 0)
        self.assertIsInstance(v, CTFontRef)

    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.assertArgHasType(CTFontDrawGlyphs, 0, b"^{__CTFont=}")
        self.assertArgHasType(CTFontDrawGlyphs, 1, b"n^S")
        self.assertArgSizeInArg(CTFontDrawGlyphs, 1, 3)
        self.assertArgHasType(CTFontDrawGlyphs, 2, b"n^" + CGPoint.__typestr__)
        self.assertArgSizeInArg(CTFontDrawGlyphs, 2, 3)
        self.assertArgHasType(CTFontDrawGlyphs, 3, objc._C_NSUInteger)
        self.assertArgHasType(CTFontDrawGlyphs, 4, b"^{CGContext=}")


    @min_os_level('10.8')
    def testFunctions10_8(self):

        font = CTFontCreateUIFontForLanguage(
                kCTFontMiniSystemFontType,
                10.0, "nl_NL")
        self.assertTrue(font is not None)
        v, gl = CTFontGetGlyphsForCharacters(font,
                b"hello".decode('latin1'), None, 5)
        self.assertTrue(v)
        self.assertIsInstance(gl, tuple)

        v, r = CTFontGetOpticalBoundsForGlyphs(font, gl, None, 5, 0)
        self.assertIsInstance(v, CGRect)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 5)
        self.assertIsInstance(r[0], CGRect)

        self.assertResultIsCFRetained(CTFontCopyDefaultCascadeListForLanguages)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(kCTFontOpenTypeFeatureTag, unicode)
        self.assertIsInstance(kCTFontOpenTypeFeatureValue, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(kCTFontVariationAxisHiddenKey, unicode)

if __name__ == "__main__":
    main()
