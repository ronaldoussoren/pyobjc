from PyObjCTools.TestSupport import *

from AppKit import *
import objc

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
        self.fail("- (void)getRectsBeingDrawn:(const NSRect **)rects count:(NSInteger *)count;")
        self.fail("- (void)sortSubviewsUsingFunction:(NSComparisonResult (*)(id, id, void *))compare context:(void *)context;")

        self.fail("- (NSTrackingRectTag)addTrackingRect:(NSRect)aRect owner:(id)anObject userData:(void *)data assumeInside:(BOOL)flag;")
        self.fail("- (NSToolTipTag)addToolTipRect:(NSRect)aRect owner:(id)anObject userData:(void *)data;")
        self.fail("- (void)getRectsExposedDuringLiveResize:(NSRect[4])exposedRects count:(NSInteger *)count;")
        self.fail("- (NSString *)view:(NSView *)view stringForToolTip:(NSToolTipTag)tag point:(NSPoint)point userData:(void *)data;")








if __name__ == "__main__":
    main()
