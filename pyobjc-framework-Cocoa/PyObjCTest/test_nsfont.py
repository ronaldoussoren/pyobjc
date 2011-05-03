from PyObjCTools.TestSupport import *
import objc

import AppKit
from AppKit import *

import os

class TestNSFont(TestCase):
    def matrixEquals(self, value1, value2):
        self.assertEqual(len(value1), len(value2))
        for v1, v2 in zip(value1, value2):
            # This should probably be 'assertAlmostEquals'
            self.assertEqual(v1, v2)


    def testMatrixMethods(self):
        o = AppKit.NSFont.boldSystemFontOfSize_(10);
        m = o.matrix()
        self.assert_(isinstance(m, tuple))
        self.assertEqual(len(m), 6)

        nm = o.fontName()

        o = AppKit.NSFont.fontWithName_matrix_(
                nm, AppKit.NSFontIdentityMatrix)
        self.assert_(o is not None)

        m = o.matrix()
        self.assert_(isinstance(m, tuple))
        self.assertEqual(len(m), 6)

        self.matrixEquals(m, (1.0, 0.0, 0.0, 1.0, 0.0, 0.0))

        # For some reason Tiger transforms this matrix to the one below. The
        # same thing happens in pure ObjC code.
        #o = AppKit.NSFont.fontWithName_matrix_(nm, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
        o = AppKit.NSFont.fontWithName_matrix_(nm, (12.0, 0.0, 0.0, 12.0, 0.0, 0.0))
        self.assert_(o is not None)

        m = o.matrix()
        self.assert_(isinstance(m, tuple))
        self.assertEqual(len(m), 6)

        #self.matrixEquals(m, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
        self.matrixEquals(m, (12.0, 0.0, 0.0, 12.0, 0.0, 0.0))

        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, "foo")
        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, (1, 2, 3, 4))
        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0))


    def testConstants(self):
        self.assertEqual(AppKit.NSFontIdentityMatrix, None)

        self.assertEqual(NSControlGlyph, 0xffffff)
        self.assertEqual(NSNullGlyph, 0)
        self.assertEqual(NSNativeShortGlyphPacking, 5)

        self.assertEqual(NSFontDefaultRenderingMode, 0)
        self.assertEqual(NSFontAntialiasedRenderingMode, 1)
        self.assertEqual(NSFontIntegerAdvancementsRenderingMode, 2)
        self.assertEqual(NSFontAntialiasedIntegerAdvancementsRenderingMode, 3)

        self.assertIsInstance(NSAntialiasThresholdChangedNotification, unicode)
        self.assertIsInstance(NSFontSetChangedNotification, unicode)

    @onlyOn32Bit
    def testConstants_32bitonly(self):
        self.assertEqual(NSOneByteGlyphPacking, 0)
        self.assertEqual(NSJapaneseEUCGlyphPacking, 1)
        self.assertEqual(NSAsciiWithDoubleByteEUCGlyphPacking, 2)
        self.assertEqual(NSTwoByteGlyphPacking, 3)
        self.assertEqual(NSFourByteGlyphPacking, 4)

        self.assertEqual(NSGlyphBelow, 1)
        self.assertEqual(NSGlyphAbove, 2)

        self.assertIsInstance(NSAFMFamilyName, unicode)
        self.assertIsInstance(NSAFMFontName, unicode)
        self.assertIsInstance(NSAFMFormatVersion, unicode)
        self.assertIsInstance(NSAFMFullName, unicode)
        self.assertIsInstance(NSAFMNotice, unicode)
        self.assertIsInstance(NSAFMVersion, unicode)
        self.assertIsInstance(NSAFMWeight, unicode)
        self.assertIsInstance(NSAFMEncodingScheme, unicode)
        self.assertIsInstance(NSAFMCharacterSet, unicode)
        self.assertIsInstance(NSAFMCapHeight, unicode)
        self.assertIsInstance(NSAFMXHeight, unicode)
        self.assertIsInstance(NSAFMAscender, unicode)
        self.assertIsInstance(NSAFMDescender, unicode)
        self.assertIsInstance(NSAFMUnderlinePosition, unicode)
        self.assertIsInstance(NSAFMUnderlineThickness, unicode)
        self.assertIsInstance(NSAFMItalicAngle, unicode)
        self.assertIsInstance(NSAFMMappingScheme, unicode)





    def testMethods(self):
        self.assertResultIsBOOL(NSFont.isFixedPitch)
        self.assertArgHasType(NSFont.getBoundingRects_forGlyphs_count_, 1, b'n^I')
        self.assertArgSizeInArg(NSFont.getBoundingRects_forGlyphs_count_, 0, 2)
        self.assertArgSizeInArg(NSFont.getBoundingRects_forGlyphs_count_, 1, 2)
        self.assertArgHasType(NSFont.getAdvancements_forGlyphs_count_, 1, b'n^I')
        self.assertArgSizeInArg(NSFont.getAdvancements_forGlyphs_count_, 0, 2)
        self.assertArgSizeInArg(NSFont.getAdvancements_forGlyphs_count_, 1, 2)
        self.assertArgSizeInArg(NSFont.getAdvancements_forPackedGlyphs_length_, 0, 2)
        self.assertArgSizeInArg(NSFont.getAdvancements_forPackedGlyphs_length_, 1, 2)

    @onlyOn32Bit
    def testMethods32(self):
        self.assertResultIsBOOL(NSFont.isBaseFont)
        self.assertResultIsBOOL(NSFont.glyphIsEncoded_)
        self.assertArgHasType(NSFont.glyphIsEncoded_, 0, b'I')
        self.assertArgHasType(NSFont.positionOfGlyph_precededByGlyph_isNominal_, 0, b'I')
        self.assertArgHasType(NSFont.positionOfGlyph_precededByGlyph_isNominal_, 1, b'I')
        self.assertArgHasType(NSFont.positionOfGlyph_precededByGlyph_isNominal_, 2, b'o^'+objc._C_NSBOOL)
        
        self.assertArgHasType(NSFont.positionsForCompositeSequence_numberOfGlyphs_pointArray_, 0, b'n^I')
        self.assertArgSizeInArg(NSFont.positionsForCompositeSequence_numberOfGlyphs_pointArray_, 0, 1)
        self.assertArgHasType(NSFont.positionsForCompositeSequence_numberOfGlyphs_pointArray_, 2, b'o^'+NSPoint.__typestr__)
        self.assertArgSizeInArg(NSFont.positionsForCompositeSequence_numberOfGlyphs_pointArray_, 2, 1)

        self.assertArgHasType(NSFont.positionOfGlyph_struckOverGlyph_metricsExist_, 2, b'o^' + objc._C_NSBOOL)
        self.assertArgHasType(NSFont.positionOfGlyph_struckOverRect_metricsExist_, 2, b'o^' + objc._C_NSBOOL)
        self.assertArgHasType(NSFont.positionOfGlyph_withRelation_toBaseGlyph_totalAdvancement_metricsExist_, 3, b'o^' + NSSize.__typestr__)
        self.assertArgHasType(NSFont.positionOfGlyph_withRelation_toBaseGlyph_totalAdvancement_metricsExist_, 4, b'o^' + objc._C_NSBOOL)


    def testFunctions(self):
        glyphs = [ ord('A'), ord('B'), ord('9'), ord('a') ]

        rv, packed = NSConvertGlyphsToPackedGlyphs(glyphs, len(glyphs), NSNativeShortGlyphPacking, None)
        self.assertIsInstance(rv, (int, long))
        self.assertIsInstance(packed, str)
        if rv == 0:
            self.assertEqual(len(packed), 0)

        else:
            self.assertEqual(len(packed), rv)

if __name__ == '__main__':
    main( )
