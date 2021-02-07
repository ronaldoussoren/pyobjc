import AppKit
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSGeometry(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSMinXEdge, 0)
        self.assertEqual(AppKit.NSMinYEdge, 1)
        self.assertEqual(AppKit.NSMaxXEdge, 2)
        self.assertEqual(AppKit.NSMaxYEdge, 3)

        self.assertEqual(AppKit.NSRectEdgeMinX, 0)
        self.assertEqual(AppKit.NSRectEdgeMinY, 1)
        self.assertEqual(AppKit.NSRectEdgeMaxX, 2)
        self.assertEqual(AppKit.NSRectEdgeMaxY, 3)

        self.assertEqual(AppKit.NSZeroPoint, AppKit.NSPoint())
        self.assertEqual(AppKit.NSZeroSize, AppKit.NSSize())
        self.assertEqual(AppKit.NSZeroRect, AppKit.NSRect())

    def testInlines(self):
        self.assertEqual(AppKit.NSMakePoint(1, 2), AppKit.NSPoint(1, 2))
        self.assertEqual(AppKit.NSMakeSize(4, 5), AppKit.NSSize(4, 5))
        self.assertEqual(
            AppKit.NSMakeRect(1, 2, 3, 4),
            AppKit.NSRect(AppKit.NSPoint(1, 2), AppKit.NSSize(3, 4)),
        )

        rect = AppKit.NSRect(AppKit.NSPoint(1, 2), AppKit.NSSize(4, 6))
        self.assertEqual(AppKit.NSMaxX(rect), 5)
        self.assertEqual(AppKit.NSMaxY(rect), 8)
        self.assertEqual(AppKit.NSMidX(rect), 3)
        self.assertEqual(AppKit.NSMidY(rect), 5)
        self.assertEqual(AppKit.NSMinX(rect), 1)
        self.assertEqual(AppKit.NSMinY(rect), 2)
        self.assertEqual(AppKit.NSWidth(rect), 4)
        self.assertEqual(AppKit.NSHeight(rect), 6)

        # Cannot test these here, need to be tested in the Quartz unittests
        self.assertHasAttr(Foundation, "NSRectFromCGRect")
        self.assertHasAttr(Foundation, "NSRectToCGRect")
        self.assertHasAttr(Foundation, "NSPointFromCGPoint")
        self.assertHasAttr(Foundation, "NSPointToCGPoint")
        self.assertHasAttr(Foundation, "NSSizeFromCGSize")
        self.assertHasAttr(Foundation, "NSSizeToCGSize")

    @min_os_level("10.8")
    def testInlines10_8(self):
        v = AppKit.NSEdgeInsetsMake(1, 2, 3, 4)
        self.assertIsInstance(v, AppKit.NSEdgeInsets)
        self.assertEqual(v.top, 1.0)
        self.assertEqual(v.left, 2.0)
        self.assertEqual(v.bottom, 3.0)
        self.assertEqual(v.right, 4.0)

    def testFunctions(self):
        p1 = AppKit.NSPoint(1, 2)
        p2 = AppKit.NSPoint(3, 4)

        s1 = AppKit.NSSize(4, 5)
        s2 = AppKit.NSSize(7, 8)

        r0 = AppKit.NSRect(AppKit.NSPoint(9, 10), AppKit.NSSize(0, 0))
        r1 = AppKit.NSRect(AppKit.NSPoint(0, 1), AppKit.NSSize(4, 5))
        r2 = AppKit.NSRect(AppKit.NSPoint(4.5, 5.5), AppKit.NSSize(7.5, 8.5))

        self.assertIs(AppKit.NSEqualPoints(p1, p1), True)
        self.assertIs(AppKit.NSEqualPoints(p1, p2), False)
        self.assertIs(AppKit.NSEqualSizes(s1, s1), True)
        self.assertIs(AppKit.NSEqualSizes(s1, s2), False)
        self.assertIs(AppKit.NSEqualRects(r1, r1), True)
        self.assertIs(AppKit.NSEqualRects(r1, r2), False)
        self.assertIs(AppKit.NSIsEmptyRect(r0), True)
        self.assertIs(AppKit.NSIsEmptyRect(r1), False)
        ra = AppKit.NSInsetRect(r1, 2, 3)
        self.assertEqual(ra, AppKit.NSRect(AppKit.NSPoint(2, 4), AppKit.NSSize(0, -1)))

        ra = AppKit.NSIntegralRect(r2)
        self.assertEqual(ra, AppKit.NSRect(AppKit.NSPoint(4, 5), AppKit.NSSize(8, 9)))

        ra = AppKit.NSUnionRect(r1, r2)
        self.assertEqual(ra, AppKit.NSRect(AppKit.NSPoint(0, 1), AppKit.NSSize(12, 13)))

        ra = AppKit.NSIntersectionRect(r1, r2)
        self.assertEqual(ra, AppKit.NSRect(AppKit.NSPoint(0, 0), AppKit.NSSize(0, 0)))

        ra = AppKit.NSOffsetRect(r1, 5, 6)
        self.assertEqual(ra, AppKit.NSRect(AppKit.NSPoint(5, 7), AppKit.NSSize(4, 5)))

        slice_value, rem = AppKit.NSDivideRect(r2, None, None, 1.5, AppKit.NSMaxYEdge)
        self.assertEqual(
            slice_value,
            AppKit.NSRect(AppKit.NSPoint(4.5, 12.5), AppKit.NSSize(7.5, 1.5)),
        )
        self.assertEqual(
            rem, AppKit.NSRect(AppKit.NSPoint(4.5, 5.5), AppKit.NSSize(7.5, 7.0))
        )

        self.assertIs(AppKit.NSPointInRect(p1, r1), True)
        self.assertIs(AppKit.NSMouseInRect(p1, r1, False), True)
        self.assertIs(AppKit.NSMouseInRect(p2, r2, True), False)
        self.assertIs(AppKit.NSContainsRect(r1, r2), False)
        self.assertIs(AppKit.NSIntersectsRect(r1, r2), False)
        self.assertEqual(AppKit.NSStringFromPoint(p1), "{1, 2}")
        self.assertEqual(AppKit.NSStringFromSize(s1), "{4, 5}")
        self.assertEqual(AppKit.NSStringFromRect(r1), "{{0, 1}, {4, 5}}")
        v = AppKit.NSPointFromString("{1, 2}")
        self.assertEqual(v, p1)
        v = AppKit.NSSizeFromString("{4,5}")
        self.assertEqual(v, s1)
        v = AppKit.NSRectFromString("{   {0,1}  , {  4, 5}}")
        self.assertEqual(v, r1)

    def testValueMethods(self):
        v = AppKit.NSValue.valueWithPoint_(AppKit.NSPoint(2, 3))
        w = v.pointValue()
        self.assertIsInstance(w, AppKit.NSPoint)
        self.assertEqual(w, (2, 3))

        w = v.sizeValue()
        self.assertIsInstance(w, AppKit.NSSize)
        self.assertEqual(w, (2, 3))

        v = AppKit.NSValue.valueWithSize_(AppKit.NSSize(9, 8))
        w = v.sizeValue()
        self.assertIsInstance(w, AppKit.NSSize)
        self.assertEqual(w, (9, 8))

        v = AppKit.NSValue.valueWithRect_(
            AppKit.NSRect(AppKit.NSPoint(9, 10), AppKit.NSSize(11, 12))
        )
        w = v.rectValue()
        self.assertIsInstance(w, AppKit.NSRect)
        self.assertEqual(w, ((9, 10), (11, 12)))

        self.assertArgHasType(
            AppKit.NSValue.valueWithPoint_, 0, AppKit.NSPoint.__typestr__
        )
        self.assertResultHasType(AppKit.NSValue.pointValue, AppKit.NSPoint.__typestr__)
        self.assertArgHasType(
            AppKit.NSValue.valueWithSize_, 0, AppKit.NSSize.__typestr__
        )
        self.assertResultHasType(AppKit.NSValue.sizeValue, AppKit.NSSize.__typestr__)
        self.assertArgHasType(
            AppKit.NSValue.valueWithRect_, 0, AppKit.NSRect.__typestr__
        )
        self.assertResultHasType(AppKit.NSValue.rectValue, AppKit.NSRect.__typestr__)

    def testCoderMethods(self):
        self.assertArgHasType(
            AppKit.NSCoder.encodePoint_, 0, AppKit.NSPoint.__typestr__
        )
        self.assertResultHasType(AppKit.NSCoder.decodePoint, AppKit.NSPoint.__typestr__)
        self.assertArgHasType(
            AppKit.NSCoder.encodePoint_forKey_, 0, AppKit.NSPoint.__typestr__
        )
        self.assertResultHasType(
            AppKit.NSCoder.decodePointForKey_, AppKit.NSPoint.__typestr__
        )

        self.assertArgHasType(AppKit.NSCoder.encodeSize_, 0, AppKit.NSSize.__typestr__)
        self.assertResultHasType(AppKit.NSCoder.decodeSize, AppKit.NSSize.__typestr__)
        self.assertArgHasType(
            AppKit.NSCoder.encodeSize_forKey_, 0, AppKit.NSSize.__typestr__
        )
        self.assertResultHasType(
            AppKit.NSCoder.decodeSizeForKey_, AppKit.NSSize.__typestr__
        )

        self.assertArgHasType(AppKit.NSCoder.encodeRect_, 0, AppKit.NSRect.__typestr__)
        self.assertResultHasType(AppKit.NSCoder.decodeRect, AppKit.NSRect.__typestr__)
        self.assertArgHasType(
            AppKit.NSCoder.encodeRect_forKey_, 0, AppKit.NSRect.__typestr__
        )
        self.assertResultHasType(
            AppKit.NSCoder.decodeRectForKey_, AppKit.NSRect.__typestr__
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AppKit.NSEdgeInsetsZero, AppKit.NSEdgeInsets)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSAlignMinXInward, 1 << 0)
        self.assertEqual(AppKit.NSAlignMinYInward, 1 << 1)
        self.assertEqual(AppKit.NSAlignMaxXInward, 1 << 2)
        self.assertEqual(AppKit.NSAlignMaxYInward, 1 << 3)
        self.assertEqual(AppKit.NSAlignWidthInward, 1 << 4)
        self.assertEqual(AppKit.NSAlignHeightInward, 1 << 5)
        self.assertEqual(AppKit.NSAlignMinXOutward, 1 << 8)
        self.assertEqual(AppKit.NSAlignMinYOutward, 1 << 9)
        self.assertEqual(AppKit.NSAlignMaxXOutward, 1 << 10)
        self.assertEqual(AppKit.NSAlignMaxYOutward, 1 << 11)
        self.assertEqual(AppKit.NSAlignWidthOutward, 1 << 12)
        self.assertEqual(AppKit.NSAlignHeightOutward, 1 << 13)
        self.assertEqual(AppKit.NSAlignMinXNearest, 1 << 16)
        self.assertEqual(AppKit.NSAlignMinYNearest, 1 << 17)
        self.assertEqual(AppKit.NSAlignMaxXNearest, 1 << 18)
        self.assertEqual(AppKit.NSAlignMaxYNearest, 1 << 19)
        self.assertEqual(AppKit.NSAlignWidthNearest, 1 << 20)
        self.assertEqual(AppKit.NSAlignHeightNearest, 1 << 21)
        self.assertEqual(AppKit.NSAlignRectFlipped, 1 << 63)
        self.assertEqual(
            AppKit.NSAlignAllEdgesInward,
            AppKit.NSAlignMinXInward
            | AppKit.NSAlignMaxXInward
            | AppKit.NSAlignMinYInward
            | AppKit.NSAlignMaxYInward,
        )
        self.assertEqual(
            AppKit.NSAlignAllEdgesOutward,
            AppKit.NSAlignMinXOutward
            | AppKit.NSAlignMaxXOutward
            | AppKit.NSAlignMinYOutward
            | AppKit.NSAlignMaxYOutward,
        )
        self.assertEqual(
            AppKit.NSAlignAllEdgesNearest,
            AppKit.NSAlignMinXNearest
            | AppKit.NSAlignMaxXNearest
            | AppKit.NSAlignMinYNearest
            | AppKit.NSAlignMaxYNearest,
        )

    @min_os_level("10.7")
    def testFunctions10_7(self):
        r2 = AppKit.NSRect(AppKit.NSPoint(4.5, 5.5), AppKit.NSSize(7.5, 8.5))
        r = AppKit.NSIntegralRectWithOptions(r2, AppKit.NSAlignAllEdgesNearest)
        self.assertIsInstance(r, AppKit.NSRect)

    @min_os_level("10.10")
    def testFunctions10_10(self):
        self.assertResultIsBOOL(AppKit.NSEdgeInsetsEqual)
