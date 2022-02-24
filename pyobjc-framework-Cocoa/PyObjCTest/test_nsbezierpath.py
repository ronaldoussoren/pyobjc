# Test special methods of AppKit.NSBezierPath
# TODO: Test implementing these in python.
import objc
import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSBezierPath(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSBezierPathElement)
        self.assertIsEnumType(AppKit.NSLineCapStyle)
        self.assertIsEnumType(AppKit.NSLineJoinStyle)
        self.assertIsEnumType(AppKit.NSWindingRule)

    def assertPointEquals(self, point1, point2):
        self.assertAlmostEqual(point1[0], point2[0])
        self.assertAlmostEqual(point1[1], point2[1])

    def test_creation(self):
        p = AppKit.NSBezierPath.bezierPath()
        self.assertIsNot(p, None)
        self.assertEqual(p.elementCount(), 0)

        p = AppKit.NSBezierPath.bezierPathWithOvalInRect_(((0, 0), (100, 50)))
        self.assertIsNot(p, None)
        self.assertEqual(p.elementCount(), 5)

    def test_appendPoints(self):
        p = AppKit.NSBezierPath.bezierPath()
        self.assertIsNot(p, None)
        self.assertEqual(p.elementCount(), 0)

        points = [(0, 0), (100, 0), (100, 100), (0, 0)]
        p.appendBezierPathWithPoints_count_(points, 3)
        self.assertEqual(p.elementCount(), 3)

    def test_setLineDash(self):
        p = AppKit.NSBezierPath.bezierPath()
        p.setLineDash_count_phase_((10, 10, 20, 5), 4, 45.0)

        pattern, count, phase = p.getLineDash_count_phase_(objc.NULL, 0, None)
        # self.assertEqual(pattern, None)
        self.assertEqual(pattern, objc.NULL)
        self.assertEqual(count, 4)
        self.assertAlmostEqual(phase, 45.0)

        pattern, count, phase = p.getLineDash_count_phase_(None, 4, None)
        self.assertAlmostEqual(pattern[0], 10)
        self.assertAlmostEqual(pattern[1], 10)
        self.assertAlmostEqual(pattern[2], 20)
        self.assertAlmostEqual(pattern[3], 5)
        self.assertEqual(count, 4)
        self.assertAlmostEqual(phase, 45.0)

    def test_elementAtIndex(self):
        p = AppKit.NSBezierPath.bezierPath()
        p.moveToPoint_((10, 10))
        p.lineToPoint_((20, 30))
        p.lineToPoint_((30, 20))
        p.curveToPoint_controlPoint1_controlPoint2_((40, 41), (10, 11), (20, 21))
        p.closePath()

        self.assertEqual(p.elementAtIndex_(0), AppKit.NSMoveToBezierPathElement)
        self.assertEqual(p.elementAtIndex_(1), AppKit.NSLineToBezierPathElement)
        self.assertEqual(p.elementAtIndex_(2), AppKit.NSLineToBezierPathElement)
        self.assertEqual(p.elementAtIndex_(3), AppKit.NSCurveToBezierPathElement)
        self.assertEqual(p.elementAtIndex_(4), AppKit.NSClosePathBezierPathElement)

        tp, points = p.elementAtIndex_associatedPoints_(0)
        self.assertEqual(tp, AppKit.NSMoveToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (10, 10))

        tp, points = p.elementAtIndex_associatedPoints_(1)
        self.assertEqual(tp, AppKit.NSLineToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (20, 30))

        tp, points = p.elementAtIndex_associatedPoints_(2)
        self.assertEqual(tp, AppKit.NSLineToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (30, 20))

        tp, points = p.elementAtIndex_associatedPoints_(3)
        self.assertEqual(tp, AppKit.NSCurveToBezierPathElement)
        self.assertEqual(len(points), 3)
        self.assertPointEquals(points[0], (10, 11))  # control point 1
        self.assertPointEquals(points[1], (20, 21))  # control point 2
        self.assertPointEquals(points[2], (40, 41))  # end point

        tp, points = p.elementAtIndex_associatedPoints_(4)
        self.assertEqual(tp, AppKit.NSClosePathBezierPathElement)
        self.assertEqual(len(points), 0)

    def test_setAssociatedPoints(self):
        p = AppKit.NSBezierPath.bezierPath()
        p.moveToPoint_((10, 10))
        p.lineToPoint_((20, 30))
        p.lineToPoint_((30, 20))
        p.curveToPoint_controlPoint1_controlPoint2_((40, 41), (10, 11), (20, 21))
        p.closePath()

        p.setAssociatedPoints_atIndex_([(0, 1)], 0)
        tp, points = p.elementAtIndex_associatedPoints_(0)
        self.assertEqual(tp, AppKit.NSMoveToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (0, 1))

        p.setAssociatedPoints_atIndex_([(0, 1), (2, 3), (3, 4)], 3)
        tp, points = p.elementAtIndex_associatedPoints_(3)
        self.assertEqual(tp, AppKit.NSCurveToBezierPathElement)
        self.assertEqual(len(points), 3)
        self.assertPointEquals(points[0], (0, 1))  # control point 1
        self.assertPointEquals(points[1], (2, 3))  # control point 2
        self.assertPointEquals(points[2], (3, 4))  # end point

    def testConstants(self):
        self.assertEqual(AppKit.NSButtLineCapStyle, 0)
        self.assertEqual(AppKit.NSRoundLineCapStyle, 1)
        self.assertEqual(AppKit.NSSquareLineCapStyle, 2)

        self.assertEqual(AppKit.NSMiterLineJoinStyle, 0)
        self.assertEqual(AppKit.NSRoundLineJoinStyle, 1)
        self.assertEqual(AppKit.NSBevelLineJoinStyle, 2)

        self.assertEqual(AppKit.NSNonZeroWindingRule, 0)
        self.assertEqual(AppKit.NSEvenOddWindingRule, 1)

        self.assertEqual(AppKit.NSMoveToBezierPathElement, 0)
        self.assertEqual(AppKit.NSLineToBezierPathElement, 1)
        self.assertEqual(AppKit.NSCurveToBezierPathElement, 2)
        self.assertEqual(AppKit.NSClosePathBezierPathElement, 3)

        self.assertEqual(AppKit.NSLineCapStyleButt, 0)
        self.assertEqual(AppKit.NSLineCapStyleRound, 1)
        self.assertEqual(AppKit.NSLineCapStyleSquare, 2)

        self.assertEqual(AppKit.NSLineJoinStyleMiter, 0)
        self.assertEqual(AppKit.NSLineJoinStyleRound, 1)
        self.assertEqual(AppKit.NSLineJoinStyleBevel, 2)

        self.assertEqual(AppKit.NSWindingRuleNonZero, 0)
        self.assertEqual(AppKit.NSWindingRuleEvenOdd, 1)

        self.assertEqual(AppKit.NSBezierPathElementMoveTo, 0)
        self.assertEqual(AppKit.NSBezierPathElementLineTo, 1)
        self.assertEqual(AppKit.NSBezierPathElementCurveTo, 2)
        self.assertEqual(AppKit.NSBezierPathElementClosePath, 3)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSBezierPath.isEmpty)
        self.assertResultIsBOOL(AppKit.NSBezierPath.containsPoint_)
        self.assertResultIsBOOL(AppKit.NSBezierPath.cachesBezierPath)
        self.assertArgIsBOOL(AppKit.NSBezierPath.setCachesBezierPath_, 0)
        self.assertArgIsBOOL(
            AppKit.NSBezierPath.appendBezierPathWithArcWithCenter_radius_startAngle_endAngle_clockwise_,  # noqa: B950
            4,
        )

        self.assertArgSizeInArg(
            AppKit.NSBezierPath.appendBezierPathWithGlyphs_count_inFont_, 0, 1
        )

        # XXX: AppKit.NSBezierPath.drawPackedGlyphs_atPoint_
        # XXX: AppKit.NSBezierPath.appendBezierPathWithPackedGlyphs_
