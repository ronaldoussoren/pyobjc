from PyObjCTools.TestSupport import *

from AppKit import *
import objc

class TestNSViewHelper (NSObject):
    def view_stringForToolTip_point_userData_(self, a, b, c, d): return 1

class ObjCTestNSView_KnowPageRange (NSView):
    def knowsPageRange_(self, range):
        return  objc.YES, (1, 10)

    def rectForPage_(self, page):
        return ((1,1),(2,2))

class TestNSView (TestCase):

    def test_knowsPageRange(self):
        method = ObjCTestNSView_KnowPageRange.knowsPageRange_
        self.assertEqual(method.__metadata__()['arguments'][2]['type'], b'o^' + NSRange.__typestr__)

    def test_rectForPage(self):
        method = ObjCTestNSView_KnowPageRange.rectForPage_


        self.assertResultHasType(method, NSRect.__typestr__)
        #self.assertEqual(objc.splitSignature(method.signature), objc.splitSignature(NSRect.__typestr__+b"@:" + objc._C_NSInteger))


class TestHeader (TestCase):
    def testConstants(self):
        self.assertEqual(NSViewNotSizable,  0)
        self.assertEqual(NSViewMinXMargin,  1)
        self.assertEqual(NSViewWidthSizable,  2)
        self.assertEqual(NSViewMaxXMargin,  4)
        self.assertEqual(NSViewMinYMargin,  8)
        self.assertEqual(NSViewHeightSizable, 16)
        self.assertEqual(NSViewMaxYMargin, 32)
        self.assertEqual(NSNoBorder, 0)
        self.assertEqual(NSLineBorder, 1)
        self.assertEqual(NSBezelBorder, 2)
        self.assertEqual(NSGrooveBorder, 3)

        self.assertIsInstance(NSViewFrameDidChangeNotification, unicode)
        self.assertIsInstance(NSViewFocusDidChangeNotification, unicode)
        self.assertIsInstance(NSViewBoundsDidChangeNotification, unicode)
        self.assertIsInstance(NSViewGlobalFrameDidChangeNotification, unicode)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(NSFullScreenModeAllScreens, unicode)
        self.assertIsInstance(NSFullScreenModeSetting, unicode)
        self.assertIsInstance(NSFullScreenModeWindowLevel, unicode)
        self.assertIsInstance(NSViewDidUpdateTrackingAreasNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSViewLayerContentsRedrawNever, 0)
        self.assertEqual(NSViewLayerContentsRedrawOnSetNeedsDisplay, 1)
        self.assertEqual(NSViewLayerContentsRedrawDuringViewResize, 2)
        self.assertEqual(NSViewLayerContentsRedrawBeforeViewResize, 3)

        self.assertEqual(NSViewLayerContentsPlacementScaleAxesIndependently, 0)
        self.assertEqual(NSViewLayerContentsPlacementScaleProportionallyToFit, 1)
        self.assertEqual(NSViewLayerContentsPlacementScaleProportionallyToFill, 2)
        self.assertEqual(NSViewLayerContentsPlacementCenter, 3)
        self.assertEqual(NSViewLayerContentsPlacementTop, 4)
        self.assertEqual(NSViewLayerContentsPlacementTopRight, 5)
        self.assertEqual(NSViewLayerContentsPlacementRight, 6)
        self.assertEqual(NSViewLayerContentsPlacementBottomRight, 7)
        self.assertEqual(NSViewLayerContentsPlacementBottom, 8)
        self.assertEqual(NSViewLayerContentsPlacementBottomLeft, 9)
        self.assertEqual(NSViewLayerContentsPlacementLeft, 10)
        self.assertEqual(NSViewLayerContentsPlacementTopLeft, 11)

        self.assertIsInstance(NSDefinitionPresentationTypeKey, unicode)
        self.assertIsInstance(NSDefinitionPresentationTypeOverlay, unicode)
        self.assertIsInstance(NSDefinitionPresentationTypeDictionaryApplication, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSView.isDescendantOf_)
        self.assertResultIsBOOL(NSView.isHidden)
        self.assertResultIsBOOL(NSView.isHiddenOrHasHiddenAncestor)
        self.assertArgIsBOOL(NSView.setHidden_, 0)
        self.assertResultIsBOOL(NSView.needsToDrawRect_)
        self.assertResultIsBOOL(NSView.wantsDefaultClipping)

        self.assertArgIsFunction(NSView.sortSubviewsUsingFunction_context_, 0, b'i@@@', False)
        self.assertArgHasType(NSView.sortSubviewsUsingFunction_context_, 1, b'@')

        self.assertResultIsBOOL(NSView.postsFrameChangedNotifications)
        self.assertArgIsBOOL(NSView.setPostsFrameChangedNotifications_, 0)
        self.assertResultIsBOOL(NSView.autoresizesSubviews)
        self.assertArgIsBOOL(NSView.setAutoresizesSubviews_, 0)
        self.assertResultIsBOOL(NSView.isFlipped)
        self.assertResultIsBOOL(NSView.isRotatedFromBase)
        self.assertResultIsBOOL(NSView.isRotatedOrScaledFromBase)
        self.assertResultIsBOOL(NSView.isOpaque)
        self.assertResultIsBOOL(NSView.canDraw)
        self.assertArgIsBOOL(NSView.setNeedsDisplay_, 0)
        self.assertResultIsBOOL(NSView.needsDisplay)
        self.assertResultIsBOOL(NSView.lockFocusIfCanDraw)
        self.assertResultIsBOOL(NSView.lockFocusIfCanDrawInContext_)
        self.assertResultIsBOOL(NSView.scrollRectToVisible_)
        self.assertResultIsBOOL(NSView.autoscroll_)
        self.assertResultIsBOOL(NSView.mouse_inRect_)
        self.assertResultIsBOOL(NSView.performKeyEquivalent_)
        self.assertResultIsBOOL(NSView.acceptsFirstMouse_)
        self.assertResultIsBOOL(NSView.shouldDelayWindowOrderingForEvent_)
        self.assertResultIsBOOL(NSView.needsPanelToBecomeKey)
        self.assertResultIsBOOL(NSView.mouseDownCanMoveWindow)
        self.assertArgHasType(NSView.addTrackingRect_owner_userData_assumeInside_, 2, b'^v')
        self.assertArgIsBOOL(NSView.addTrackingRect_owner_userData_assumeInside_, 3)
        self.assertResultIsBOOL(NSView.shouldDrawColor)
        self.assertResultIsBOOL(NSView.postsBoundsChangedNotifications)
        self.assertArgIsBOOL(NSView.setPostsBoundsChangedNotifications_, 0)
        self.assertResultIsBOOL(NSView.inLiveResize)
        self.assertResultIsBOOL(NSView.preservesContentDuringLiveResize)

        self.assertArgHasType(NSView.getRectsExposedDuringLiveResize_count_, 0, b'o^' + NSRect.__typestr__)
        m = NSView.getRectsExposedDuringLiveResize_count_.__metadata__()['arguments'][2]
        self.assertEqual(m['c_array_of_fixed_length'], 4)
        self.assertArgIsOut(NSView.getRectsExposedDuringLiveResize_count_, 1)

        self.assertResultIsBOOL(NSView.performMnemonic_)
        self.assertResultIsBOOL(NSView.canBecomeKeyView)
        self.assertResultIsBOOL(NSView.knowsPageRange_)
        self.assertArgIsOut(NSView.adjustPageWidthNew_left_right_limit_, 0)
        self.assertArgIsOut(NSView.adjustPageHeightNew_top_bottom_limit_, 0)

        self.assertArgIsBOOL(NSView.dragImage_at_offset_event_pasteboard_source_slideBack_, 6)
        self.assertResultIsBOOL(NSView.dragFile_fromRect_slideBack_event_)
        self.assertArgIsBOOL(NSView.dragFile_fromRect_slideBack_event_, 2)
        self.assertResultIsBOOL(NSView.dragPromisedFilesOfTypes_fromRect_source_slideBack_event_)
        self.assertArgIsBOOL(NSView.dragPromisedFilesOfTypes_fromRect_source_slideBack_event_, 3)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsBOOL(NSView.setWantsLayer_, 0)
        self.assertResultIsBOOL(NSView.wantsLayer)
        self.assertResultIsBOOL(NSView.enterFullScreenMode_withOptions_)
        self.assertResultIsBOOL(NSView.isInFullScreenMode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSView.canDrawConcurrently)
        self.assertArgIsBOOL(NSView.setCanDrawConcurrently_, 0)
        self.assertResultIsBOOL(NSView.acceptsTouchEvents)
        self.assertArgIsBOOL(NSView.setAcceptsTouchEvents_, 0)
        self.assertResultIsBOOL(NSView.wantsRestingTouches)
        self.assertArgIsBOOL(NSView.setWantsRestingTouches_, 0)

        self.assertArgHasType(NSView.showDefinitionForAttributedString_atPoint_, 1, NSPoint.__typestr__)

        self.assertArgHasType(NSView.showDefinitionForAttributedString_range_options_baselineOriginProvider_, 1, NSRange.__typestr__)
        self.assertArgIsBlock(NSView.showDefinitionForAttributedString_range_options_baselineOriginProvider_, 3, 
                NSPoint.__typestr__ + NSRange.__typestr__)


    def testProtocol(self):
        self.assertArgHasType(TestNSViewHelper.view_stringForToolTip_point_userData_, 2, NSPoint.__typestr__)
        self.assertArgHasType(TestNSViewHelper.view_stringForToolTip_point_userData_, 3, b'^v')


    def testMissingTests(self):
        v = NSView.alloc().init()
        v.setNeedsDisplayInRect_(((0, 0), (50, 50)))
        r = v.getRectsBeingDrawn_count_(None, None)
        self.assertIsInstance(r, tuple)
        self.assertEqual(len(r), 2)
        self.assertIsInstance(r[0], tuple)
        self.assertIsInstance(r[1], (int, long))
        if r[1] != 0:
            self.assertIsInstance(r[0][0], NSRect)







if __name__ == "__main__":
    main()
