import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TesNSScrollView(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSScrollElasticity)
        self.assertIsEnumType(AppKit.NSScrollViewFindBarPosition)

    def test_constants(self):
        self.assertEqual(AppKit.NSScrollElasticityAutomatic, 0)
        self.assertEqual(AppKit.NSScrollElasticityNone, 1)
        self.assertEqual(AppKit.NSScrollElasticityAllowed, 2)

        self.assertEqual(AppKit.NSScrollViewFindBarPositionAboveHorizontalRuler, 0)
        self.assertEqual(AppKit.NSScrollViewFindBarPositionAboveContent, 1)
        self.assertEqual(AppKit.NSScrollViewFindBarPositionBelowContent, 2)

        self.assertIsInstance(AppKit.NSScrollViewWillStartLiveMagnifyNotification, str)
        self.assertIsInstance(AppKit.NSScrollViewDidEndLiveMagnifyNotification, str)

        self.assertIsInstance(AppKit.NSScrollViewWillStartLiveScrollNotification, str)
        self.assertIsInstance(AppKit.NSScrollViewDidLiveScrollNotification, str)
        self.assertIsInstance(AppKit.NSScrollViewDidEndLiveScrollNotification, str)

    def test_methods(self):
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

        self.assertArgIsBOOL(AppKit.NSScrollView.setAllowsMagnification_, 0)
        self.assertResultIsBOOL(AppKit.NSScrollView.allowsMagnification)

        self.assertResultIsBOOL(AppKit.NSScrollView.usesPredominantAxisScrolling)
        self.assertArgIsBOOL(AppKit.NSScrollView.setUsesPredominantAxisScrolling_, 0)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertArgIsBOOL(
            AppKit.NSScrollView.setAutomaticallyAdjustsContentInsets_, 0
        )
        self.assertResultIsBOOL(AppKit.NSScrollView.automaticallyAdjustsContentInsets)

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(AppKit.NSScrollView.isTouchScrollingEnabled)
        self.assertArgIsBOOL(AppKit.NSScrollView.setTouchScrollingEnabled_, 0)
