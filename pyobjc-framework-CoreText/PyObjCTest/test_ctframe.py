import os

import CoreText
import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCTFrame(TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreText.CTFrameRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(CoreText.kCTFrameProgressionTopToBottom, 0)
        self.assertEqual(CoreText.kCTFrameProgressionRightToLeft, 1)
        self.assertEqual(CoreText.kCTFrameProgressionLeftToRight, 2)

        self.assertEqual(CoreText.kCTFramePathFillEvenOdd, 0)
        self.assertEqual(CoreText.kCTFramePathFillWindingNumber, 1)

        self.assertIsInstance(CoreText.kCTFrameProgressionAttributeName, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CoreText.kCTFramePathFillRuleAttributeName, str)
        self.assertIsInstance(CoreText.kCTFramePathWidthAttributeName, str)
        self.assertIsInstance(CoreText.kCTFrameClippingPathsAttributeName, str)
        self.assertIsInstance(CoreText.kCTFramePathClippingPathAttributeName, str)

    def testFunctions(self):
        v = CoreText.CTFrameGetTypeID()
        self.assertIsInstance(v, int)

        setter = CoreText.CTFramesetterCreateWithAttributedString(
            CoreText.CFAttributedStringCreate(None, "hello", None)
        )
        self.assertIsInstance(setter, CoreText.CTFramesetterRef)

        path = CoreText.CGPathCreateMutable()
        self.assertIsInstance(path, CoreText.CGPathRef)
        CoreText.CGPathAddRect(
            path,
            None,
            CoreText.CGRect(CoreText.CGPoint(0, 0), CoreText.CGSize(400, 400)),
        )
        attr = {"foo": 42}
        frame = CoreText.CTFramesetterCreateFrame(
            setter, CoreText.CFRange(0, 5), path, attr
        )
        self.assertIsInstance(frame, CoreText.CTFrameRef)

        v = CoreText.CTFrameGetStringRange(frame)
        self.assertIsInstance(v, CoreText.CFRange)

        v = CoreText.CTFrameGetVisibleStringRange(frame)
        self.assertIsInstance(v, CoreText.CFRange)

        self.assertResultIsNotCFRetained(CoreText.CTFrameGetPath)
        v = CoreText.CTFrameGetPath(frame)
        self.assertIsInstance(v, CoreText.CGPathRef)

        v = CoreText.CTFrameGetFrameAttributes(frame)
        self.assertTrue(v is attr)

        v = CoreText.CTFrameGetLines(frame)
        self.assertIsInstance(v, CoreText.CFArrayRef)

        self.assertArgIsOut(CoreText.CTFrameGetLineOrigins, 2)
        self.assertArgSizeInArg(CoreText.CTFrameGetLineOrigins, 2, 1)
        v = CoreText.CTFrameGetLineOrigins(frame, CoreText.CFRange(0, 1), None)
        self.assertIsInstance(v, tuple)
        self.assertEqual(len(v), 1)
        self.assertIsInstance(v[0], CoreText.CGPoint)

        url = CoreText.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", CoreText.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, CoreText.CFURLRef)
        ctx = Quartz.CGPDFContextCreateWithURL(
            url, Quartz.CGRect(CoreText.CGPoint(0, 0), Quartz.CGSize(1000, 1000)), None
        )
        self.assertIsInstance(ctx, Quartz.CGContextRef)

        CoreText.CTFrameDraw(frame, ctx)

        if os.path.exists("/tmp/pyobjc.test.pdf"):
            os.unlink("/tmp/pyobjc.test.pdf")
