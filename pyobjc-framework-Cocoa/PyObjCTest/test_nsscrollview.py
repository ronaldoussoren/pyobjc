from AppKit import *
from PyObjCTools.TestSupport import *


class TesNSScrollView (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(NSScrollView.frameSizeForContentSize_hasHorizontalScroller_hasVerticalScroller_borderType_, 1)
        self.assertArgIsBOOL(NSScrollView.frameSizeForContentSize_hasHorizontalScroller_hasVerticalScroller_borderType_, 2)
        self.assertArgIsBOOL(NSScrollView.contentSizeForFrameSize_hasHorizontalScroller_hasVerticalScroller_borderType_, 1)
        self.assertArgIsBOOL(NSScrollView.contentSizeForFrameSize_hasHorizontalScroller_hasVerticalScroller_borderType_, 2)

        self.assertResultIsBOOL(NSScrollView.drawsBackground)
        self.assertArgIsBOOL(NSScrollView.setDrawsBackground_, 0)
        self.assertResultIsBOOL(NSScrollView.hasVerticalScroller)
        self.assertArgIsBOOL(NSScrollView.setHasVerticalScroller_, 0)
        self.assertResultIsBOOL(NSScrollView.hasHorizontalScroller)
        self.assertArgIsBOOL(NSScrollView.setHasHorizontalScroller_, 0)
        self.assertResultIsBOOL(NSScrollView.autohidesScrollers)
        self.assertArgIsBOOL(NSScrollView.setAutohidesScrollers_, 0)
        self.assertResultIsBOOL(NSScrollView.scrollsDynamically)
        self.assertArgIsBOOL(NSScrollView.setScrollsDynamically_, 0)
        self.assertResultIsBOOL(NSScrollView.rulersVisible)
        self.assertArgIsBOOL(NSScrollView.setRulersVisible_, 0)
        self.assertResultIsBOOL(NSScrollView.hasHorizontalRuler)
        self.assertArgIsBOOL(NSScrollView.setHasHorizontalRuler_, 0)
        self.assertResultIsBOOL(NSScrollView.hasVerticalRuler)
        self.assertArgIsBOOL(NSScrollView.setHasVerticalRuler_, 0)


if __name__ == "__main__":
    main()
