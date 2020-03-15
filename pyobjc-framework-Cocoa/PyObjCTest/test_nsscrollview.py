import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TesNSScrollView(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            AppKit.NSScrollView.frameSizeForContentSize_hasHorizontalScroller_hasVerticalScroller_borderType_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            AppKit.NSScrollView.frameSizeForContentSize_hasHorizontalScroller_hasVerticalScroller_borderType_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            AppKit.NSScrollView.contentSizeForFrameSize_hasHorizontalScroller_hasVerticalScroller_borderType_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            AppKit.NSScrollView.contentSizeForFrameSize_hasHorizontalScroller_hasVerticalScroller_borderType_,  # noqa: B950
            2,
        )

        self.assertResultIsBOOL(AppKit.NSScrollView.drawsBackground)
        self.assertArgIsBOOL(AppKit.NSScrollView.setDrawsBackground_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.hasVerticalScroller)
        self.assertArgIsBOOL(AppKit.NSScrollView.setHasVerticalScroller_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.hasHorizontalScroller)
        self.assertArgIsBOOL(AppKit.NSScrollView.setHasHorizontalScroller_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.autohidesScrollers)
        self.assertArgIsBOOL(AppKit.NSScrollView.setAutohidesScrollers_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.scrollsDynamically)
        self.assertArgIsBOOL(AppKit.NSScrollView.setScrollsDynamically_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.rulersVisible)
        self.assertArgIsBOOL(AppKit.NSScrollView.setRulersVisible_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.hasHorizontalRuler)
        self.assertArgIsBOOL(AppKit.NSScrollView.setHasHorizontalRuler_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.hasVerticalRuler)
        self.assertArgIsBOOL(AppKit.NSScrollView.setHasVerticalRuler_, 0)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBOOL(
            AppKit.NSScrollView.setAutomaticallyAdjustsContentInsets_, 0
        )
        self.assertResultIsBOOL(AppKit.NSScrollView.automaticallyAdjustsContentInsets)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AppKit.NSScrollViewWillStartLiveScrollNotification, str)
        self.assertIsInstance(AppKit.NSScrollViewDidLiveScrollNotification, str)
        self.assertIsInstance(AppKit.NSScrollViewDidEndLiveScrollNotification, str)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBOOL(AppKit.NSScrollView.setAllowsMagnification_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.allowsMagnification)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(AppKit.NSScrollViewWillStartLiveMagnifyNotification, str)
        self.assertIsInstance(AppKit.NSScrollViewDidEndLiveMagnifyNotification, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSScrollElasticityAutomatic, 0)
        self.assertEqual(AppKit.NSScrollElasticityNone, 1)
        self.assertEqual(AppKit.NSScrollElasticityAllowed, 2)

        self.assertEqual(AppKit.NSScrollViewFindBarPositionAboveHorizontalRuler, 0)
        self.assertEqual(AppKit.NSScrollViewFindBarPositionAboveContent, 1)
        self.assertEqual(AppKit.NSScrollViewFindBarPositionBelowContent, 2)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSScrollView.usesPredominantAxisScrolling)
        self.assertArgIsBOOL(AppKit.NSScrollView.setUsesPredominantAxisScrolling_, 0)
