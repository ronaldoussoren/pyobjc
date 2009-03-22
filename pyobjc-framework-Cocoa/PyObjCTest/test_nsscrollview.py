from AppKit import *
from PyObjCTools.TestSupport import *


class TesNSScrollView (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSScrollView.frameSizeForContentSize_hasHorizontalScroller_hasVerticalScroller_borderType_, 1)
        self.failUnlessArgIsBOOL(NSScrollView.frameSizeForContentSize_hasHorizontalScroller_hasVerticalScroller_borderType_, 2)
        self.failUnlessArgIsBOOL(NSScrollView.contentSizeForFrameSize_hasHorizontalScroller_hasVerticalScroller_borderType_, 1)
        self.failUnlessArgIsBOOL(NSScrollView.contentSizeForFrameSize_hasHorizontalScroller_hasVerticalScroller_borderType_, 2)

        self.failUnlessResultIsBOOL(NSScrollView.drawsBackground)
        self.failUnlessArgIsBOOL(NSScrollView.setDrawsBackground_, 0)
        self.failUnlessResultIsBOOL(NSScrollView.hasVerticalScroller)
        self.failUnlessArgIsBOOL(NSScrollView.setHasVerticalScroller_, 0)
        self.failUnlessResultIsBOOL(NSScrollView.hasHorizontalScroller)
        self.failUnlessArgIsBOOL(NSScrollView.setHasHorizontalScroller_, 0)
        self.failUnlessResultIsBOOL(NSScrollView.autohidesScrollers)
        self.failUnlessArgIsBOOL(NSScrollView.setAutohidesScrollers_, 0)
        self.failUnlessResultIsBOOL(NSScrollView.scrollsDynamically)
        self.failUnlessArgIsBOOL(NSScrollView.setScrollsDynamically_, 0)
        self.failUnlessResultIsBOOL(NSScrollView.rulersVisible)
        self.failUnlessArgIsBOOL(NSScrollView.setRulersVisible_, 0)
        self.failUnlessResultIsBOOL(NSScrollView.hasHorizontalRuler)
        self.failUnlessArgIsBOOL(NSScrollView.setHasHorizontalRuler_, 0)
        self.failUnlessResultIsBOOL(NSScrollView.hasVerticalRuler)
        self.failUnlessArgIsBOOL(NSScrollView.setHasVerticalRuler_, 0)


if __name__ == "__main__":
    main()
