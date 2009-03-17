from PyObjCTools.TestSupport import *
import objc

import AppKit
from AppKit import *

import os

class TestNSFont(TestCase):
    def matrixEquals(self, value1, value2):
        self.assertEquals(len(value1), len(value2))
        for v1, v2 in zip(value1, value2):
            # This should probably be 'assertAlmostEquals'
            self.assertEquals(v1, v2)


    def testMatrixMethods(self):
        o = AppKit.NSFont.boldSystemFontOfSize_(10);
        m = o.matrix()
        self.assert_(isinstance(m, tuple))
        self.assertEquals(len(m), 6)

        nm = o.fontName()

        o = AppKit.NSFont.fontWithName_matrix_(
                nm, AppKit.NSFontIdentityMatrix)
        self.assert_(o is not None)

        m = o.matrix()
        self.assert_(isinstance(m, tuple))
        self.assertEquals(len(m), 6)

        self.matrixEquals(m, (1.0, 0.0, 0.0, 1.0, 0.0, 0.0))

        # For some reason Tiger transforms this matrix to the one below. The
        # same thing happens in pure ObjC code.
        #o = AppKit.NSFont.fontWithName_matrix_(nm, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
        o = AppKit.NSFont.fontWithName_matrix_(nm, (12.0, 0.0, 0.0, 12.0, 0.0, 0.0))
        self.assert_(o is not None)

        m = o.matrix()
        self.assert_(isinstance(m, tuple))
        self.assertEquals(len(m), 6)

        #self.matrixEquals(m, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
        self.matrixEquals(m, (12.0, 0.0, 0.0, 12.0, 0.0, 0.0))

        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, "foo")
        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, (1, 2, 3, 4))
        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0))


    def testConstants(self):
        self.assertEquals(AppKit.NSFontIdentityMatrix, None)

        self.failUnlessEqual(NSControlGlyph, 0xffffff)
        self.failUnlessEqual(NSNullGlyph, 0)
        self.failUnlessEqual(NSNativeShortGlyphPacking, 5)

        self.failUnlessEqual(NSFontDefaultRenderingMode, 0)
        self.failUnlessEqual(NSFontAntialiasedRenderingMode, 1)
        self.failUnlessEqual(NSFontIntegerAdvancementsRenderingMode, 2)
        self.failUnlessEqual(NSFontAntialiasedIntegerAdvancementsRenderingMode, 3)

        self.failUnlessIsInstance(NSAntialiasThresholdChangedNotification, unicode)
        self.failUnlessIsInstance(NSFontSetChangedNotification, unicode)

    @onlyOn32Bit
    def testConstants_32bitonly(self):
        self.failUnlessEqual(NSOneByteGlyphPacking, 0)
        self.failUnlessEqual(NSJapaneseEUCGlyphPacking, 1)
        self.failUnlessEqual(NSAsciiWithDoubleByteEUCGlyphPacking, 2)
        self.failUnlessEqual(NSTwoByteGlyphPacking, 3)
        self.failUnlessEqual(NSFourByteGlyphPacking, 4)

        self.failUnlessEqual(NSGlyphBelow, 1)
        self.failUnlessEqual(NSGlyphAbove, 2)

        self.failUnlessIsInstance(NSAFMFamilyName, unicode)
        self.failUnlessIsInstance(NSAFMFontName, unicode)
        self.failUnlessIsInstance(NSAFMFormatVersion, unicode)
        self.failUnlessIsInstance(NSAFMFullName, unicode)
        self.failUnlessIsInstance(NSAFMNotice, unicode)
        self.failUnlessIsInstance(NSAFMVersion, unicode)
        self.failUnlessIsInstance(NSAFMWeight, unicode)
        self.failUnlessIsInstance(NSAFMEncodingScheme, unicode)
        self.failUnlessIsInstance(NSAFMCharacterSet, unicode)
        self.failUnlessIsInstance(NSAFMCapHeight, unicode)
        self.failUnlessIsInstance(NSAFMXHeight, unicode)
        self.failUnlessIsInstance(NSAFMAscender, unicode)
        self.failUnlessIsInstance(NSAFMDescender, unicode)
        self.failUnlessIsInstance(NSAFMUnderlinePosition, unicode)
        self.failUnlessIsInstance(NSAFMUnderlineThickness, unicode)
        self.failUnlessIsInstance(NSAFMItalicAngle, unicode)
        self.failUnlessIsInstance(NSAFMMappingScheme, unicode)





    def testMethods(self):
        self.failUnlessResultIsBOOL(NSFont.isFixedPitch)
        self.failUnlessArgHasType(NSFont.getBoundingRects_forGlyphs_count_, 1, 'n^I')
        self.failUnlessArgSizeInArg(NSFont.getBoundingRects_forGlyphs_count_, 0, 2)
        self.failUnlessArgSizeInArg(NSFont.getBoundingRects_forGlyphs_count_, 1, 2)
        self.failUnlessArgHasType(NSFont.getAdvancements_forGlyphs_count_, 1, 'n^I')
        self.failUnlessArgSizeInArg(NSFont.getAdvancements_forGlyphs_count_, 0, 2)
        self.failUnlessArgSizeInArg(NSFont.getAdvancements_forGlyphs_count_, 1, 2)
        self.failUnlessArgSizeInArg(NSFont.getAdvancements_forPackedGlyphs_length_, 0, 2)
        self.failUnlessArgSizeInArg(NSFont.getAdvancements_forPackedGlyphs_length_, 1, 2)

    @onlyOn32Bit
    def testMethods32(self):
        self.failUnlessResultIsBOOL(NSFont.isBaseFont)
        self.failUnlessResultIsBOOL(NSFont.glyphIsEncoded_)
        self.failUnlessArgHasType(NSFont.glyphIsEncoded_, 0, 'I')
        self.failUnlessArgHasType(NSFont.positionOfGlyph_precededByGlyph_isNominal_, 0, 'I')
        self.failUnlessArgHasType(NSFont.positionOfGlyph_precededByGlyph_isNominal_, 1, 'I')
        self.failUnlessArgHasType(NSFont.positionOfGlyph_precededByGlyph_isNominal_, 2, 'o^'+objc._C_NSBOOL)
        
        self.failUnlessArgHasType(NSFont.positionsForCompositeSequence_numberOfGlyphs_pointArray_, 0, 'n^I')
        self.failUnlessArgSizeInArg(NSFont.positionsForCompositeSequence_numberOfGlyphs_pointArray_, 0, 1)
        self.failUnlessArgHasType(NSFont.positionsForCompositeSequence_numberOfGlyphs_pointArray_, 2, 'o^'+NSPoint.__typestr__)
        self.failUnlessArgSizeInArg(NSFont.positionsForCompositeSequence_numberOfGlyphs_pointArray_, 2, 1)

        self.failUnlessArgHasType(NSFont.positionOfGlyph_struckOverGlyph_metricsExist_, 2, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgHasType(NSFont.positionOfGlyph_struckOverRect_metricsExist_, 2, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgHasType(NSFont.positionOfGlyph_withRelation_toBaseGlyph_totalAdvancement_metricsExist_, 3, 'o^' + NSSize.__typestr__)
        self.failUnlessArgHasType(NSFont.positionOfGlyph_withRelation_toBaseGlyph_totalAdvancement_metricsExist_, 4, 'o^' + objc._C_NSBOOL)


    def testFunctions(self):
        glyphs = [ ord('A'), ord('B'), ord('9'), ord('a') ]

        rv, packed = NSConvertGlyphsToPackedGlyphs(glyphs, len(glyphs), NSNativeShortGlyphPacking, None)
        self.failUnlessIsInstance(rv, (int, long))
        self.failUnlessIsInstance(packed, str)
        if rv == 0:
            self.failUnlessEqual(len(packed), 0)

        else:
            self.failUnlessEqual(len(packed), rv)

if __name__ == '__main__':
    main( )
