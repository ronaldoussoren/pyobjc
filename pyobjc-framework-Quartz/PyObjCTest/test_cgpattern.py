import os

import Quartz
from PyObjCTools.TestSupport import TestCase
import objc


class TestCGPattern(TestCase):
    def testConstants(self):
        self.assertEqual(Quartz.kCGPatternTilingNoDistortion, 0)
        self.assertEqual(Quartz.kCGPatternTilingConstantSpacingMinimalDistortion, 1)
        self.assertEqual(Quartz.kCGPatternTilingConstantSpacing, 2)

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGPatternGetTypeID(), int)

        myInfo = object()
        cnt = [0]

        def drawPattern(info, context):
            self.assertTrue(info is myInfo)
            self.assertIsInstance(context, Quartz.CGContextRef)
            cnt[0] += 1

        pattern = Quartz.CGPatternCreate(
            myInfo,
            Quartz.CGRectMake(0, 0, 10, 10),
            Quartz.CGAffineTransformIdentity,
            10.0,
            10.0,
            Quartz.kCGPatternTilingConstantSpacing,
            True,
            drawPattern,
        )
        self.assertIsInstance(pattern, Quartz.CGPatternRef)

        v = Quartz.CGPatternRetain(pattern)
        self.assertTrue(v is pattern)
        Quartz.CGPatternRelease(pattern)

        url = Quartz.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", Quartz.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, Quartz.CFURLRef)
        context = Quartz.CGPDFContextCreateWithURL(url, ((0, 0), (1000, 1000)), None)
        self.assertIsInstance(context, Quartz.CGContextRef)
        Quartz.CGContextBeginPage(context, objc.NULL)
        try:
            color = Quartz.CGColorCreateWithPattern(
                Quartz.CGColorSpaceCreatePattern(None), pattern, (0.5, 0.5, 0.5, 0.5)
            )
            self.assertIsInstance(color, Quartz.CGColorRef)

            v = Quartz.CGColorGetPattern(color)
            self.assertTrue(v is pattern)

            # Now draw something with the pattern color to ensure that the callback
            # is actually called at least once.
            Quartz.CGContextSetFillColorWithColor(context, color)
            Quartz.CGContextSetStrokeColorWithColor(context, color)
            Quartz.CGContextFillRect(context, ((0, 0), (50, 50)))

        finally:
            Quartz.CGContextEndPage(context)
            if hasattr(Quartz, "CGPDFContextClose"):
                Quartz.CGPDFContextClose(context)
            if os.path.exists("/tmp/pyobjc.test.pdf"):
                os.unlink("/tmp/pyobjc.test.pdf")

        self.assertNotEqual(cnt[0], 0)
