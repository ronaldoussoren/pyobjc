
from PyObjCTools.TestSupport import *
from Quartz import *
import Quartz
import os

class TestCGPattern (TestCase):
    def testConstants(self):
        self.assertEqual(kCGPatternTilingNoDistortion, 0)
        self.assertEqual(kCGPatternTilingConstantSpacingMinimalDistortion, 1)
        self.assertEqual(kCGPatternTilingConstantSpacing, 2)

    def testFunctions(self):
        self.assertIsInstance(CGPatternGetTypeID(), (int, long))

        myInfo = object()
        cnt = [0]
        def drawPattern(info, context):
            self.assertTrue(info is myInfo)
            self.assertIsInstance(context, CGContextRef)
            cnt[0] += 1

        pattern = CGPatternCreate(myInfo, CGRectMake(0, 0, 10, 10), CGAffineTransformIdentity, 10.0, 10.0,
                kCGPatternTilingConstantSpacing, True, drawPattern)
        self.assertIsInstance(pattern, CGPatternRef)

        v = CGPatternRetain(pattern)
        self.assertTrue(v is pattern)
        CGPatternRelease(pattern)

        url = CFURLCreateWithFileSystemPath(None,
                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)
        context = CGPDFContextCreateWithURL(url,
            ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, CGContextRef)
        CGContextBeginPage(context, objc.NULL)
        try:
            color = CGColorCreateWithPattern(CGColorSpaceCreatePattern(None), pattern, (0.5, 0.5, 0.5, 0.5))
            self.assertIsInstance(color, CGColorRef)

            v = CGColorGetPattern(color)
            self.assertTrue(v is pattern)

            # Now draw something with the pattern color to ensure that the callback
            # is actually called at least once.
            CGContextSetFillColorWithColor(context, color)
            CGContextSetStrokeColorWithColor(context, color)
            CGContextFillRect(context, ((0, 0), (50, 50)))


        finally:
            CGContextEndPage(context)
            if hasattr(Quartz, 'CGPDFContextClose'): CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

        self.assertNotEqual(cnt[0], 0)


if __name__ == "__main__":
    main()
