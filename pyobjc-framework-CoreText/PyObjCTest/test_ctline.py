
from PyObjCTools.TestSupport import *
from CoreText import *
from Quartz import *

import os

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
        token = CTLineCreateWithAttributedString(
                CFAttributedStringCreate(None, u"-", None))
        self.assertIsInstance(token, CTLineRef)

        line = CTLineCreateWithAttributedString(
                CFAttributedStringCreate(None, u"hello world", None))
        self.assertIsInstance(line, CTLineRef)

        self.assertResultIsCFRetained(CTLineCreateTruncatedLine)
        v = CTLineCreateTruncatedLine(line, 20.0, kCTLineTruncationStart, token)
        self.assertIsInstance(v, CTLineRef)

        self.assertResultIsCFRetained(CTLineCreateJustifiedLine)
        v = CTLineCreateJustifiedLine(line, 0.75, 20.0)
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

if __name__ == "__main__":
    main()
