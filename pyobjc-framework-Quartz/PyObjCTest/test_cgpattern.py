
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
import os

class TestCGPattern (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCGPatternTilingNoDistortion, 0)
        self.failUnlessEqual(kCGPatternTilingConstantSpacingMinimalDistortion, 1)
        self.failUnlessEqual(kCGPatternTilingConstantSpacing, 2)

    def testFunctions(self):
        self.failUnlessIsInstance(CGPatternGetTypeID(), (int, long))

        myInfo = object()
        cnt = [0]
        def drawPattern(info, context):
            self.failUnless(info is myInfo)
            self.failUnlessIsInstance(context, CGContextRef)
            cnt[0] += 1

        pattern = CGPatternCreate(myInfo, CGRectMake(0, 0, 10, 10), CGAffineTransformIdentity, 10.0, 10.0,
                kCGPatternTilingConstantSpacing, True, drawPattern)
        self.failUnlessIsInstance(pattern, CGPatternRef)

        v = CGPatternRetain(pattern)
        self.failUnless(v is pattern)
        CGPatternRelease(pattern)

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.failUnlessIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
            ((0, 0), (1000, 1000)), None)
        self.failUnlessIsInstance(context, CGContextRef)
        CGContextBeginPage(context, objc.NULL)
        try:
            color = CGColorCreateWithPattern(CGColorSpaceCreatePattern(None), pattern, (0.5, 0.5, 0.5, 0.5))
            self.failUnlessIsInstance(color, CGColorRef)

            v = CGColorGetPattern(color)
            self.failUnless(v is pattern)

            # Now draw something with the pattern color to ensure that the callback
            # is actually called at least once.
            CGContextSetFillColorWithColor(context, color)
            CGContextSetStrokeColorWithColor(context, color)
            CGContextFillRect(context, ((0, 0), (50, 50)))


        finally:
            CGContextEndPage(context)
            CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

        self.failIfEqual(cnt[0], 0)


if __name__ == "__main__":
    main()
