
from PyObjCTools.TestSupport import *
from CoreText import *
from Foundation import NSDictionary
from Quartz.CoreGraphics import *

class TestCTRun (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CTRunRef)

    def testConstants(self):
        self.failUnlessEqual(kCTRunStatusNoStatus, 0)
        self.failUnlessEqual(kCTRunStatusRightToLeft, (1 << 0))
        self.failUnlessEqual(kCTRunStatusNonMonotonic, (1 << 1))
        self.failUnlessEqual(kCTRunStatusHasNonIdentityMatrix, (1 << 2))

    def testFunctions(self):
        self.failUnlessIsInstance(CTRunGetTypeID(), (int, long))

        line = CTLineCreateWithAttributedString(
                CFAttributedStringCreate(None, u"hello world", None))
        self.failUnlessIsInstance(line, CTLineRef)

        run = CTLineGetGlyphRuns(line)[0]
        self.failUnlessIsInstance(run, CTRunRef)

        v = CTRunGetGlyphCount(run)
        self.failUnlessIsInstance(v, (int, long))

        v = CTRunGetAttributes(run)
        self.failUnlessIsInstance(v, (dict, NSDictionary))

        v = CTRunGetStatus(run)
        self.failUnlessIsInstance(v, (int, long))

        buf = CTRunGetGlyphsPtr(run)
        self.failUnlessIsInstance(buf, objc.varlist)
        self.failUnlessIsInstance(buf[0], (int, long))

        buf = CTRunGetGlyphs(run, CFRange(0, 5), None)
        self.failUnlessIsInstance(buf, tuple)
        self.failUnlessEqual(len(buf), 5)
        self.failUnlessIsInstance(buf[0], (int, long))

        buf = CTRunGetPositionsPtr(run)
        self.failUnlessIsInstance(buf, objc.varlist)
        self.failUnlessIsInstance(buf[0], CGPoint)

        buf = CTRunGetPositions(run, CFRange(0, 5), None)
        self.failUnlessIsInstance(buf, tuple)
        self.failUnlessEqual(len(buf), 5)
        self.failUnlessIsInstance(buf[0], CGPoint)

        buf = CTRunGetStringIndicesPtr(run)
        self.failUnlessIsInstance(buf, objc.varlist)
        self.failUnlessIsInstance(buf[0], (int, long))

        buf = CTRunGetStringIndices(run, CFRange(0, 5), None)
        self.failUnlessIsInstance(buf, tuple)
        self.failUnlessEqual(len(buf), 5)
        self.failUnlessIsInstance(buf[0], (int, long))

        v = CTRunGetStringRange(run)
        self.failUnlessIsInstance(v, CFRange)

        v = CTRunGetTypographicBounds(run, CFRange(0, 5), None, None, None)
        self.failUnlessIsInstance(v, tuple)
        self.failUnlessEqual(len(v), 4)
        self.failUnlessIsInstance(v[0], float)
        self.failUnlessIsInstance(v[1], float)
        self.failUnlessIsInstance(v[2], float)
        self.failUnlessIsInstance(v[3], float)

        url = CFURLCreateWithFileSystemPath(None,
                                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)

        ctx = CGPDFContextCreateWithURL(url, CGRect(CGPoint(0, 0), CGSize(1000, 1000)), None)
        v = CTRunGetImageBounds(run, ctx, CFRange(0, 5))
        self.failUnlessIsInstance(v, CGRect)

        v = CTRunGetTextMatrix(run)
        self.failUnlessIsInstance(v, CGAffineTransform)

        v = CTRunDraw(run, ctx, CFRange(0, 5))
        self.failUnless(v is None)



if __name__ == "__main__":
    main()
