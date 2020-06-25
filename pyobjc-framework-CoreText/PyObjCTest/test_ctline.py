import os

import CoreText
import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCTLine(TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreText.CTLineRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(CoreText.kCTLineTruncationStart, 0)
        self.assertEqual(CoreText.kCTLineTruncationEnd, 1)
        self.assertEqual(CoreText.kCTLineTruncationMiddle, 2)

    def testFunctions(self):
        v = CoreText.CTLineGetTypeID()
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(CoreText.CTLineCreateWithAttributedString)
        astr = CoreText.CFAttributedStringCreate(None, "-", None)
        self.assertTrue(astr is not None)
        token = CoreText.CTLineCreateWithAttributedString(astr)
        self.assertIsInstance(token, CoreText.CTLineRef)

        astr = CoreText.CFAttributedStringCreate(None, "hello world", None)
        self.assertTrue(astr is not None)
        line = CoreText.CTLineCreateWithAttributedString(astr)
        self.assertIsInstance(line, CoreText.CTLineRef)

        self.assertResultIsCFRetained(CoreText.CTLineCreateTruncatedLine)
        v = CoreText.CTLineCreateTruncatedLine(
            line, 20.0, CoreText.kCTLineTruncationStart, token
        )
        self.assertIsInstance(v, CoreText.CTLineRef)

        self.assertResultIsCFRetained(CoreText.CTLineCreateJustifiedLine)
        v = CoreText.CTLineCreateJustifiedLine(line, 2.0, 123.0)
        self.assertIsInstance(v, CoreText.CTLineRef)

        v = CoreText.CTLineGetGlyphCount(line)
        self.assertIsInstance(v, int)

        v = CoreText.CTLineGetGlyphRuns(line)
        self.assertIsInstance(v, CoreText.CFArrayRef)

        v = CoreText.CTLineGetStringRange(line)
        self.assertIsInstance(v, CoreText.CFRange)

        v = CoreText.CTLineGetPenOffsetForFlush(line, 0.5, 40.0)
        self.assertIsInstance(v, float)

        url = CoreText.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", CoreText.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, CoreText.CFURLRef)
        ctx = CoreText.CGPDFContextCreateWithURL(
            url, Quartz.CGRect(Quartz.CGPoint(0, 0), Quartz.CGSize(1000, 1000)), None
        )
        self.assertIsInstance(ctx, Quartz.CGContextRef)

        CoreText.CTLineDraw(line, ctx)

        v = CoreText.CTLineGetImageBounds(line, ctx)
        self.assertIsInstance(v, CoreText.CGRect)

        self.assertArgIsOut(CoreText.CTLineGetTypographicBounds, 1)
        self.assertArgIsOut(CoreText.CTLineGetTypographicBounds, 2)
        self.assertArgIsOut(CoreText.CTLineGetTypographicBounds, 3)

        v = CoreText.CTLineGetTypographicBounds(line, None, None, None)
        self.assertIsInstance(v, tuple)
        self.assertIsInstance(v[0], float)
        self.assertIsInstance(v[1], float)
        self.assertIsInstance(v[2], float)
        self.assertIsInstance(v[3], float)

        v = CoreText.CTLineGetTrailingWhitespaceWidth(line)
        self.assertIsInstance(v, float)

        v = CoreText.CTLineGetStringIndexForPosition(line, CoreText.CGPoint(10, 10))
        self.assertIsInstance(v, int)

        self.assertArgIsOut(CoreText.CTLineGetOffsetForStringIndex, 2)
        v = CoreText.CTLineGetOffsetForStringIndex(line, 2, None)
        self.assertIsInstance(v, tuple)
        self.assertIsInstance(v[0], float)
        self.assertIsInstance(v[1], float)

        if os.path.exists("/tmp/pyobjc.test.pdf"):
            os.unlink("/tmp/pyobjc.test.pdf")

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(CoreText.kCTLineBoundsExcludeTypographicLeading, 1 << 0)
        self.assertEqual(CoreText.kCTLineBoundsExcludeTypographicShifts, 1 << 1)
        self.assertEqual(CoreText.kCTLineBoundsUseHangingPunctuation, 1 << 2)
        self.assertEqual(CoreText.kCTLineBoundsUseGlyphPathBounds, 1 << 3)
        self.assertEqual(CoreText.kCTLineBoundsUseOpticalBounds, 1 << 4)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(CoreText.kCTLineBoundsIncludeLanguageExtents, 1 << 5)

    @min_os_level("10.8")
    def testFunctions10_8(self):
        astr = CoreText.CFAttributedStringCreate(None, "-", None)
        self.assertTrue(astr is not None)

        token = CoreText.CTLineCreateWithAttributedString(astr)
        self.assertIsInstance(token, CoreText.CTLineRef)

        r = CoreText.CTLineGetBoundsWithOptions(
            token, CoreText.kCTLineBoundsExcludeTypographicLeading
        )
        self.assertIsInstance(r, Quartz.CGRect)

    @min_os_level("10.11")
    def testFunctions10_11(self):
        self.assertArgIsBlock(CoreText.CTLineEnumerateCaretOffsets, 1, b"vdLBo^B")
