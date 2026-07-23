# Test special methods of AppKit.NSBezierPath
# TODO: Test implementing these in python.
import objc
import AppKit
import warnings
from PyObjCTools.TestSupport import TestCase
from .testhelper import PyObjC_TestClass3


class OC_BezierPath(AppKit.NSBezierPath):
    def elementAtIndex_associatedPoints_(self, index, points):
        if index == 1:
            return 42

        elif index == 2:
            return (AppKit.NSBezierPathElementMoveTo, ())

        elif index == 3:
            return (AppKit.NSBezierPathElementMoveTo, ((1, 2),))

        elif index == 4:
            return (AppKit.NSBezierPathElementLineTo, ((3, 4),))

        elif index == 5:
            return (AppKit.NSBezierPathElementCubicCurveTo, ((5, 6), (7, 8), (9, 10)))

        elif index == 6:
            return (AppKit.NSBezierPathElementClosePath, ())

        elif index == 7:
            return (AppKit.NSBezierPathElementQuadraticCurveTo, ((11, 12),))

        elif index == 8:
            raise RuntimeError("method error")

        elif index == 9:
            return (AppKit.NSBezierPathElementMoveTo, (1, 2), 4)

        elif index == 10:
            return (AppKit.NSBezierPathElementMoveTo, ((1, "2"),))

        elif index == 11:
            return ("move-to", ((1, 2),))

        else:
            return AppKit.NSBezierPathElementQuadraticCurveTo + 5, ((0, 1), (2, 3))


class TestNSBezierPath(TestCase):
    def test_enums(self):
        # Legacy alias:
        self.assertEqual(AppKit.NSButtLineCapStyle, 0)
        self.assertEqual(AppKit.NSRoundLineCapStyle, 1)
        self.assertEqual(AppKit.NSSquareLineCapStyle, 2)

        # Legacy alias:
        self.assertEqual(AppKit.NSMiterLineJoinStyle, 0)
        self.assertEqual(AppKit.NSRoundLineJoinStyle, 1)
        self.assertEqual(AppKit.NSBevelLineJoinStyle, 2)

        # Legacy alias:
        self.assertEqual(AppKit.NSNonZeroWindingRule, 0)
        self.assertEqual(AppKit.NSEvenOddWindingRule, 1)

        self.assertEqual(AppKit.NSMoveToBezierPathElement, 0)
        self.assertEqual(AppKit.NSLineToBezierPathElement, 1)
        self.assertEqual(AppKit.NSCurveToBezierPathElement, 2)
        self.assertEqual(AppKit.NSClosePathBezierPathElement, 3)

        self.assertIsEnumType(AppKit.NSLineCapStyle)
        self.assertEqual(AppKit.NSLineCapStyleButt, 0)
        self.assertEqual(AppKit.NSLineCapStyleRound, 1)
        self.assertEqual(AppKit.NSLineCapStyleSquare, 2)

        self.assertIsEnumType(AppKit.NSLineJoinStyle)
        self.assertEqual(AppKit.NSLineJoinStyleMiter, 0)
        self.assertEqual(AppKit.NSLineJoinStyleRound, 1)
        self.assertEqual(AppKit.NSLineJoinStyleBevel, 2)

        self.assertIsEnumType(AppKit.NSWindingRule)
        self.assertEqual(AppKit.NSWindingRuleNonZero, 0)
        self.assertEqual(AppKit.NSWindingRuleEvenOdd, 1)

        self.assertIsEnumType(AppKit.NSBezierPathElement)
        self.assertEqual(AppKit.NSBezierPathElementMoveTo, 0)
        self.assertEqual(AppKit.NSBezierPathElementLineTo, 1)
        self.assertEqual(AppKit.NSBezierPathElementCurveTo, 2)
        self.assertEqual(AppKit.NSBezierPathElementClosePath, 3)
        self.assertEqual(AppKit.NSBezierPathElementCubicCurveTo, 2)
        self.assertEqual(AppKit.NSBezierPathElementClosePath, 3)
        self.assertEqual(AppKit.NSBezierPathElementQuadraticCurveTo, 4)
        self.assertEqual(
            AppKit.NSBezierPathElementCurveTo, AppKit.NSBezierPathElementCubicCurveTo
        )

    def test_methods(self):
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


class TestNSBezierPathUsage(TestCase):
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

    def test_append_points(self):
        p = AppKit.NSBezierPath.bezierPath()
        self.assertIsNot(p, None)
        self.assertEqual(p.elementCount(), 0)

        points = [(0, 0), (100, 0), (100, 100), (0, 0)]
        p.appendBezierPathWithPoints_count_(points, 3)
        self.assertEqual(p.elementCount(), 3)

    def test_set_linedash(self):
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

    def test_element_at_index(self):
        p = AppKit.NSBezierPath.bezierPath()
        p.moveToPoint_((10, 10))
        p.lineToPoint_((20, 30))
        p.lineToPoint_((30, 20))
        p.curveToPoint_controlPoint1_controlPoint2_((40, 41), (10, 11), (20, 21))

        if objc.macos_available(14, 0):
            p.relativeCurveToPoint_controlPoint_((90, 90), (100, 80))
        p.closePath()

        self.assertEqual(p.elementAtIndex_(0), AppKit.NSMoveToBezierPathElement)
        self.assertEqual(p.elementAtIndex_(1), AppKit.NSLineToBezierPathElement)
        self.assertEqual(p.elementAtIndex_(2), AppKit.NSLineToBezierPathElement)
        self.assertEqual(p.elementAtIndex_(3), AppKit.NSCurveToBezierPathElement)

        if objc.macos_available(14, 0):
            self.assertEqual(
                p.elementAtIndex_(4), AppKit.NSBezierPathElementQuadraticCurveTo
            )
            self.assertEqual(p.elementAtIndex_(5), AppKit.NSClosePathBezierPathElement)
        else:
            self.assertEqual(p.elementAtIndex_(4), AppKit.NSClosePathBezierPathElement)

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            p.elementAtIndex_associatedPoints_()

        with self.assertRaisesRegex(ValueError, "buffer must be None"):
            p.elementAtIndex_associatedPoints_(0, 42)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            p.elementAtIndex_associatedPoints_("0", None)

        tp, points = p.elementAtIndex_associatedPoints_(0, None)
        self.assertEqual(tp, AppKit.NSMoveToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (10, 10))

        tp, points = p.elementAtIndex_associatedPoints_(1, None)
        self.assertEqual(tp, AppKit.NSLineToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (20, 30))

        tp, points = p.elementAtIndex_associatedPoints_(2, None)
        self.assertEqual(tp, AppKit.NSLineToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (30, 20))

        tp, points = p.elementAtIndex_associatedPoints_(3, None)
        self.assertEqual(tp, AppKit.NSCurveToBezierPathElement)
        self.assertEqual(len(points), 3)
        self.assertPointEquals(points[0], (10, 11))  # control point 1
        self.assertPointEquals(points[1], (20, 21))  # control point 2
        self.assertPointEquals(points[2], (40, 41))  # end point

        if objc.macos_available(14, 0):
            tp, points = p.elementAtIndex_associatedPoints_(4, None)
            self.assertEqual(tp, AppKit.NSBezierPathElementQuadraticCurveTo)
            self.assertEqual(len(points), 1)
            self.assertPointEquals(points[0], (140, 121))  # control point

            tp, points = p.elementAtIndex_associatedPoints_(5, None)
            self.assertEqual(tp, AppKit.NSClosePathBezierPathElement)
            self.assertEqual(len(points), 0)

        else:
            tp, points = p.elementAtIndex_associatedPoints_(4, None)
            self.assertEqual(tp, AppKit.NSClosePathBezierPathElement)
            self.assertEqual(len(points), 0)

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=DeprecationWarning)
            with self.assertRaisesRegex(
                DeprecationWarning, "leaving of the second argument is deprecated"
            ):
                p.elementAtIndex_associatedPoints_(4)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=DeprecationWarning)
            with self.assertRaisesRegex(
                ValueError, "depythonifying 'long long', got 'str'"
            ):
                p.elementAtIndex_associatedPoints_("four")

        with warnings.catch_warnings(record=True) as wrn:
            warnings.simplefilter("always", category=DeprecationWarning)
            tp, points = p.elementAtIndex_associatedPoints_(3)
            self.assertEqual(tp, AppKit.NSCurveToBezierPathElement)
            self.assertEqual(len(points), 3)
        self.assertEqual(len(wrn), 1)
        self.assertEqual(wrn[0].category, DeprecationWarning)

    def test_set_associated_points(self):
        p = AppKit.NSBezierPath.bezierPath()
        p.moveToPoint_((10, 10))
        p.lineToPoint_((20, 30))
        p.lineToPoint_((30, 20))
        p.curveToPoint_controlPoint1_controlPoint2_((40, 41), (10, 11), (20, 21))
        p.closePath()

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            p.setAssociatedPoints_atIndex_()

        with self.assertRaisesRegex(ValueError, "Need at most 3 elements"):
            p.setAssociatedPoints_atIndex_([(0, 1), (1, 2), (2, 3), (3, 4)], 0)

        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            p.setAssociatedPoints_atIndex_(42, 0)

        with self.assertRaisesRegex(
            TypeError, "depythonifying struct, got no sequence"
        ):
            p.setAssociatedPoints_atIndex_([42], 0)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str' of 3"
        ):
            p.setAssociatedPoints_atIndex_([(1, 2)], "nil")

        p.setAssociatedPoints_atIndex_([(0, 1)], 0)
        tp, points = p.elementAtIndex_associatedPoints_(0, None)
        self.assertEqual(tp, AppKit.NSMoveToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (0, 1))

        p.setAssociatedPoints_atIndex_([(0, 1), (2, 3), (3, 4)], 3)
        tp, points = p.elementAtIndex_associatedPoints_(3, None)
        self.assertEqual(tp, AppKit.NSCurveToBezierPathElement)
        self.assertEqual(len(points), 3)
        self.assertPointEquals(points[0], (0, 1))  # control point 1
        self.assertPointEquals(points[1], (2, 3))  # control point 2
        self.assertPointEquals(points[2], (3, 4))  # end point

        p.methodForSelector_(b"setAssociatedPoints:atIndex:")(p, [(2, 4)], 0)
        tp, points = p.methodForSelector_(b"elementAtIndex:associatedPoints:")(
            p, 0, None
        )
        self.assertEqual(tp, AppKit.NSMoveToBezierPathElement)
        self.assertEqual(len(points), 1)
        self.assertPointEquals(points[0], (2, 4))

    def test_python_path(self):
        p = OC_BezierPath.alloc().init()
        with self.assertRaisesRegex(TypeError, "'int' object is not iterable"):
            PyObjC_TestClass3.elementAtIndex_on_(1, p)

        with self.assertRaisesRegex(ValueError, "expected 1 points, got 0"):
            PyObjC_TestClass3.elementAtIndex_on_(2, p)

        tp, points = PyObjC_TestClass3.elementAtIndex_on_(3, p)
        self.assertEqual(tp, AppKit.NSBezierPathElementMoveTo)
        self.assertEqual(
            [i.pointValue() for i in points], [(1, 2), (0, 0), (0, 0), (0, 0), (0, 0)]
        )

        tp, points = PyObjC_TestClass3.elementAtIndex_on_(4, p)
        self.assertEqual(tp, AppKit.NSBezierPathElementLineTo)
        self.assertEqual(
            [i.pointValue() for i in points], [(3, 4), (0, 0), (0, 0), (0, 0), (0, 0)]
        )

        tp, points = PyObjC_TestClass3.elementAtIndex_on_(5, p)
        self.assertEqual(tp, AppKit.NSBezierPathElementCubicCurveTo)
        self.assertEqual(
            [i.pointValue() for i in points], [(5, 6), (7, 8), (9, 10), (0, 0), (0, 0)]
        )

        tp, points = PyObjC_TestClass3.elementAtIndex_on_(6, p)
        self.assertEqual(tp, AppKit.NSBezierPathElementClosePath)
        self.assertEqual(
            [i.pointValue() for i in points], [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        )

        tp, points = PyObjC_TestClass3.elementAtIndex_on_(7, p)
        self.assertEqual(tp, AppKit.NSBezierPathElementQuadraticCurveTo)
        self.assertEqual(
            [i.pointValue() for i in points], [(11, 12), (0, 0), (0, 0), (0, 0), (0, 0)]
        )

        with self.assertRaisesRegex(RuntimeError, "method error"):
            PyObjC_TestClass3.elementAtIndex_on_(8, p)

        with self.assertRaisesRegex(ValueError, "should return tuple of length 2"):
            PyObjC_TestClass3.elementAtIndex_on_(9, p)

        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            PyObjC_TestClass3.elementAtIndex_on_(10, p)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            PyObjC_TestClass3.elementAtIndex_on_(11, p)

        with self.assertRaisesRegex(
            ValueError, r"Return\[0\] should be NS{\*}PathElement"
        ):
            PyObjC_TestClass3.elementAtIndex_on_(12, p)
