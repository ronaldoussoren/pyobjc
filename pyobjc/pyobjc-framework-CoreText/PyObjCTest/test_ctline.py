
from PyObjCTools.TestSupport import *
from CoreText import *
from Quartz.CoreGraphics import *

import os

class TestCTLine (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(CTLineRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessEqual(kCTLineTruncationStart, 0)
        self.failUnlessEqual(kCTLineTruncationEnd, 1)
        self.failUnlessEqual(kCTLineTruncationMiddle, 2)

    def testFunctions(self):
        v = CTLineGetTypeID()
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessResultIsCFRetained(CTLineCreateWithAttributedString)
        token = CTLineCreateWithAttributedString(
                CFAttributedStringCreate(None, u"-", None))
        self.failUnlessIsInstance(token, CTLineRef)

        line = CTLineCreateWithAttributedString(
                CFAttributedStringCreate(None, u"hello world", None))
        self.failUnlessIsInstance(line, CTLineRef)

        self.failUnlessResultIsCFRetained(CTLineCreateTruncatedLine)
        v = CTLineCreateTruncatedLine(line, 20.0, kCTLineTruncationStart, token)
        self.failUnlessIsInstance(v, CTLineRef)

        self.failUnlessResultIsCFRetained(CTLineCreateJustifiedLine)
        v = CTLineCreateJustifiedLine(line, 0.75, 20.0)
        self.failUnlessIsInstance(v, CTLineRef)

        v = CTLineGetGlyphCount(line)
        self.failUnlessIsInstance(v, (int, long))

        v = CTLineGetGlyphRuns(line)
        self.failUnlessIsInstance(v, CFArrayRef)
        
        v = CTLineGetStringRange(line)
        self.failUnlessIsInstance(v, CFRange)

        v = CTLineGetPenOffsetForFlush(line, 0.5, 40.0)
        self.failUnlessIsInstance(v, float)

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        ctx = CGPDFContextCreateWithURL(url, CGRect(CGPoint(0, 0), CGSize(1000, 1000)), None)
        self.failUnlessIsInstance(ctx, CGContextRef)

        CTLineDraw(line, ctx)

        v = CTLineGetImageBounds(line, ctx)
        self.failUnlessIsInstance(v, CGRect)

        self.failUnlessArgIsOut(CTLineGetTypographicBounds, 1)
        self.failUnlessArgIsOut(CTLineGetTypographicBounds, 2)
        self.failUnlessArgIsOut(CTLineGetTypographicBounds, 3)

        v = CTLineGetTypographicBounds(line, None, None, None)
        self.failUnlessIsInstance(v, tuple)
        self.failUnlessIsInstance(v[0], float)
        self.failUnlessIsInstance(v[1], float)
        self.failUnlessIsInstance(v[2], float)
        self.failUnlessIsInstance(v[3], float)

        v = CTLineGetTrailingWhitespaceWidth(line)
        self.failUnlessIsInstance(v, float)

        v = CTLineGetStringIndexForPosition(line, CGPoint(10, 10))
        self.failUnlessIsInstance(v, (int, long))

        self.failUnlessArgIsOut(CTLineGetOffsetForStringIndex, 2)
        v = CTLineGetOffsetForStringIndex(line, 2, None)
        self.failUnlessIsInstance(v, tuple)
        self.failUnlessIsInstance(v[0], float)
        self.failUnlessIsInstance(v[1], float)


        if os.path.exists("/tmp/pyobjc.test.pdf"):
            os.unlink("/tmp/pyobjc.test.pdf")

if __name__ == "__main__":
    main()
