from AppKit import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str


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

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertArgIsBOOL(NSScrollView.setAllowsMagnification_, 0)
        self.assertResultIsBOOL(NSScrollView.allowsMagnification, 0)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(NSScrollViewWillStartLiveMagnifyNotification, unicode)
        self.assertIsInstance(NSScrollViewDidEndLiveMagnifyNotification, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSScrollElasticityAutomatic, 0)
        self.assertEqual(NSScrollElasticityNone, 1)
        self.assertEqual(NSScrollElasticityAllowed, 2)
        self.assertEqual(NSScrollViewFindBarPositionAboveHorizontalRuler, 0)
        self.assertEqual(NSScrollViewFindBarPositionAboveContent, 1)
        self.assertEqual(NSScrollViewFindBarPositionBelowContent, 2)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSScrollView.usesPredominantAxisScrolling)
        self.assertArgIsBOOL(NSScrollView.setUsesPredominantAxisScrolling_, 0)
if __name__ == "__main__":
    main()
