import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSRulerViewHelper(AppKit.NSView):
    def rulerView_shouldMoveMarker_(self, rl, mk):
        return 1

    def rulerView_willMoveMarker_toLocation_(self, rl, mk, x):
        return 1

    def rulerView_didMoveMarker_(self, rv, mk):
        pass

    def rulerView_shouldRemoveMarker_(self, rv, mk):
        return 1

    def rulerView_didRemoveMarker_(self, rv, mk):
        pass

    def rulerView_shouldAddMarker_(self, rv, mk):
        return 1

    def rulerView_willAddMarker_atLocation_(self, rv, mk, x):
        return 1

    def rulerView_didAddMarker_(self, rv, mk):
        pass

    def rulerView_handleMouseDown_(self, rv, ev):
        pass

    def rulerView_willSetClientView_(self, rv, vw):
        pass

    def rulerView_locationForPoint_(self, rv, vw):
        return 1

    def rulerView_pointForLocation_(self, rv, vw):
        return 1


class TestNSRulerView(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSRulerViewUnitName, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSRulerOrientation)

    def testConstants(self):
        self.assertEqual(AppKit.NSHorizontalRuler, 0)
        self.assertEqual(AppKit.NSVerticalRuler, 1)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AppKit.NSRulerViewUnitInches, str)
        self.assertIsInstance(AppKit.NSRulerViewUnitCentimeters, str)
        self.assertIsInstance(AppKit.NSRulerViewUnitPoints, str)
        self.assertIsInstance(AppKit.NSRulerViewUnitPicas, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSRulerView.trackMarker_withMouseEvent_)
        self.assertResultIsBOOL(AppKit.NSRulerView.isFlipped)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSRulerViewHelper.rulerView_shouldMoveMarker_)

        self.assertResultHasType(
            TestNSRulerViewHelper.rulerView_willMoveMarker_toLocation_, objc._C_CGFloat
        )
        self.assertArgHasType(
            TestNSRulerViewHelper.rulerView_willMoveMarker_toLocation_,
            2,
            objc._C_CGFloat,
        )

        self.assertResultIsBOOL(TestNSRulerViewHelper.rulerView_shouldRemoveMarker_)
        self.assertResultIsBOOL(TestNSRulerViewHelper.rulerView_shouldAddMarker_)
        self.assertResultHasType(
            TestNSRulerViewHelper.rulerView_willAddMarker_atLocation_, objc._C_CGFloat
        )
        self.assertArgHasType(
            TestNSRulerViewHelper.rulerView_willAddMarker_atLocation_,
            2,
            objc._C_CGFloat,
        )

        self.assertResultHasType(
            TestNSRulerViewHelper.rulerView_locationForPoint_, objc._C_CGFloat
        )
        self.assertArgHasType(
            TestNSRulerViewHelper.rulerView_locationForPoint_,
            1,
            AppKit.NSPoint.__typestr__,
        )

        self.assertResultHasType(
            TestNSRulerViewHelper.rulerView_pointForLocation_,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSRulerViewHelper.rulerView_pointForLocation_, 1, objc._C_CGFloat
        )
