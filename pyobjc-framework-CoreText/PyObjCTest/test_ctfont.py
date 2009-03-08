
from PyObjCTools.TestSupport import *
from CoreText import *
from Quartz.CoreGraphics import *

class TestCTFont (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(CTFontRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessIsInstance(kCTFontCopyrightNameKey, unicode)
        self.failUnlessIsInstance(kCTFontFamilyNameKey, unicode)
        self.failUnlessIsInstance(kCTFontSubFamilyNameKey, unicode)
        self.failUnlessIsInstance(kCTFontStyleNameKey, unicode)
        self.failUnlessIsInstance(kCTFontUniqueNameKey, unicode)
        self.failUnlessIsInstance(kCTFontFullNameKey, unicode)
        self.failUnlessIsInstance(kCTFontVersionNameKey, unicode)
        self.failUnlessIsInstance(kCTFontPostScriptNameKey, unicode)
        self.failUnlessIsInstance(kCTFontTrademarkNameKey, unicode)
        self.failUnlessIsInstance(kCTFontManufacturerNameKey, unicode)
        self.failUnlessIsInstance(kCTFontDesignerNameKey, unicode)
        self.failUnlessIsInstance(kCTFontDescriptionNameKey, unicode)
        self.failUnlessIsInstance(kCTFontVendorURLNameKey, unicode)
        self.failUnlessIsInstance(kCTFontDesignerURLNameKey, unicode)
        self.failUnlessIsInstance(kCTFontLicenseNameKey, unicode)
        self.failUnlessIsInstance(kCTFontLicenseURLNameKey, unicode)
        self.failUnlessIsInstance(kCTFontSampleTextNameKey, unicode)
        self.failUnlessIsInstance(kCTFontPostScriptCIDNameKey, unicode)

	self.failUnlessEqual(kCTFontNoFontType,  -1)
	self.failUnlessEqual(kCTFontUserFontType,  0)
	self.failUnlessEqual(kCTFontUserFixedPitchFontType,  1)
	self.failUnlessEqual(kCTFontSystemFontType,  2)
	self.failUnlessEqual(kCTFontEmphasizedSystemFontType,  3)
	self.failUnlessEqual(kCTFontSmallSystemFontType,  4)
	self.failUnlessEqual(kCTFontSmallEmphasizedSystemFontType,  5)
	self.failUnlessEqual(kCTFontMiniSystemFontType,  6)
	self.failUnlessEqual(kCTFontMiniEmphasizedSystemFontType,  7)
	self.failUnlessEqual(kCTFontViewsFontType,  8)
	self.failUnlessEqual(kCTFontApplicationFontType,  9)
	self.failUnlessEqual(kCTFontLabelFontType, 10)
	self.failUnlessEqual(kCTFontMenuTitleFontType, 11)
	self.failUnlessEqual(kCTFontMenuItemFontType, 12)
	self.failUnlessEqual(kCTFontMenuItemMarkFontType, 13)
	self.failUnlessEqual(kCTFontMenuItemCmdKeyFontType, 14)
	self.failUnlessEqual(kCTFontWindowTitleFontType, 15)
	self.failUnlessEqual(kCTFontPushButtonFontType, 16)
	self.failUnlessEqual(kCTFontUtilityWindowTitleFontType, 17)
	self.failUnlessEqual(kCTFontAlertHeaderFontType, 18)
	self.failUnlessEqual(kCTFontSystemDetailFontType, 19)
	self.failUnlessEqual(kCTFontEmphasizedSystemDetailFontType, 20)
	self.failUnlessEqual(kCTFontToolbarFontType, 21)
	self.failUnlessEqual(kCTFontSmallToolbarFontType, 22)
	self.failUnlessEqual(kCTFontMessageFontType, 23)
	self.failUnlessEqual(kCTFontPaletteFontType, 24)
	self.failUnlessEqual(kCTFontToolTipFontType, 25)
	self.failUnlessEqual(kCTFontControlContentFontType, 26)

        self.failUnlessIsInstance(kCTFontVariationAxisIdentifierKey, unicode)
        self.failUnlessIsInstance(kCTFontVariationAxisMinimumValueKey, unicode)
        self.failUnlessIsInstance(kCTFontVariationAxisMaximumValueKey, unicode)
        self.failUnlessIsInstance(kCTFontVariationAxisDefaultValueKey, unicode)
        self.failUnlessIsInstance(kCTFontVariationAxisNameKey, unicode)

        self.failUnlessIsInstance(kCTFontFeatureTypeIdentifierKey, unicode)
        self.failUnlessIsInstance(kCTFontFeatureTypeNameKey, unicode)
        self.failUnlessIsInstance(kCTFontFeatureTypeExclusiveKey, unicode)
        self.failUnlessIsInstance(kCTFontFeatureTypeSelectorsKey, unicode)
        self.failUnlessIsInstance(kCTFontFeatureSelectorIdentifierKey, unicode)
        self.failUnlessIsInstance(kCTFontFeatureSelectorNameKey, unicode)
        self.failUnlessIsInstance(kCTFontFeatureSelectorDefaultKey, unicode)
        self.failUnlessIsInstance(kCTFontFeatureSelectorSettingKey, unicode)


	self.failUnlessEqual(kCTFontTableBASE, fourcc('BASE'))
	self.failUnlessEqual(kCTFontTableCFF, fourcc('CFF '))
	self.failUnlessEqual(kCTFontTableDSIG, fourcc('DSIG'))
	self.failUnlessEqual(kCTFontTableEBDT, fourcc('EBDT'))
	self.failUnlessEqual(kCTFontTableEBLC, fourcc('EBLC'))
	self.failUnlessEqual(kCTFontTableEBSC, fourcc('EBSC'))
	self.failUnlessEqual(kCTFontTableGDEF, fourcc('GDEF'))
	self.failUnlessEqual(kCTFontTableGPOS, fourcc('GPOS'))
	self.failUnlessEqual(kCTFontTableGSUB, fourcc('GSUB'))
	self.failUnlessEqual(kCTFontTableJSTF, fourcc('JSTF'))
	self.failUnlessEqual(kCTFontTableLTSH, fourcc('LTSH'))
	self.failUnlessEqual(kCTFontTableOS2, fourcc('OS/2'))
	self.failUnlessEqual(kCTFontTablePCLT, fourcc('PCLT'))
	self.failUnlessEqual(kCTFontTableVDMX, fourcc('VDMX'))
	self.failUnlessEqual(kCTFontTableVORG, fourcc('VORG'))
	self.failUnlessEqual(kCTFontTableZapf, fourcc('Zapf'))
	self.failUnlessEqual(kCTFontTableAcnt, fourcc('acnt'))
	self.failUnlessEqual(kCTFontTableAvar, fourcc('avar'))
	self.failUnlessEqual(kCTFontTableBdat, fourcc('bdat'))
	self.failUnlessEqual(kCTFontTableBhed, fourcc('bhed'))
	self.failUnlessEqual(kCTFontTableBloc, fourcc('bloc'))
	self.failUnlessEqual(kCTFontTableBsln, fourcc('bsln'))
	self.failUnlessEqual(kCTFontTableCmap, fourcc('cmap'))
	self.failUnlessEqual(kCTFontTableCvar, fourcc('cvar'))
	self.failUnlessEqual(kCTFontTableCvt, fourcc('cvt '))
	self.failUnlessEqual(kCTFontTableFdsc, fourcc('fdsc'))
	self.failUnlessEqual(kCTFontTableFeat, fourcc('feat'))
	self.failUnlessEqual(kCTFontTableFmtx, fourcc('fmtx'))
	self.failUnlessEqual(kCTFontTableFpgm, fourcc('fpgm'))
	self.failUnlessEqual(kCTFontTableFvar, fourcc('fvar'))
	self.failUnlessEqual(kCTFontTableGasp, fourcc('gasp'))
	self.failUnlessEqual(kCTFontTableGlyf, fourcc('glyf'))
	self.failUnlessEqual(kCTFontTableGvar, fourcc('gvar'))
	self.failUnlessEqual(kCTFontTableHdmx, fourcc('hdmx'))
	self.failUnlessEqual(kCTFontTableHead, fourcc('head'))
	self.failUnlessEqual(kCTFontTableHhea, fourcc('hhea'))
	self.failUnlessEqual(kCTFontTableHmtx, fourcc('hmtx'))
	self.failUnlessEqual(kCTFontTableHsty, fourcc('hsty'))
	self.failUnlessEqual(kCTFontTableJust, fourcc('just'))
	self.failUnlessEqual(kCTFontTableKern, fourcc('kern'))
	self.failUnlessEqual(kCTFontTableLcar, fourcc('lcar'))
	self.failUnlessEqual(kCTFontTableLoca, fourcc('loca'))
	self.failUnlessEqual(kCTFontTableMaxp, fourcc('maxp'))
	self.failUnlessEqual(kCTFontTableMort, fourcc('mort'))
	self.failUnlessEqual(kCTFontTableMorx, fourcc('morx'))
	self.failUnlessEqual(kCTFontTableName, fourcc('name'))
	self.failUnlessEqual(kCTFontTableOpbd, fourcc('opbd'))
	self.failUnlessEqual(kCTFontTablePost, fourcc('post'))
	self.failUnlessEqual(kCTFontTablePrep, fourcc('prep'))
	self.failUnlessEqual(kCTFontTableProp, fourcc('prop'))
	self.failUnlessEqual(kCTFontTableTrak, fourcc('trak'))
	self.failUnlessEqual(kCTFontTableVhea, fourcc('vhea'))
	self.failUnlessEqual(kCTFontTableVmtx, fourcc('vmtx'))

	self.failUnlessEqual(kCTFontTableOptionNoOptions, 0)
	self.failUnlessEqual(kCTFontTableOptionExcludeSynthetic, (1 << 0))

    def testFunctions(self):
        font = CTFontCreateWithName(u"Optima Bold",
                14,
                None)
        self.failUnless(isinstance(font, CTFontRef))
        self.failUnlessResultIsCFRetained(CTFontCreateWithName)

        descriptor = CTFontDescriptorCreateWithNameAndSize(
                "Optima Bold", 14.0)
        self.failUnless(isinstance(descriptor, CTFontDescriptorRef))

        font = CTFontCreateWithFontDescriptor(
                descriptor, 5.0, None)
        self.failUnless(isinstance(font, CTFontRef))
        self.failUnlessResultIsCFRetained(CTFontCreateWithFontDescriptor)

        font = CTFontCreateUIFontForLanguage(
                kCTFontMiniSystemFontType,
                10.0, "nl_NL")
        self.failUnless(isinstance(font, CTFontRef))
        self.failUnlessResultIsCFRetained(CTFontCreateUIFontForLanguage)

        font2 = CTFontCreateCopyWithAttributes(
                font,
                9.0,
                None,
                None)

        self.failUnless(isinstance(font2, CTFontRef))
        self.failUnlessResultIsCFRetained(CTFontCreateCopyWithAttributes)

        font2 = CTFontCreateCopyWithSymbolicTraits(
                font, 14.0, None,
                kCTFontBoldTrait, kCTFontBoldTrait)
        self.failUnless(isinstance(font2, CTFontRef))
        self.failUnlessResultIsCFRetained(CTFontCreateCopyWithAttributes)


        font2 = CTFontCreateCopyWithFamily(
                font, 14.0, None, "Lucida Grande")
        self.failUnless(isinstance(font2, CTFontRef))
        self.failUnlessResultIsCFRetained(CTFontCreateCopyWithFamily)

        font2 = CTFontCreateForString(
                font, u"hello world", CFRange(0, 4))
        self.failUnless(isinstance(font2, CTFontRef))
        self.failUnlessResultIsCFRetained(CTFontCreateForString)

        descriptor = CTFontCopyFontDescriptor(font)
        self.failUnless(isinstance(descriptor, CTFontDescriptorRef))

        v = CTFontCopyAttribute(font, "size")
        self.failUnlessIsNone(v)
        self.failUnlessResultIsCFRetained(CTFontCopyAttribute)

        v = CTFontGetSize(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetMatrix(font)
        self.failUnlessIsInstance(v, CGAffineTransform)

        v = CTFontGetSymbolicTraits(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CTFontCopyTraits(font)
        self.failUnlessIsInstance(v, CFDictionaryRef)

        v = CTFontCopyPostScriptName(font)
        self.failUnlessIsInstance(v, unicode)

        v = CTFontCopyFamilyName(font)
        self.failUnlessIsInstance(v, unicode)

        v = CTFontCopyFullName(font)
        self.failUnlessIsInstance(v, unicode)

        v = CTFontCopyDisplayName(font)
        self.failUnlessIsInstance(v, unicode)

        v = CTFontCopyName(font, kCTFontCopyrightNameKey)
        self.failUnlessIsInstance(v, unicode)

        v, l = CTFontCopyLocalizedName(font, kCTFontCopyrightNameKey, None)
        self.failUnlessIsInstance(v, unicode)
        self.failUnlessIsInstance(l, unicode)
        self.failUnlessArgIsOut(CTFontCopyLocalizedName, 2)

        v = CTFontCopyCharacterSet(font)
        self.failUnlessIsInstance(v, CFCharacterSetRef)

        v = CTFontGetStringEncoding(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CTFontCopySupportedLanguages(font)
        self.failUnlessIsInstance(v, CFArrayRef)

        self.failUnlessArgIsOut(CTFontGetGlyphsForCharacters, 2)
        v, gl = CTFontGetGlyphsForCharacters(font,
                u"hello", None, 5)

        self.failUnless(v is True)
        self.failUnlessIsInstance(gl, tuple)
        self.failUnlessEqual(len(gl), 5)
        self.failUnlessIsInstance(gl[0], (int, long))

        v = CTFontGetAscent(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetDescent(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetLeading(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetUnitsPerEm(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CTFontGetGlyphCount(font)
        self.failUnlessIsInstance(v, (int, long))

        v = CTFontGetBoundingBox(font)
        self.failUnlessIsInstance(v, CGRect)

        v = CTFontGetUnderlinePosition(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetUnderlineThickness(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetSlantAngle(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetCapHeight(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetXHeight(font)
        self.failUnlessIsInstance(v, float)

        v = CTFontGetGlyphWithName(font, "A")
        self.failUnlessIsInstance(v, (int, long))


        v, r = CTFontGetBoundingRectsForGlyphs(font,
                kCTFontDefaultOrientation, gl, None, 5)
        self.failUnlessIsInstance(v, CGRect)
        self.failUnlessIsInstance(r, tuple)
        self.failUnlessEqual(len(r), 5)
        self.failUnlessIsInstance(r[0], CGRect)


        v, r = CTFontGetAdvancesForGlyphs(font,
                kCTFontDefaultOrientation, gl, None, 5)
        self.failUnlessIsInstance(v, float)
        self.failUnlessIsInstance(r, tuple)
        self.failUnlessEqual(len(r), 5)
        self.failUnlessIsInstance(r[0], CGSize)

        r = CTFontGetVerticalTranslationsForGlyphs(font, gl, None, 5)
        self.failUnlessIsInstance(r, tuple)
        self.failUnlessEqual(len(r), 5)
        self.failUnlessIsInstance(r[0], CGSize)

        v = CTFontCreatePathForGlyph(font, gl[0], None)
        self.failUnlessIsInstance(v, CGPathRef)

        self.failUnlessResultIsCFRetained(CTFontCopyVariationAxes)
        v = CTFontCopyVariationAxes(font)
        if v is not None:
            self.failUnlessIsInstance(v, CFArrayRef)

        self.failUnlessResultIsCFRetained(CTFontCopyVariation)
        v = CTFontCopyVariation(font)
        if v is not None:
            self.failUnlessIsInstance(v, CFDictionaryRef)

        v = CTFontCopyFeatures(font)
        self.failUnlessIsInstance(v, CFArrayRef)
        self.failUnlessResultIsCFRetained(CTFontCopyFeatures)

        self.failUnlessResultIsCFRetained(CTFontCopyFeatureSettings)
        v = CTFontCopyFeatureSettings(font)
        if v is not None:
            self.failUnlessIsInstance(v, CFArrayRef)

        v, o = CTFontCopyGraphicsFont(font, None)
        self.failUnlessIsInstance(v, CGFontRef)
        if o is not None:
            self.failUnlessIsInstance(o, CTFontDescriptorRef)
        self.failUnlessResultIsCFRetained(CTFontCopyGraphicsFont)
        self.failUnlessArgIsCFRetained(CTFontCopyGraphicsFont, 1)
        self.failUnlessArgIsOut(CTFontCopyGraphicsFont, 1)

        v = CTFontCreateWithGraphicsFont(v, 20.5, None, None)
        self.failUnlessIsInstance(v, CTFontRef)
        self.failUnlessResultIsCFRetained(CTFontCreateWithGraphicsFont)

        if 0:
            # Cannot tests these because the ATS framework is not
            # wrapped.
            v, o = CTFontGetPlatformFont(font, None)
            self.failUnlessIsInstance(v, ATSFontRef)
            self.failUnlessIsInstance(o, CTFontDescriptorRef)

            v = CTFontCreateWithPlatformFont(v, 22.5, None, None)
            self.failUnlessIsInstance(v, CGFontRef)

        self.failUnlessArgIsCFRetained(CTFontGetPlatformFont, 1)
        self.failUnlessResultIsCFRetained(CTFontCreateWithPlatformFont)

        v = CTFontCopyAvailableTables(font, kCTFontTableOptionNoOptions)
        self.failUnlessIsInstance(v, tuple)

        v = CTFontCopyTable(font, v[0], 0)
        self.failUnlessIsInstance(v, CFDataRef)

        v = CTFontGetTypeID()
        self.failUnlessIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
