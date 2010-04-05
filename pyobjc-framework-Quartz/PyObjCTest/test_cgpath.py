
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Quartz import CoreGraphics 

class TestCGPath (TestCase):
    def testTypes(self):
        self.assertIsCFType(CGPathRef)
        self.failIf(hasattr(CoreGraphics, 'CGMutablePathRef'))

    def testFunctions(self):
        self.assertIsInstance(CGPathGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CGPathCreateMutable)
        path = CGPathCreateMutable()
        self.assertIsInstance(path, CGPathRef)

        self.assertResultIsCFRetained(CGPathCreateCopy)
        v = CGPathCreateCopy(path)
        self.assertIsInstance(v, CGPathRef)

        self.assertResultIsCFRetained(CGPathCreateMutableCopy)
        v = CGPathCreateMutableCopy(path)
        self.assertIsInstance(v, CGPathRef)

        v = CGPathRetain(path)
        self.assertTrue(v is path)
        CGPathRelease(path)

        self.assertResultHasType(CGPathEqualToPath, objc._C_BOOL)
        v = CGPathEqualToPath(path, path)
        self.assertTrue(v is True)

        transform = CGAffineTransformIdentity
        self.assertArgIsIn(CGPathMoveToPoint, 1)
        CGPathMoveToPoint(path, transform, 10, 30)

        self.assertArgIsIn(CGPathAddLineToPoint, 1)
        CGPathAddLineToPoint(path, transform, 10, 30)

        self.assertArgIsIn(CGPathAddQuadCurveToPoint, 1)
        CGPathAddQuadCurveToPoint(path, transform, 10, 30, 90, 90)

        self.assertArgIsIn(CGPathAddCurveToPoint, 1)
        CGPathAddCurveToPoint(path, transform, 10, 30, 90, 90, 140, 140)

        CGPathCloseSubpath(path)

        self.assertArgIsIn(CGPathAddRect, 1)
        CGPathAddRect(path, transform, CGRectMake(50, 60, 90, 10))

        self.assertArgIsIn(CGPathAddRects, 1)
        self.assertArgIsIn(CGPathAddRects, 2)
        CGPathAddRects(path, transform, [ CGRectMake(50, 60, 90, 10), CGRectMake(90, 50, 10, 10)], 2)
        self.assertRaises(ValueError, CGPathAddRects, path, transform, [ CGRectMake(50, 60, 90, 10), CGRectMake(90, 50, 10, 10)], 3)


        self.assertArgIsIn(CGPathAddLines, 1)
        self.assertArgIsIn(CGPathAddLines, 2)
        CGPathAddLines(path, transform, [ CGPoint(50, 60), CGPoint(90, 50)], 2)
        self.assertRaises(ValueError, CGPathAddLines, path, transform, [ CGPoint(50, 60), CGPoint(90, 50)], 3)

        self.assertArgIsIn(CGPathAddEllipseInRect, 1)
        CGPathAddEllipseInRect(path, transform, CGRectMake(50, 60, 20, 20))

        self.assertArgIsIn(CGPathAddArc, 1)
        self.assertArgHasType(CGPathAddArc, 7, objc._C_BOOL)
        CGPathAddArc(path, transform, 50, 60, 30, 2.0, 2.5, True)

        self.assertArgIsIn(CGPathAddArcToPoint, 1)
        CGPathAddArcToPoint(path, transform, 50, 60, 30, 30, 40)

        path2 = CGPathCreateMutable()
        self.assertArgIsIn(CGPathAddPath, 1)
        CGPathAddPath(path, transform, path2)

        self.assertResultHasType(CGPathIsEmpty, objc._C_BOOL)
        self.assertTrue(CGPathIsEmpty(path2) is True)
        self.assertTrue(CGPathIsEmpty(path) is False)

        self.assertResultHasType(CGPathIsRect, objc._C_BOOL)
        v1, v2 = CGPathIsRect(path, None)
        self.assertTrue(v1 is False)
        self.assertIsInstance(v2, CGRect)

        v = CGPathGetCurrentPoint(path)
        self.assertIsInstance(v, CGPoint)
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)

        v = CGPathGetBoundingBox(path)
        self.assertIsInstance(v, CGRect)
        box = v

        self.assertResultHasType(CGPathContainsPoint, objc._C_BOOL)
        self.assertArgHasType(CGPathContainsPoint, 3, objc._C_BOOL)
        self.assertArgIsIn(CGPathContainsPoint, 1)
        v = CGPathContainsPoint(path, transform, (
            CGRectGetMidX(box),
            CGRectGetMidY(box)), True)
        self.assertTrue(v is True)

        v = CGPathContainsPoint(path, transform, (
            box.origin.x - 1,
            box.origin.y - 1), True)
        self.assertTrue(v is False)



        l = [0]
        info = object()
        def applier(ctx, element):
            l[0] += 1
            self.assertTrue(ctx is info)
            self.assertIsInstance(element, CGPathElement)
            self.assertIsInstance(element.type, (int, long))
            self.assertIsInstance(element.points, objc.varlist)
            self.assertIsInstance(element.points[0], CGPoint)

        CGPathApply(path, info, applier)
        self.failIfEqual(l[0], 0)




    def testConstants(self):
        self.assertEqual(kCGPathElementMoveToPoint, 0)
        self.assertEqual(kCGPathElementAddLineToPoint, 1)
        self.assertEqual(kCGPathElementAddQuadCurveToPoint, 2)
        self.assertEqual(kCGPathElementAddCurveToPoint, 3)
        self.assertEqual(kCGPathElementCloseSubpath, 4)

    def testStructs(self):
        v = CGPathElement()
        self.assertTrue(hasattr(CGPathElement, 'type'))
        self.assertTrue(hasattr(CGPathElement, 'points'))




if __name__ == "__main__":
    main()
