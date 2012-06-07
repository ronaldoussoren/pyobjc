
from PyObjCTools.TestSupport import *
from CoreText import *
from Foundation import NSDictionary
from Quartz import *

try:
    long
except NameError:
    long = int

class TestCTRun (TestCase):
    def testTypes(self):
        self.assertIsCFType(CTRunRef)

    def testConstants(self):
        self.assertEqual(kCTRunStatusNoStatus, 0)
        self.assertEqual(kCTRunStatusRightToLeft, (1 << 0))
        self.assertEqual(kCTRunStatusNonMonotonic, (1 << 1))
        self.assertEqual(kCTRunStatusHasNonIdentityMatrix, (1 << 2))

    def testFunctions(self):
        self.assertIsInstance(CTRunGetTypeID(), (int, long))

        line = CTLineCreateWithAttributedString(
                CFAttributedStringCreate(None, b"hello world".decode('latin1'), None))
        self.assertIsInstance(line, CTLineRef)

        run = CTLineGetGlyphRuns(line)[0]
        self.assertIsInstance(run, CTRunRef)

        v = CTRunGetGlyphCount(run)
        self.assertIsInstance(v, (int, long))

        v = CTRunGetAttributes(run)
        self.assertIsInstance(v, (dict, NSDictionary))

        v = CTRunGetStatus(run)
        self.assertIsInstance(v, (int, long))

        buf = CTRunGetGlyphsPtr(run)
        self.assertIsInstance(buf, objc.varlist)
        self.assertIsInstance(buf[0], (int, long))

        buf = CTRunGetGlyphs(run, CFRange(0, 5), None)
        self.assertIsInstance(buf, tuple)
        self.assertEqual(len(buf), 5)
        self.assertIsInstance(buf[0], (int, long))

        buf = CTRunGetPositionsPtr(run)
        self.assertIsInstance(buf, objc.varlist)
        self.assertIsInstance(buf[0], CGPoint)

        buf = CTRunGetPositions(run, CFRange(0, 5), None)
        self.assertIsInstance(buf, tuple)
        self.assertEqual(len(buf), 5)
        self.assertIsInstance(buf[0], CGPoint)

        buf = CTRunGetStringIndicesPtr(run)
        self.assertIsInstance(buf, objc.varlist)
        self.assertIsInstance(buf[0], (int, long))

        buf = CTRunGetStringIndices(run, CFRange(0, 5), None)
        self.assertIsInstance(buf, tuple)
        self.assertEqual(len(buf), 5)
        self.assertIsInstance(buf[0], (int, long))

        v = CTRunGetStringRange(run)
        self.assertIsInstance(v, CFRange)

        v = CTRunGetTypographicBounds(run, CFRange(0, 5), None, None, None)
        self.assertIsInstance(v, tuple)
        self.assertEqual(len(v), 4)
        self.assertIsInstance(v[0], float)
        self.assertIsInstance(v[1], float)
        self.assertIsInstance(v[2], float)
        self.assertIsInstance(v[3], float)

        url = CFURLCreateWithFileSystemPath(None,
                                "/tmp/pyobjc.test.pdf", kCFURLPOSIXPathStyle, False)
        self.assertIsInstance(url, CFURLRef)

        ctx = CGPDFContextCreateWithURL(url, CGRect(CGPoint(0, 0), CGSize(1000, 1000)), None)
        v = CTRunGetImageBounds(run, ctx, CFRange(0, 5))
        self.assertIsInstance(v, CGRect)

        v = CTRunGetTextMatrix(run)
        self.assertIsInstance(v, CGAffineTransform)

        v = CTRunDraw(run, ctx, CFRange(0, 5))
        self.assertTrue(v is None)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        self.assertArgIsOut(CTRunGetAdvances, 2)
        self.assertArgSizeInArg(CTRunGetAdvances, 2, 1)

        line = CTLineCreateWithAttributedString(
                CFAttributedStringCreate(None, b"hello world".decode('latin1'), None))
        self.assertIsInstance(line, CTLineRef)

        run = CTLineGetGlyphRuns(line)[0]
        self.assertIsInstance(run, CTRunRef)

        r = CTRunGetAdvances(run, CFRange(1, 3), None)
        self.assertIsInstance(r, (list, tuple))
        self.assertEquals(len(r), 3)
        for i in range(3):
            self.assertIsInstance(r[i], CGSize)


        try:
            CTRunGetAdvancesPtr
        except NameError:
            pass
        else:
            self.fail("CTRunGetAdvancesPtr is defined")


if __name__ == "__main__":
    main()
