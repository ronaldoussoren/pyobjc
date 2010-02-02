
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSRulerViewHelper (NSView):
    def rulerView_shouldMoveMarker_(self, rl, mk): return 1
    def rulerView_willMoveMarker_toLocation_(self, rl, mk, l): return 1
    def rulerView_didMoveMarker_(self, rv, mk): pass
    def rulerView_shouldRemoveMarker_(self, rv, mk): return 1
    def rulerView_didRemoveMarker_(self, rv, mk): pass
    def rulerView_shouldAddMarker_(self, rv, mk): return 1
    def rulerView_willAddMarker_atLocation_(self, rv, mk, l): return 1
    def rulerView_didAddMarker_(self, rv, mk): pass
    def rulerView_handleMouseDown_(self, rv , ev): pass
    def rulerView_willSetClientView_(self, rv, vw): pass

class TestNSRulerView (TestCase):
    def testConstants(self):
        self.assertEqual(NSHorizontalRuler, 0)
        self.assertEqual(NSVerticalRuler, 1)

    def testMethods(self):
        self.assertResultIsBOOL(NSRulerView.trackMarker_withMouseEvent_)
        self.assertResultIsBOOL(NSRulerView.isFlipped)

    def testProtocols(self):
        self.assertResultIsBOOL(TestNSRulerViewHelper.rulerView_shouldMoveMarker_)

        self.assertResultHasType(TestNSRulerViewHelper.rulerView_willMoveMarker_toLocation_, objc._C_CGFloat)
        self.assertArgHasType(TestNSRulerViewHelper.rulerView_willMoveMarker_toLocation_, 2, objc._C_CGFloat)

        self.assertResultIsBOOL(TestNSRulerViewHelper.rulerView_shouldRemoveMarker_)
        self.assertResultIsBOOL(TestNSRulerViewHelper.rulerView_shouldAddMarker_)
        self.assertResultHasType(TestNSRulerViewHelper.rulerView_willAddMarker_atLocation_, objc._C_CGFloat)
        self.assertArgHasType(TestNSRulerViewHelper.rulerView_willAddMarker_atLocation_, 2, objc._C_CGFloat)

if __name__ == "__main__":
    main()
