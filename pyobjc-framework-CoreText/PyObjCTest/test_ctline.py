
from PyObjCTools.TestSupport import *
from CoreText import *
from Quartz import *

import os

try:
    long
except NameError:
    long = int

class TestCTLine (TestCase):
    def testTypes(self):
        self.assertIsInstance(CTLineRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(kCTLineTruncationStart, 0)
        self.assertEqual(kCTLineTruncationEnd, 1)
        self.assertEqual(kCTLineTruncationMiddle, 2)

    def testFunctions(self):
        v = CTLineGetTypeID()
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(CTLineCreateWithAttributedString)
        astr = CFAttributedStringCreate(None, b"-".decode('latin1'), None)
        self.assertTrue(astr is not None)
        token = CTLineCreateWithAttributedString(astr)
        self.assertIsInstance(token, CTLineRef)

        astr = CFAttributedStringCreate(None, b"hello world".decode('latin1'), None)
        self.assertTrue(astr is not None)
        line = CTLineCreateWithAttributedString(astr)
        self.assertIsInstance(line, CTLineRef)

        self.assertResultIsCFRetained(CTLineCreateTruncatedLine)
        v = CTLineCreateTruncatedLine(line, 20.0, kCTLineTruncationStart, token)
        self.assertIsInstance(v, CTLineRef)

        self.assertResultIsCFRetained(CTLineCreateJustifiedLine)
        v = CTLineCreateJustifiedLine(line, 2.0, 123.0)
        self.assertIsInstance(v, CTLineRef)

        v = CTLineGetGlyphCount(line)
        self.assertIsInstance(v, (int, long))

        v = CTLineGetGlyphRuns(line)
        self.assertIsInstance(v, CFArrayRef)

        v = CTLineGetStringRange(line)
        self.assertIsInstance(v, CFRange)

        v = CTLineGetPenOffsetForFlush(line, 0.5, 40.0)
        self.assertIsInstance(v, float)

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        ctx = CGPDFContextCreateWithURL(url, CGRect(CGPoint(0, 0), CGSize(1000, 1000)), None)
        self.assertIsInstance(ctx, CGContextRef)

        CTLineDraw(line, ctx)

        v = CTLineGetImageBounds(line, ctx)
        self.assertIsInstance(v, CGRect)

        self.assertArgIsOut(CTLineGetTypographicBounds, 1)
        self.assertArgIsOut(CTLineGetTypographicBounds, 2)
        self.assertArgIsOut(CTLineGetTypographicBounds, 3)

        v = CTLineGetTypographicBounds(line, None, None, None)
        self.assertIsInstance(v, tuple)
        self.assertIsInstance(v[0], float)
        self.assertIsInstance(v[1], float)
        self.assertIsInstance(v[2], float)
        self.assertIsInstance(v[3], float)

        v = CTLineGetTrailingWhitespaceWidth(line)
        self.assertIsInstance(v, float)

        v = CTLineGetStringIndexForPosition(line, CGPoint(10, 10))
        self.assertIsInstance(v, (int, long))

        self.assertArgIsOut(CTLineGetOffsetForStringIndex, 2)
        v = CTLineGetOffsetForStringIndex(line, 2, None)
        self.assertIsInstance(v, tuple)
        self.assertIsInstance(v[0], float)
        self.assertIsInstance(v[1], float)


        if os.path.exists("/tmp/pyobjc.test.pdf"):
            os.unlink("/tmp/pyobjc.test.pdf")

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(kCTLineBoundsExcludeTypographicLeading, 1 << 0)
        self.assertEqual(kCTLineBoundsExcludeTypographicShifts, 1 << 1)
        self.assertEqual(kCTLineBoundsUseHangingPunctuation, 1 << 2)
        self.assertEqual(kCTLineBoundsUseGlyphPathBounds, 1 << 3)
        self.assertEqual(kCTLineBoundsUseOpticalBounds, 1 << 4)

    @min_os_level("10.8")
    def testFunctions10_8(self):
        astr = CFAttributedStringCreate(None, b"-".decode('latin1'), None)
        self.assertTrue(astr is not None)

        token = CTLineCreateWithAttributedString(astr)
        self.assertIsInstance(token, CTLineRef)

        r = CTLineGetBoundsWithOptions(token, kCTLineBoundsExcludeTypographicLeading)
        self.assertIsInstance(r, CGRect)

if __name__ == "__main__":
    main()
