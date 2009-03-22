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
        self.assertEquals(method.__metadata__()['arguments'][2]['type'], 'o^{_NSRange=II}')

    def test_rectForPage(self):
        method = ObjCTestNSView_KnowPageRange.rectForPage_
        self.assertEquals(objc.splitSignature(method.signature), objc.splitSignature("{_NSRect={_NSPoint=ff}{_NSSize=ff}}12@0:4i8"))


class TestHeader (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSViewNotSizable,  0)
        self.failUnlessEqual(NSViewMinXMargin,  1)
        self.failUnlessEqual(NSViewWidthSizable,  2)
        self.failUnlessEqual(NSViewMaxXMargin,  4)
        self.failUnlessEqual(NSViewMinYMargin,  8)
        self.failUnlessEqual(NSViewHeightSizable, 16)
        self.failUnlessEqual(NSViewMaxYMargin, 32)
        self.failUnlessEqual(NSNoBorder, 0)
        self.failUnlessEqual(NSLineBorder, 1)
        self.failUnlessEqual(NSBezelBorder, 2)
        self.failUnlessEqual(NSGrooveBorder, 3)

        self.failUnlessIsInstance(NSViewFrameDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSViewFocusDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSViewBoundsDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSViewGlobalFrameDidChangeNotification, unicode)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessIsInstance(NSFullScreenModeAllScreens, unicode)
        self.failUnlessIsInstance(NSFullScreenModeSetting, unicode)
        self.failUnlessIsInstance(NSFullScreenModeWindowLevel, unicode)
        self.failUnlessIsInstance(NSViewDidUpdateTrackingAreasNotification, unicode)



    def testMethods(self):
        self.failUnlessResultIsBOOL(NSView.isDescendantOf_)
        self.failUnlessResultIsBOOL(NSView.isHidden)
        self.failUnlessResultIsBOOL(NSView.isHiddenOrHasHiddenAncestor)
        self.failUnlessArgIsBOOL(NSView.setHidden_, 0)
        self.failUnlessResultIsBOOL(NSView.needsToDrawRect_)
        self.failUnlessResultIsBOOL(NSView.wantsDefaultClipping)

        self.failUnlessArgIsFunction(NSView.sortSubviewsUsingFunction_context_, 0, 'i@@@', False)
        self.failUnlessArgHasType(NSView.sortSubviewsUsingFunction_context_, 1, '@')

        self.failUnlessResultIsBOOL(NSView.postsFrameChangedNotifications)
        self.failUnlessArgIsBOOL(NSView.setPostsFrameChangedNotifications_, 0)
        self.failUnlessResultIsBOOL(NSView.autoresizesSubviews)
        self.failUnlessArgIsBOOL(NSView.setAutoresizesSubviews_, 0)
        self.failUnlessResultIsBOOL(NSView.isFlipped)
        self.failUnlessResultIsBOOL(NSView.isRotatedFromBase)
        self.failUnlessResultIsBOOL(NSView.isRotatedOrScaledFromBase)
        self.failUnlessResultIsBOOL(NSView.isOpaque)
        self.failUnlessResultIsBOOL(NSView.canDraw)
        self.failUnlessArgIsBOOL(NSView.setNeedsDisplay_, 0)
        self.failUnlessResultIsBOOL(NSView.needsDisplay)
        self.failUnlessResultIsBOOL(NSView.lockFocusIfCanDraw)
        self.failUnlessResultIsBOOL(NSView.lockFocusIfCanDrawInContext_)
        self.failUnlessResultIsBOOL(NSView.scrollRectToVisible_)
        self.failUnlessResultIsBOOL(NSView.autoscroll_)
        self.failUnlessResultIsBOOL(NSView.mouse_inRect_)
        self.failUnlessResultIsBOOL(NSView.performKeyEquivalent_)
        self.failUnlessResultIsBOOL(NSView.acceptsFirstMouse_)
        self.failUnlessResultIsBOOL(NSView.shouldDelayWindowOrderingForEvent_)
        self.failUnlessResultIsBOOL(NSView.needsPanelToBecomeKey)
        self.failUnlessResultIsBOOL(NSView.mouseDownCanMoveWindow)
        self.failUnlessArgHasType(NSView.addTrackingRect_owner_userData_assumeInside_, 2, '^v')
        self.failUnlessArgIsBOOL(NSView.addTrackingRect_owner_userData_assumeInside_, 3)
        self.failUnlessResultIsBOOL(NSView.shouldDrawColor)
        self.failUnlessResultIsBOOL(NSView.postsBoundsChangedNotifications)
        self.failUnlessArgIsBOOL(NSView.setPostsBoundsChangedNotifications_, 0)
        self.failUnlessResultIsBOOL(NSView.inLiveResize)
        self.failUnlessResultIsBOOL(NSView.preservesContentDuringLiveResize)

        self.failUnlessArgHasType(NSView.getRectsExposedDuringLiveResize_count_, 0, 'o^' + NSRect.__typestr__)
        m = NSView.getRectsExposedDuringLiveResize_count_.__metadata__()['arguments'][2]
        self.failUnlessEqual(m['c_array_of_fixed_length'], 4)
        self.failUnlessArgIsOut(NSView.getRectsExposedDuringLiveResize_count_, 1)

        self.failUnlessResultIsBOOL(NSView.performMnemonic_)
        self.failUnlessResultIsBOOL(NSView.canBecomeKeyView)
        self.failUnlessResultIsBOOL(NSView.knowsPageRange_)
        self.failUnlessArgIsOut(NSView.adjustPageWidthNew_left_right_limit_, 0)
        self.failUnlessArgIsOut(NSView.adjustPageHeightNew_top_bottom_limit_, 0)

        self.failUnlessArgIsBOOL(NSView.dragImage_at_offset_event_pasteboard_source_slideBack_, 6)
        self.failUnlessResultIsBOOL(NSView.dragFile_fromRect_slideBack_event_)
        self.failUnlessArgIsBOOL(NSView.dragFile_fromRect_slideBack_event_, 2)
        self.failUnlessResultIsBOOL(NSView.dragPromisedFilesOfTypes_fromRect_source_slideBack_event_)
        self.failUnlessArgIsBOOL(NSView.dragPromisedFilesOfTypes_fromRect_source_slideBack_event_, 3)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsBOOL(NSView.setWantsLayer_, 0)
        self.failUnlessResultIsBOOL(NSView.wantsLayer)
        self.failUnlessResultIsBOOL(NSView.enterFullScreenMode_withOptions_)
        self.failUnlessResultIsBOOL(NSView.isInFullScreenMode)


    def testProtocol(self):
        self.failUnlessArgHasType(TestNSViewHelper.view_stringForToolTip_point_userData_, 2, NSPoint.__typestr__)
        self.failUnlessArgHasType(TestNSViewHelper.view_stringForToolTip_point_userData_, 3, '^v')


    def testMissingTests(self):
        v = NSView.alloc().init()
        v.setNeedsDisplayInRect_(((0, 0), (50, 50)))
        r = v.getRectsBeingDrawn_count_(None, None)
        self.failUnlessIsInstance(r, tuple)
        self.failUnlessEqual(len(r), 2)
        self.failUnlessIsInstance(r[0], tuple)
        self.failUnlessIsInstance(r[1], (int, long))
        if r[1] != 0:
            self.failUnlessIsInstance(r[0][0], NSRect)







if __name__ == "__main__":
    main()
