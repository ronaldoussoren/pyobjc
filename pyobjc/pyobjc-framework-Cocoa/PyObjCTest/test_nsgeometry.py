from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation


class TestNSGeometry (TestCase):
    def testConstants(self):
        self.assertEquals(NSMinXEdge, 0)
        self.assertEquals(NSMinYEdge, 1)
        self.assertEquals(NSMaxXEdge, 2)
        self.assertEquals(NSMaxYEdge, 3)

        self.assertEquals(NSZeroPoint, NSPoint())
        self.assertEquals(NSZeroSize, NSSize())
        self.assertEquals(NSZeroRect, NSRect())

    def testInlines(self):
        self.assertEquals(NSMakePoint(1, 2), NSPoint(1, 2))
        self.assertEquals(NSMakeSize(4, 5), NSSize(4, 5))
        self.assertEquals(NSMakeRect(1, 2, 3, 4), NSRect(NSPoint(1, 2), NSSize(3, 4)))

        rect = NSRect(NSPoint(1,2), NSSize(4,6))
        self.assertEquals(NSMaxX(rect), 5)
        self.assertEquals(NSMaxY(rect), 8)
        self.assertEquals(NSMidX(rect), 3)
        self.assertEquals(NSMidY(rect), 5)
        self.assertEquals(NSMinX(rect), 1)
        self.assertEquals(NSMinY(rect), 2)
        self.assertEquals(NSWidth(rect), 4)
        self.assertEquals(NSHeight(rect), 6)
       
        # Cannot test these here, need to be tested in the Quartz unittests
        self.failUnless(hasattr(Foundation, 'NSRectFromCGRect'))
        self.failUnless(hasattr(Foundation, 'NSRectToCGRect'))
        self.failUnless(hasattr(Foundation, 'NSPointFromCGPoint'))
        self.failUnless(hasattr(Foundation, 'NSPointToCGPoint'))
        self.failUnless(hasattr(Foundation, 'NSSizeFromCGSize'))
        self.failUnless(hasattr(Foundation, 'NSSizeToCGSize'))

    def testFunctions(self):
        p1 = NSPoint(1, 2)
        p2 = NSPoint(3, 4)
        
        s1 = NSSize(4, 5)
        s2 = NSSize(7, 8)

        r0 = NSRect(NSPoint(9, 10), NSSize(0, 0))
        r1 = NSRect(NSPoint(0, 1), NSSize(4, 5))
        r2 = NSRect(NSPoint(4.5, 5.5), NSSize(7.5, 8.5))



        self.failUnless(NSEqualPoints(p1, p1) is True)
        self.failUnless(NSEqualPoints(p1, p2) is False)

        self.failUnless(NSEqualSizes(s1, s1) is True)
        self.failUnless(NSEqualSizes(s1, s2) is False)

        self.failUnless(NSEqualRects(r1, r1) is True)
        self.failUnless(NSEqualRects(r1, r2) is False)

        self.failUnless(NSIsEmptyRect(r0) is True)
        self.failUnless(NSIsEmptyRect(r1) is False)

        ra = NSInsetRect(r1, 2, 3)
        self.assertEquals(ra, NSRect(NSPoint(2, 4), NSSize(0, -1)))

        ra = NSIntegralRect(r2)
        self.assertEquals(ra, NSRect(NSPoint(4, 5), NSSize(8, 9)))

        ra = NSUnionRect(r1, r2)
        self.assertEquals(ra, NSRect(NSPoint(0, 1), NSSize(12, 13)))

        ra = NSIntersectionRect(r1, r2)
        self.assertEquals(ra, NSRect(NSPoint(0, 0), NSSize(0, 0)))

        ra = NSOffsetRect(r1, 5, 6)
        self.assertEquals(ra, NSRect(NSPoint(5, 7), NSSize(4,5)))

        slice, rem = NSDivideRect(r2, None, None, 1.5, NSMaxYEdge)
        self.assertEquals(slice, NSRect(NSPoint(4.5, 12.5), NSSize(7.5, 1.5))) 
        self.assertEquals(rem, NSRect(NSPoint(4.5, 5.5), NSSize(7.5, 7.0)))

        self.failUnless(NSPointInRect(p1, r1) is True)
        self.failUnless(NSMouseInRect(p1, r1, False) is True)
        self.failUnless(NSMouseInRect(p2, r2, True) is False)

        self.failUnless(NSContainsRect(r1, r2) is False)
        self.failUnless(NSIntersectsRect(r1, r2) is False)

        self.assertEquals(NSStringFromPoint(p1), u'{1, 2}')
        self.assertEquals(NSStringFromSize(s1), u'{4, 5}')
        self.assertEquals(NSStringFromRect(r1),  u'{{0, 1}, {4, 5}}')
        v = NSPointFromString('{1, 2}')
        self.assertEquals(v, p1)
        v = NSSizeFromString('{4,5}')
        self.assertEquals(v, s1)
        v = NSRectFromString(u'{   {0,1}  , {  4, 5}}')
        self.assertEquals(v, r1)

    def testValueMethods(self):
        v = NSValue.valueWithPoint_(NSPoint(2, 3))
        w = v.pointValue()
        self.failUnless(isinstance(w, NSPoint))
        self.assertEquals(w, (2,3))

        w = v.sizeValue()
        self.failUnless(isinstance(w, NSSize))
        self.assertEquals(w, (2,3))

        v = NSValue.valueWithSize_(NSSize(9, 8))
        w = v.sizeValue()
        self.failUnless(isinstance(w, NSSize))
        self.assertEquals(w, (9,8))

        v = NSValue.valueWithRect_(NSRect(NSPoint(9, 10), NSSize(11, 12)))
        w = v.rectValue()
        self.failUnless(isinstance(w, NSRect))
        self.assertEquals(w, ((9,10),(11,12)))

        self.failUnlessArgHasType(NSValue.valueWithPoint_, 0, NSPoint.__typestr__)
        self.failUnlessResultHasType(NSValue.pointValue, NSPoint.__typestr__)
        self.failUnlessArgHasType(NSValue.valueWithSize_, 0, NSSize.__typestr__)
        self.failUnlessResultHasType(NSValue.sizeValue, NSSize.__typestr__)
        self.failUnlessArgHasType(NSValue.valueWithRect_, 0, NSRect.__typestr__)
        self.failUnlessResultHasType(NSValue.rectValue, NSRect.__typestr__)


    def testCoderMethods(self):
        self.failUnlessArgHasType(NSCoder.encodePoint_, 0, NSPoint.__typestr__)
        self.failUnlessResultHasType(NSCoder.decodePoint, NSPoint.__typestr__)
        self.failUnlessArgHasType(NSCoder.encodeSize_, 0, NSSize.__typestr__)
        self.failUnlessResultHasType(NSCoder.decodeSize, NSSize.__typestr__)
        self.failUnlessArgHasType(NSCoder.encodeRect_, 0, NSRect.__typestr__)
        self.failUnlessResultHasType(NSCoder.decodeRect, NSRect.__typestr__)


if __name__ == "__main__":
    main()
