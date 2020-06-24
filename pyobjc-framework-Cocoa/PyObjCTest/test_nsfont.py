import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFont(TestCase):
    def matrixEquals(self, value1, value2):
        self.assertEqual(len(value1), len(value2))
        for v1, v2 in zip(value1, value2):
            # This should probably be 'assertAlmostEquals'
            self.assertEqual(v1, v2)

    def testMatrixMethods(self):
        o = AppKit.NSFont.boldSystemFontOfSize_(10)
        m = o.matrix()
        self.assertTrue(isinstance(m, tuple))
        self.assertEqual(len(m), 6)

        nm = o.fontName()

        o = AppKit.NSFont.fontWithName_matrix_(nm, AppKit.NSFontIdentityMatrix)
        self.assertTrue(o is not None)

        m = o.matrix()
        self.assertIsInstance(m, tuple)
        self.assertEqual(len(m), 6)

        self.matrixEquals(m, (1.0, 0.0, 0.0, 1.0, 0.0, 0.0))

        # For some reason Tiger transforms this matrix to the one below. The
        # same thing happens in pure ObjC code.
        # o = AppKit.NSFont.fontWithName_matrix_(nm, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
        o = AppKit.NSFont.fontWithName_matrix_(nm, (12.0, 0.0, 0.0, 12.0, 0.0, 0.0))
        self.assertTrue(o is not None)

        m = o.matrix()
        self.assertIsInstance(m, tuple)
        self.assertEqual(len(m), 6)

        # self.matrixEquals(m, (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
        self.matrixEquals(m, (12.0, 0.0, 0.0, 12.0, 0.0, 0.0))

        self.assertRaises(ValueError, AppKit.NSFont.fontWithName_matrix_, nm, "foo")
        self.assertRaises(
            ValueError, AppKit.NSFont.fontWithName_matrix_, nm, (1, 2, 3, 4)
        )
        self.assertRaises(
            ValueError,
            AppKit.NSFont.fontWithName_matrix_,
            nm,
            (1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0),
        )

    def testConstants(self):
        self.assertEqual(AppKit.NSFontIdentityMatrix, None)

        self.assertEqual(AppKit.NSControlGlyph, 0xFFFFFF)
        self.assertEqual(AppKit.NSNullGlyph, 0)
        self.assertEqual(AppKit.NSNativeShortGlyphPacking, 5)

        self.assertEqual(AppKit.NSFontDefaultRenderingMode, 0)
        self.assertEqual(AppKit.NSFontAntialiasedRenderingMode, 1)
        self.assertEqual(AppKit.NSFontIntegerAdvancementsRenderingMode, 2)
        self.assertEqual(AppKit.NSFontAntialiasedIntegerAdvancementsRenderingMode, 3)

        self.assertIsInstance(AppKit.NSAntialiasThresholdChangedNotification, str)
        self.assertIsInstance(AppKit.NSFontSetChangedNotification, str)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(AppKit.NSFont.getBoundingRects_forCGGlyphs_count_, 0)
        self.assertArgIsIn(AppKit.NSFont.getBoundingRects_forCGGlyphs_count_, 1)
        self.assertArgSizeInArg(AppKit.NSFont.getBoundingRects_forCGGlyphs_count_, 0, 2)
        self.assertArgSizeInArg(AppKit.NSFont.getBoundingRects_forCGGlyphs_count_, 1, 2)

        self.assertArgIsOut(AppKit.NSFont.getAdvancements_forCGGlyphs_count_, 0)
        self.assertArgIsIn(AppKit.NSFont.getAdvancements_forCGGlyphs_count_, 1)
        self.assertArgSizeInArg(AppKit.NSFont.getAdvancements_forCGGlyphs_count_, 0, 2)
        self.assertArgSizeInArg(AppKit.NSFont.getAdvancements_forCGGlyphs_count_, 1, 2)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSFont.isVertical)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSFont.isFixedPitch)
        self.assertArgIsOut(AppKit.NSFont.getBoundingRects_forGlyphs_count_, 0)
        self.assertArgHasType(
            AppKit.NSFont.getBoundingRects_forGlyphs_count_, 1, b"n^I"
        )
        self.assertArgSizeInArg(AppKit.NSFont.getBoundingRects_forGlyphs_count_, 0, 2)
        self.assertArgSizeInArg(AppKit.NSFont.getBoundingRects_forGlyphs_count_, 1, 2)
        self.assertArgIsOut(AppKit.NSFont.getAdvancements_forGlyphs_count_, 0)
        self.assertArgHasType(AppKit.NSFont.getAdvancements_forGlyphs_count_, 1, b"n^I")
        self.assertArgSizeInArg(AppKit.NSFont.getAdvancements_forGlyphs_count_, 0, 2)
        self.assertArgSizeInArg(AppKit.NSFont.getAdvancements_forGlyphs_count_, 1, 2)
        if hasattr(AppKit.NSFont, "getAdvancements_forPackedGlyphs_count_"):
            self.assertArgIsOut(AppKit.NSFont.getAdvancements_forPackedGlyphs_count_, 0)
            self.assertArgIsIn(AppKit.NSFont.getAdvancements_forPackedGlyphs_count_, 1)
        self.assertArgSizeInArg(
            AppKit.NSFont.getAdvancements_forPackedGlyphs_length_, 0, 2
        )
        self.assertArgSizeInArg(
            AppKit.NSFont.getAdvancements_forPackedGlyphs_length_, 1, 2
        )

    def testFunctions(self):
        glyphs = [ord("A"), ord("B"), ord("9"), ord("a")]

        rv, packed = AppKit.NSConvertGlyphsToPackedGlyphs(
            glyphs, len(glyphs), AppKit.NSNativeShortGlyphPacking, None
        )
        self.assertIsInstance(rv, int)
        self.assertIsInstance(packed, str)
        if rv == 0:
            self.assertEqual(len(packed), 0)

        else:
            self.assertEqual(len(packed), rv)
