
from PyObjCTools.TestSupport import *
from CoreText import *
from Quartz.CoreGraphics import *

import os

class TestCTFrame (TestCase):

    def testTypes(self):
        self.failUnlessIsInstance(CTFrameRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessEqual(kCTFrameProgressionTopToBottom, 0)
        self.failUnlessEqual(kCTFrameProgressionRightToLeft, 1)

        self.failUnlessIsInstance(kCTFrameProgressionAttributeName, unicode)

    def testFunctions(self):
        v = CTFrameGetTypeID()
        self.failUnlessIsInstance(v, (int, long))

        setter = CTFramesetterCreateWithAttributedString(
                CFAttributedStringCreate(None, u"hello", None))
        self.failUnlessIsInstance(setter, CTFramesetterRef)

        path = CGPathCreateMutable()
        self.failUnlessIsInstance(path, CGPathRef)
        CGPathAddRect(path, None, CGRect(CGPoint(0, 0), CGSize(400, 400)))
        attr = { 'foo': 42 }
        frame = CTFramesetterCreateFrame(setter, CFRange(0, 5), 
                path, attr)
        self.failUnlessIsInstance(frame, CTFrameRef)

        v = CTFrameGetStringRange(frame)
        self.failUnlessIsInstance(v, CFRange)

        v = CTFrameGetVisibleStringRange(frame)
        self.failUnlessIsInstance(v, CFRange)

        self.failIfResultIsCFRetained(CTFrameGetPath)
        v = CTFrameGetPath(frame)
        self.failUnlessIsInstance(v, CGPathRef)

        v = CTFrameGetFrameAttributes(frame)
        self.failUnless(v is attr)

        v = CTFrameGetLines(frame)
        self.failUnlessIsInstance(v, CFArrayRef)

        v = CTFrameGetLineOrigins(frame, CFRange(0, 1), None)
        self.failUnlessIsInstance(v, tuple)
        self.failUnlessEqual(len(v), 1)
        self.failUnlessIsInstance(v[0], CGPoint)

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        ctx = CGPDFContextCreateWithURL(url, CGRect(CGPoint(0, 0), CGSize(1000, 1000)), None)
        self.failUnlessIsInstance(ctx, CGContextRef)

        CTFrameDraw(frame, ctx)

        if os.path.exists("/tmp/pyobjc.test.pdf"):
            os.unlink("/tmp/pyobjc.test.pdf")


if __name__ == "__main__":
    main()
