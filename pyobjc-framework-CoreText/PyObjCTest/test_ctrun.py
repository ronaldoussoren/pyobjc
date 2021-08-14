import CoreText
from Foundation import NSDictionary
from PyObjCTools.TestSupport import TestCase, min_os_level
from Quartz import CGPDFContextCreateWithURL, CGRect, CGPoint, CGSize
import objc


class TestCTRun(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreText.CTRunRef)

    def testConstants(self):
        self.assertEqual(CoreText.kCTRunStatusNoStatus, 0)
        self.assertEqual(CoreText.kCTRunStatusRightToLeft, (1 << 0))
        self.assertEqual(CoreText.kCTRunStatusNonMonotonic, (1 << 1))
        self.assertEqual(CoreText.kCTRunStatusHasNonIdentityMatrix, (1 << 2))

    def testFunctions(self):
        self.assertIsInstance(CoreText.CTRunGetTypeID(), int)

        line = CoreText.CTLineCreateWithAttributedString(
            CoreText.CFAttributedStringCreate(None, "hello world", None)
        )
        self.assertIsInstance(line, CoreText.CTLineRef)

        run = CoreText.CTLineGetGlyphRuns(line)[0]
        self.assertIsInstance(run, CoreText.CTRunRef)

        v = CoreText.CTRunGetGlyphCount(run)
        self.assertIsInstance(v, int)

        v = CoreText.CTRunGetAttributes(run)
        self.assertIsInstance(v, (dict, NSDictionary))

        v = CoreText.CTRunGetStatus(run)
        self.assertIsInstance(v, int)

        buf = CoreText.CTRunGetGlyphsPtr(run)
        self.assertIsInstance(buf, objc.varlist)
        self.assertIsInstance(buf[0], int)

        buf = CoreText.CTRunGetGlyphs(run, CoreText.CFRange(0, 5), None)
        self.assertIsInstance(buf, tuple)
        self.assertEqual(len(buf), 5)
        self.assertIsInstance(buf[0], int)

        buf = CoreText.CTRunGetPositionsPtr(run)
        self.assertIsInstance(buf, objc.varlist)
        self.assertIsInstance(buf[0], CGPoint)

        buf = CoreText.CTRunGetPositions(run, CoreText.CFRange(0, 5), None)
        self.assertIsInstance(buf, tuple)
        self.assertEqual(len(buf), 5)
        self.assertIsInstance(buf[0], CGPoint)

        buf = CoreText.CTRunGetStringIndicesPtr(run)
        self.assertIsInstance(buf, objc.varlist)
        self.assertIsInstance(buf[0], int)

        buf = CoreText.CTRunGetStringIndices(run, CoreText.CFRange(0, 5), None)
        self.assertIsInstance(buf, tuple)
        self.assertEqual(len(buf), 5)
        self.assertIsInstance(buf[0], int)

        v = CoreText.CTRunGetStringRange(run)
        self.assertIsInstance(v, CoreText.CFRange)

        v = CoreText.CTRunGetTypographicBounds(
            run, CoreText.CFRange(0, 5), None, None, None
        )
        self.assertIsInstance(v, tuple)
        self.assertEqual(len(v), 4)
        self.assertIsInstance(v[0], float)
        self.assertIsInstance(v[1], float)
        self.assertIsInstance(v[2], float)
        self.assertIsInstance(v[3], float)

        url = CoreText.CFURLCreateWithFileSystemPath(
            None, "/tmp/pyobjc.test.pdf", CoreText.kCFURLPOSIXPathStyle, False
        )
        self.assertIsInstance(url, CoreText.CFURLRef)

        ctx = CGPDFContextCreateWithURL(
            url, CGRect(CGPoint(0, 0), CGSize(1000, 1000)), None
        )
        v = CoreText.CTRunGetImageBounds(run, ctx, CoreText.CFRange(0, 5))
        self.assertIsInstance(v, CGRect)

        v = CoreText.CTRunGetTextMatrix(run)
        self.assertIsInstance(v, CoreText.CGAffineTransform)

        v = CoreText.CTRunDraw(run, ctx, CoreText.CFRange(0, 5))
        self.assertTrue(v is None)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        self.assertArgIsOut(CoreText.CTRunGetAdvances, 2)
        self.assertArgSizeInArg(CoreText.CTRunGetAdvances, 2, 1)

        line = CoreText.CTLineCreateWithAttributedString(
            CoreText.CFAttributedStringCreate(None, "hello world", None)
        )
        self.assertIsInstance(line, CoreText.CTLineRef)

        run = CoreText.CTLineGetGlyphRuns(line)[0]
        self.assertIsInstance(run, CoreText.CTRunRef)

        r = CoreText.CTRunGetAdvances(run, CoreText.CFRange(1, 3), None)
        self.assertIsInstance(r, (list, tuple))
        self.assertEqual(len(r), 3)
        for i in range(3):
            self.assertIsInstance(r[i], CGSize)

        v = CoreText.CTRunGetAdvancesPtr(run)
        if v is not objc.NULL:
            self.assertIsInstance(v, objc.varlist)
            self.assertIsInstance(v[0], CGSize)

    @min_os_level("10.11")
    def testFunctions10_11(self):
        self.assertArgIsOut(CoreText.CTRunGetBaseAdvancesAndOrigins, 2)
        self.assertArgSizeInArg(CoreText.CTRunGetBaseAdvancesAndOrigins, 2, 1)
        self.assertArgIsOut(CoreText.CTRunGetBaseAdvancesAndOrigins, 3)
        self.assertArgSizeInArg(CoreText.CTRunGetBaseAdvancesAndOrigins, 3, 1)
