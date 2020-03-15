import AppKit
from PyObjCTools.TestSupport import TestCase, is32Bit, onlyOn32Bit

if is32Bit():

    class TestNSSimpleHorizontalTypesetterHelper(AppKit.NSSimpleHorizontalTypesetter):
        def willSetLineFragmentRect_forGlyphRange_usedRect_(self, a, b, c):
            return 1


class TestNSSimpleHorizontalTypesetter(TestCase):
    # @onlyOn32Bit
    def testConstants(self):
        self.assertEqual(AppKit.NSLayoutNotDone, 0)
        self.assertEqual(AppKit.NSLayoutDone, 1)
        self.assertEqual(AppKit.NSLayoutCantFit, 2)
        self.assertEqual(AppKit.NSLayoutOutOfGlyphs, 3)

        self.assertEqual(AppKit.NSGlyphLayoutAtAPoint, 0)
        self.assertEqual(AppKit.NSGlyphLayoutAgainstAPoint, 1)
        self.assertEqual(AppKit.NSGlyphLayoutWithPrevious, 2)

        self.assertEqual(AppKit.NSLayoutLeftToRight, 0)
        self.assertEqual(AppKit.NSLayoutRightToLeft, 1)

        self.assertEqual(AppKit.NSBaselineNotSet, -1.0)
        self.assertEqual(AppKit.NumGlyphsToGetEachTime, 20)

    @onlyOn32Bit
    def testMethods(self):
        self.assertArgIsOut(
            AppKit.NSSimpleHorizontalTypesetter.layoutGlyphsInLayoutManager_startingAtGlyphIndex_maxNumberOfLineFragments_nextGlyphIndex_,  # noqa: B950
            3,
        )
        self.assertArgIsInOut(
            AppKit.NSSimpleHorizontalTypesetter.layoutGlyphsInHorizontalLineFragment_baseline_,
            1,
        )
        self.assertArgIsBOOL(
            AppKit.NSSimpleHorizontalTypesetter.growGlyphCaches_fillGlyphInfo_, 1
        )

        self.assertArgIsInOut(
            TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_,  # noqa: B950
            2,
        )
        self.assertArgHasType(
            TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_,  # noqa: B950
            2,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_,  # noqa: B950
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_,  # noqa: B950
            0,
            b"N^" + AppKit.NSRect.__typestr__,
        )
