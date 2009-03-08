
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *
from Quartz import CoreGraphics 

class TestCGPath (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CGPathRef)
        self.failIf(hasattr(CoreGraphics, 'CGMutablePathRef'))

    def testFunctions(self):
        self.failUnlessIsInstance(CGPathGetTypeID(), (int, long))

        self.failUnlessResultIsCFRetained(CGPathCreateMutable)
        path = CGPathCreateMutable()
        self.failUnlessIsInstance(path, CGPathRef)

        self.failUnlessResultIsCFRetained(CGPathCreateCopy)
        v = CGPathCreateCopy(path)
        self.failUnlessIsInstance(v, CGPathRef)

        self.failUnlessResultIsCFRetained(CGPathCreateMutableCopy)
        v = CGPathCreateMutableCopy(path)
        self.failUnlessIsInstance(v, CGPathRef)

        v = CGPathRetain(path)
        self.failUnless(v is path)
        CGPathRelease(path)

        self.failUnlessResultHasType(CGPathEqualToPath, objc._C_BOOL)
        v = CGPathEqualToPath(path, path)
        self.failUnless(v is True)

        transform = CGAffineTransformIdentity
        self.failUnlessArgIsIn(CGPathMoveToPoint, 1)
        CGPathMoveToPoint(path, transform, 10, 30)

        self.failUnlessArgIsIn(CGPathAddLineToPoint, 1)
        CGPathAddLineToPoint(path, transform, 10, 30)

        self.failUnlessArgIsIn(CGPathAddQuadCurveToPoint, 1)
        CGPathAddQuadCurveToPoint(path, transform, 10, 30, 90, 90)

        self.failUnlessArgIsIn(CGPathAddCurveToPoint, 1)
        CGPathAddCurveToPoint(path, transform, 10, 30, 90, 90, 140, 140)

        CGPathCloseSubpath(path)

        self.failUnlessArgIsIn(CGPathAddRect, 1)
        CGPathAddRect(path, transform, CGRectMake(50, 60, 90, 10))

        self.failUnlessArgIsIn(CGPathAddRects, 1)
        self.failUnlessArgIsIn(CGPathAddRects, 2)
        CGPathAddRects(path, transform, [ CGRectMake(50, 60, 90, 10), CGRectMake(90, 50, 10, 10)], 2)
        self.failUnlessRaises(ValueError, CGPathAddRects, path, transform, [ CGRectMake(50, 60, 90, 10), CGRectMake(90, 50, 10, 10)], 3)


        self.failUnlessArgIsIn(CGPathAddLines, 1)
        self.failUnlessArgIsIn(CGPathAddLines, 2)
        CGPathAddLines(path, transform, [ CGPoint(50, 60), CGPoint(90, 50)], 2)
        self.failUnlessRaises(ValueError, CGPathAddLines, path, transform, [ CGPoint(50, 60), CGPoint(90, 50)], 3)

        self.failUnlessArgIsIn(CGPathAddEllipseInRect, 1)
        CGPathAddEllipseInRect(path, transform, CGRectMake(50, 60, 20, 20))

        self.failUnlessArgIsIn(CGPathAddArc, 1)
        self.failUnlessArgHasType(CGPathAddArc, 7, objc._C_BOOL)
        CGPathAddArc(path, transform, 50, 60, 30, 2.0, 2.5, True)

        self.failUnlessArgIsIn(CGPathAddArcToPoint, 1)
        CGPathAddArcToPoint(path, transform, 50, 60, 30, 30, 40)

        path2 = CGPathCreateMutable()
        self.failUnlessArgIsIn(CGPathAddPath, 1)
        CGPathAddPath(path, transform, path2)

        self.failUnlessResultHasType(CGPathIsEmpty, objc._C_BOOL)
        self.failUnless(CGPathIsEmpty(path2) is True)
        self.failUnless(CGPathIsEmpty(path) is False)

        self.failUnlessResultHasType(CGPathIsRect, objc._C_BOOL)
        v1, v2 = CGPathIsRect(path, None)
        self.failUnless(v1 is False)
        self.failUnlessIsInstance(v2, CGRect)

        v = CGPathGetCurrentPoint(path)
        self.failUnlessIsInstance(v, CGPoint)
        self.failUnlessIsInstance(v.x, float)
        self.failUnlessIsInstance(v.y, float)

        v = CGPathGetBoundingBox(path)
        self.failUnlessIsInstance(v, CGRect)
        box = v

        self.failUnlessResultHasType(CGPathContainsPoint, objc._C_BOOL)
        self.failUnlessArgHasType(CGPathContainsPoint, 3, objc._C_BOOL)
        self.failUnlessArgIsIn(CGPathContainsPoint, 1)
        v = CGPathContainsPoint(path, transform, (
            CGRectGetMidX(box),
            CGRectGetMidY(box)), True)
        self.failUnless(v is True)

        v = CGPathContainsPoint(path, transform, (
            box.origin.x - 1,
            box.origin.y - 1), True)
        self.failUnless(v is False)



        l = [0]
        info = object()
        def applier(ctx, element):
            l[0] += 1
            self.failUnless(ctx is info)
            self.failUnlessIsInstance(element, CGPathElement)
            self.failUnlessIsInstance(element.type, (int, long))
            self.failUnlessIsInstance(element.points, objc.varlist)
            self.failUnlessIsInstance(element.points[0], CGPoint)

        CGPathApply(path, info, applier)
        self.failIfEqual(l[0], 0)




    def testConstants(self):
        self.failUnlessEqual(kCGPathElementMoveToPoint, 0)
        self.failUnlessEqual(kCGPathElementAddLineToPoint, 1)
        self.failUnlessEqual(kCGPathElementAddQuadCurveToPoint, 2)
        self.failUnlessEqual(kCGPathElementAddCurveToPoint, 3)
        self.failUnlessEqual(kCGPathElementCloseSubpath, 4)

    def testStructs(self):
        v = CGPathElement()
        self.failUnless(hasattr(CGPathElement, 'type'))
        self.failUnless(hasattr(CGPathElement, 'points'))




if __name__ == "__main__":
    main()
