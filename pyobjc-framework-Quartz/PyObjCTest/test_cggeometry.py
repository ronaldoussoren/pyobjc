
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGGeometry (TestCase):
    def testStruct(self):
        v = CGPoint()
        self.failUnlessIsInstance(v.x, float)
        self.failUnlessIsInstance(v.y, float)

        v = CGSize()
        self.failUnlessIsInstance(v.width, float)
        self.failUnlessIsInstance(v.height, float)

        v = CGRect()
        self.failUnlessIsInstance(v.origin, CGPoint)
        self.failUnlessIsInstance(v.size, CGSize)

    def testConstants(self):
        self.failUnlessEqual(CGRectMinXEdge, 0)
        self.failUnlessEqual(CGRectMinYEdge, 1)
        self.failUnlessEqual(CGRectMaxXEdge, 2)
        self.failUnlessEqual(CGRectMaxYEdge, 3)

        self.failUnlessIsInstance(CGPointZero, CGPoint)
        self.failUnlessEqual(CGPointZero.x, 0.0)
        self.failUnlessEqual(CGPointZero.y, 0.0)

        self.failUnlessIsInstance(CGSizeZero, CGSize)
        self.failUnlessEqual(CGSizeZero.width, 0.0)
        self.failUnlessEqual(CGSizeZero.height, 0.0)

        self.failUnlessIsInstance(CGRectZero, CGRect)
        self.failUnlessEqual(CGRectZero.origin, CGPointZero)
        self.failUnlessEqual(CGRectZero.size, CGSizeZero)

        self.failUnlessIsInstance(CGRectNull, CGRect)
        self.failUnlessIsInstance(CGRectInfinite, CGRect)

    def testFunctions(self):
        v = CGPointMake(2.5, 3.5)
        self.failUnlessIsInstance(v, CGPoint)
        self.failUnlessEqual(v.x, 2.5)
        self.failUnlessEqual(v.y, 3.5)

        v = CGSizeMake(2.5, 3.5)
        self.failUnlessIsInstance(v, CGSize)
        self.failUnlessEqual(v.width, 2.5)
        self.failUnlessEqual(v.height, 3.5)

        v = CGRectMake(2.5, 3.5, 15.5, 25.5)
        self.failUnlessIsInstance(v, CGRect)
        self.failUnlessEqual(v.origin.x, 2.5)
        self.failUnlessEqual(v.origin.y, 3.5)
        self.failUnlessEqual(v.size.width, 15.5)
        self.failUnlessEqual(v.size.height, 25.5)
        rect = v

        v = CGRectGetMinX(rect)
        self.failUnlessEqual(v, min(rect.origin.x, rect.origin.x + rect.size.width))
        v = CGRectGetMidX(rect)
        self.failUnlessEqual(v, rect.origin.x + (rect.size.width/2))

        v = CGRectGetMaxX(rect)
        self.failUnlessEqual(v, max(rect.origin.x, rect.origin.x + rect.size.width))

        v = CGRectGetMinY(rect)
        self.failUnlessEqual(v, min(rect.origin.y, rect.origin.y + rect.size.height))
        v = CGRectGetMidY(rect)
        self.failUnlessEqual(v, rect.origin.y + (rect.size.height/2))

        v = CGRectGetMaxY(rect)
        self.failUnlessEqual(v, max(rect.origin.y, rect.origin.y + rect.size.height))

        self.failUnlessEqual(CGRectGetWidth(rect), abs(rect.size.width))
        self.failUnlessEqual(CGRectGetHeight(rect), abs(rect.size.height))

        self.failUnlessResultHasType(CGPointEqualToPoint, objc._C_BOOL)
        self.failUnless(CGPointEqualToPoint((1, 1), (2, 2)) is False)
        self.failUnless(CGPointEqualToPoint((1, 1), (1, 1)) is True)

        self.failUnlessResultHasType(CGSizeEqualToSize, objc._C_BOOL)
        self.failUnless(CGSizeEqualToSize((1, 1), (2, 2)) is False)
        self.failUnless(CGSizeEqualToSize((1, 1), (1, 1)) is True)

        self.failUnlessResultHasType(CGRectEqualToRect, objc._C_BOOL)
        self.failUnless(CGRectEqualToRect(((1,1), (1,1)), ((2,2), (2,2))) is False)
        self.failUnless(CGRectEqualToRect(((1,1), (1,1)), ((1,1), (1,1))) is True)

        v = CGRectStandardize(((90, 90), (-4, -5)))
        self.failUnlessIsInstance(v, CGRect)
        self.failUnlessEqual(v, CGRectMake(86, 85, 4, 5))

        self.failUnlessResultHasType(CGRectIsEmpty, objc._C_BOOL)
        self.failUnless(CGRectIsEmpty(rect) is False)
        self.failUnless(CGRectIsEmpty(CGRectZero) is True)

        self.failUnlessResultHasType(CGRectIsNull, objc._C_BOOL)
        self.failUnless(CGRectIsNull(rect) is False)
        self.failUnless(CGRectIsNull(CGRectNull) is True)

        self.failUnlessResultHasType(CGRectIsInfinite, objc._C_BOOL)
        self.failUnless(CGRectIsInfinite(rect) is False)
        self.failUnless(CGRectIsInfinite(CGRectInfinite) is True)

        v = CGRectInset(rect, 2, 3)
        self.failUnlessIsInstance(v, CGRect)
        self.failUnlessEqual(v.origin.x, rect.origin.x + 2)
        self.failUnlessEqual(v.origin.y, rect.origin.y + 3)
        self.failUnlessEqual(v.size.width, rect.size.width - 4)
        self.failUnlessEqual(v.size.height, rect.size.height - 6)

        v = CGRectIntegral(CGRectMake(1.5, 2.5, 3.5, 4.5))
        self.failUnlessIsInstance(v, CGRect)
        self.failUnlessEqual(v, ((1, 2), (4, 5)))

        v = CGRectUnion(((1,1), (4,5)), ((99,5), (40, 40)))
        self.failUnlessIsInstance(v, CGRect)

        v = CGRectIntersection(((1,1), (4,5)), ((99,5), (40, 40)))
        self.failUnlessIsInstance(v, CGRect)

        r = CGRectOffset(rect, 9, -5)
        self.failUnlessIsInstance(v, CGRect)

        self.failUnlessArgIsOut(CGRectDivide, 1)
        self.failUnlessArgIsOut(CGRectDivide, 2)
        slice, remainder = CGRectDivide(rect, None, None, 10, CGRectMinYEdge)
        self.failUnlessIsInstance(slice, CGRect)
        self.failUnlessIsInstance(remainder, CGRect)

        self.failUnlessResultHasType(CGRectContainsPoint, objc._C_BOOL)
        self.failUnlessResultHasType(CGRectContainsRect, objc._C_BOOL)
        self.failUnlessResultHasType(CGRectIntersectsRect, objc._C_BOOL)
        self.failUnless(CGRectContainsPoint(rect, rect.origin) is True)
        self.failUnless(CGRectContainsRect(rect, rect) is True)
        self.failUnless(CGRectIntersectsRect(rect, rect) is True)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        d = CGPointCreateDictionaryRepresentation((10, 5))
        self.failUnlessIsInstance(d, CFDictionaryRef)

        ok, p = CGPointMakeWithDictionaryRepresentation(d, None)
        self.failUnless(ok is True)
        self.failUnlessIsInstance(p, CGPoint)
        self.failUnlessEqual(p.x, 10)
        self.failUnlessEqual(p.y, 5)

        d = CGSizeCreateDictionaryRepresentation((10, 5))
        self.failUnlessIsInstance(d, CFDictionaryRef)

        ok, p = CGSizeMakeWithDictionaryRepresentation(d, None)
        self.failUnless(ok is True)
        self.failUnlessIsInstance(p, CGSize)
        self.failUnlessEqual(p.width, 10)
        self.failUnlessEqual(p.height, 5)

        d = CGRectCreateDictionaryRepresentation(CGRectMake(0, 10, 20, 30))
        self.failUnlessIsInstance(d, CFDictionaryRef)

        ok, p = CGRectMakeWithDictionaryRepresentation(d, None)
        self.failUnless(ok is True)
        self.failUnlessIsInstance(p, CGRect)
        self.failUnlessEqual(p, CGRectMake(0, 10, 20, 30))



if __name__ == "__main__":
    main()
