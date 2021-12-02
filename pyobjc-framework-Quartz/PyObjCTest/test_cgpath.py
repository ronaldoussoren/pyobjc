from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCGPath(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CGPathRef)
        self.assertFalse(hasattr(Quartz, "CGMutablePathRef"))

    def testFunctions(self):
        self.assertIsInstance(Quartz.CGPathGetTypeID(), int)

        self.assertResultIsCFRetained(Quartz.CGPathCreateMutable)
        path = Quartz.CGPathCreateMutable()
        self.assertIsInstance(path, Quartz.CGPathRef)

        path = Quartz.CGPathCreateWithRect(
            Quartz.CGRectMake(1, 2, 3, 4), Quartz.CGAffineTransformIdentity
        )
        self.assertIsInstance(path, Quartz.CGPathRef)

        self.assertResultIsCFRetained(Quartz.CGPathCreateCopy)
        v = Quartz.CGPathCreateCopy(path)
        self.assertIsInstance(v, Quartz.CGPathRef)

        self.assertResultIsCFRetained(Quartz.CGPathCreateMutableCopy)
        v = Quartz.CGPathCreateMutableCopy(path)
        self.assertIsInstance(v, Quartz.CGPathRef)

        v = Quartz.CGPathRetain(path)
        self.assertTrue(v is path)
        Quartz.CGPathRelease(path)

        self.assertResultHasType(Quartz.CGPathEqualToPath, objc._C_BOOL)
        v = Quartz.CGPathEqualToPath(path, path)
        self.assertTrue(v is True)

        transform = Quartz.CGAffineTransformIdentity
        self.assertArgIsIn(Quartz.CGPathMoveToPoint, 1)
        Quartz.CGPathMoveToPoint(path, transform, 10, 30)

        self.assertArgIsIn(Quartz.CGPathAddLineToPoint, 1)
        Quartz.CGPathAddLineToPoint(path, transform, 10, 30)

        self.assertArgIsIn(Quartz.CGPathAddQuadCurveToPoint, 1)
        Quartz.CGPathAddQuadCurveToPoint(path, transform, 10, 30, 90, 90)

        self.assertArgIsIn(Quartz.CGPathAddCurveToPoint, 1)
        Quartz.CGPathAddCurveToPoint(path, transform, 10, 30, 90, 90, 140, 140)

        Quartz.CGPathCloseSubpath(path)

        self.assertArgIsIn(Quartz.CGPathAddRect, 1)
        Quartz.CGPathAddRect(path, transform, Quartz.CGRectMake(50, 60, 90, 10))

        self.assertArgIsIn(Quartz.CGPathAddRects, 1)
        self.assertArgIsIn(Quartz.CGPathAddRects, 2)
        Quartz.CGPathAddRects(
            path,
            transform,
            [Quartz.CGRectMake(50, 60, 90, 10), Quartz.CGRectMake(90, 50, 10, 10)],
            2,
        )
        self.assertRaises(
            ValueError,
            Quartz.CGPathAddRects,
            path,
            transform,
            [Quartz.CGRectMake(50, 60, 90, 10), Quartz.CGRectMake(90, 50, 10, 10)],
            3,
        )

        self.assertArgIsIn(Quartz.CGPathAddLines, 1)
        self.assertArgIsIn(Quartz.CGPathAddLines, 2)
        Quartz.CGPathAddLines(
            path, transform, [Quartz.CGPoint(50, 60), Quartz.CGPoint(90, 50)], 2
        )
        self.assertRaises(
            ValueError,
            Quartz.CGPathAddLines,
            path,
            transform,
            [Quartz.CGPoint(50, 60), Quartz.CGPoint(90, 50)],
            3,
        )

        self.assertArgIsIn(Quartz.CGPathAddEllipseInRect, 1)
        Quartz.CGPathAddEllipseInRect(
            path, transform, Quartz.CGRectMake(50, 60, 20, 20)
        )

        self.assertArgIsIn(Quartz.CGPathAddArc, 1)
        self.assertArgHasType(Quartz.CGPathAddArc, 7, objc._C_BOOL)
        Quartz.CGPathAddArc(path, transform, 50, 60, 30, 2.0, 2.5, True)

        self.assertArgIsIn(Quartz.CGPathAddArcToPoint, 1)
        Quartz.CGPathAddArcToPoint(path, transform, 50, 60, 30, 30, 40)

        path2 = Quartz.CGPathCreateMutable()
        self.assertArgIsIn(Quartz.CGPathAddPath, 1)
        Quartz.CGPathAddPath(path, transform, path2)

        self.assertResultHasType(Quartz.CGPathIsEmpty, objc._C_BOOL)
        self.assertTrue(Quartz.CGPathIsEmpty(path2) is True)
        self.assertTrue(Quartz.CGPathIsEmpty(path) is False)

        self.assertResultHasType(Quartz.CGPathIsRect, objc._C_BOOL)
        v1, v2 = Quartz.CGPathIsRect(path, None)
        self.assertTrue(v1 is False)
        self.assertIsInstance(v2, Quartz.CGRect)

        v = Quartz.CGPathGetCurrentPoint(path)
        self.assertIsInstance(v, Quartz.CGPoint)
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)

        v = Quartz.CGPathGetBoundingBox(path)
        self.assertIsInstance(v, Quartz.CGRect)
        box = v

        self.assertResultHasType(Quartz.CGPathContainsPoint, objc._C_BOOL)
        self.assertArgHasType(Quartz.CGPathContainsPoint, 3, objc._C_BOOL)
        self.assertArgIsIn(Quartz.CGPathContainsPoint, 1)
        v = Quartz.CGPathContainsPoint(
            path,
            transform,
            (Quartz.CGRectGetMidX(box), Quartz.CGRectGetMidY(box)),
            True,
        )
        self.assertTrue(v is True or v is False)

        v = Quartz.CGPathContainsPoint(
            path, transform, (box.origin.x - 1, box.origin.y - 1), True
        )
        self.assertTrue(v is False)

        lst = [0]
        info = object()

        def applier(ctx, element):
            lst[0] += 1
            self.assertTrue(ctx is info)
            self.assertIsInstance(element, Quartz.CGPathElement)
            self.assertIsInstance(element.type, int)
            self.assertIsInstance(element.points, objc.varlist)
            self.assertIsInstance(element.points[0], Quartz.CGPoint)

        Quartz.CGPathApply(path, info, applier)
        self.assertNotEqual(lst[0], 0)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        path = Quartz.CGPathCreateMutable()
        self.assertIsInstance(path, Quartz.CGPathRef)

        transform = Quartz.CGAffineTransformIdentity
        Quartz.CGPathMoveToPoint(path, transform, 10, 30)
        Quartz.CGPathAddLineToPoint(path, transform, 10, 30)

        r = Quartz.CGPathGetPathBoundingBox(path)
        self.assertIsInstance(r, Quartz.CGRect)

    @min_os_level("10.7")
    def testFunctions10_7(self):
        path = Quartz.CGPathCreateMutable()
        self.assertIsInstance(path, Quartz.CGPathRef)

        transform = Quartz.CGAffineTransformIdentity
        Quartz.CGPathMoveToPoint(path, transform, 10, 30)
        Quartz.CGPathAddLineToPoint(path, transform, 10, 30)

        self.assertResultIsCFRetained(Quartz.CGPathCreateCopyByTransformingPath)
        path2 = Quartz.CGPathCreateCopyByTransformingPath(path, transform)
        self.assertIsInstance(path2, Quartz.CGPathRef)

        self.assertResultIsCFRetained(Quartz.CGPathCreateMutableCopyByTransformingPath)
        path3 = Quartz.CGPathCreateCopyByTransformingPath(path, transform)
        self.assertIsInstance(path3, Quartz.CGPathRef)

        self.assertResultIsCFRetained(Quartz.CGPathCreateWithEllipseInRect)
        path = Quartz.CGPathCreateWithEllipseInRect(
            Quartz.CGRect(Quartz.CGPoint(0, 0), Quartz.CGSize(10, 20)), transform
        )
        self.assertIsInstance(path, Quartz.CGPathRef)

        self.assertResultIsCFRetained(Quartz.CGPathCreateCopyByDashingPath)
        self.assertArgSizeInArg(Quartz.CGPathCreateCopyByDashingPath, 3, 4)
        path2 = Quartz.CGPathCreateCopyByDashingPath(
            path, transform, 2.5, [2.0, 3.0, 4.0], 3
        )
        self.assertIsInstance(path2, Quartz.CGPathRef)

        self.assertResultIsCFRetained(Quartz.CGPathCreateCopyByStrokingPath)
        path2 = Quartz.CGPathCreateCopyByStrokingPath(
            path, transform, 4, Quartz.kCGLineCapButt, Quartz.kCGLineJoinRound, 1.0
        )
        self.assertIsInstance(path2, Quartz.CGPathRef)

        path = Quartz.CGPathCreateMutable()
        self.assertIsInstance(path, Quartz.CGPathRef)

        transform = Quartz.CGAffineTransformIdentity
        Quartz.CGPathMoveToPoint(path, transform, 10, 30)
        Quartz.CGPathAddRelativeArc(path, transform, 80, 90, 22.5, 33.0, 5.0)

    @min_os_level("10.9")
    def testFunctions10_9(self):

        path = Quartz.CGPathCreateMutable()
        self.assertIsInstance(path, Quartz.CGPathRef)

        transform = Quartz.CGAffineTransformIdentity

        self.assertResultIsCFRetained(Quartz.CGPathCreateWithRoundedRect)
        v = Quartz.CGPathCreateWithRoundedRect(
            Quartz.CGRectMake(100, 200, 300, 400), 2, 4, transform
        )
        self.assertIsInstance(v, Quartz.CGPathRef)

        Quartz.CGPathAddRoundedRect(
            path, transform, Quartz.CGRectMake(100, 200, 300, 400), 2, 3
        )

    def testConstants(self):
        self.assertEqual(Quartz.kCGLineJoinMiter, 0)
        self.assertEqual(Quartz.kCGLineJoinRound, 1)
        self.assertEqual(Quartz.kCGLineJoinBevel, 2)

        self.assertEqual(Quartz.kCGLineCapButt, 0)
        self.assertEqual(Quartz.kCGLineCapRound, 1)
        self.assertEqual(Quartz.kCGLineCapSquare, 2)

        self.assertEqual(Quartz.kCGPathElementMoveToPoint, 0)
        self.assertEqual(Quartz.kCGPathElementAddLineToPoint, 1)
        self.assertEqual(Quartz.kCGPathElementAddQuadCurveToPoint, 2)
        self.assertEqual(Quartz.kCGPathElementAddCurveToPoint, 3)
        self.assertEqual(Quartz.kCGPathElementCloseSubpath, 4)

    def testStructs(self):
        v = Quartz.CGPathElement()
        self.assertTrue(hasattr(v, "type"))
        self.assertTrue(hasattr(v, "points"))
        self.assertPickleRoundTrips(v)
