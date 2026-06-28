from PyObjCTools.TestSupport import TestCase
import Quartz
import objc


class TestIKFilterBrowserPanel(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.IKFilterBrowserFilterSelectedNotification, str)
        self.assertIsInstance(Quartz.IKFilterBrowserFilterDoubleClickNotification, str)
        self.assertIsInstance(Quartz.IKFilterBrowserWillPreviewFilterNotification, str)
        self.assertIsInstance(Quartz.IKFilterBrowserShowCategories, str)
        self.assertIsInstance(Quartz.IKFilterBrowserShowPreview, str)
        self.assertIsInstance(Quartz.IKFilterBrowserExcludeCategories, str)
        self.assertIsInstance(Quartz.IKFilterBrowserExcludeFilters, str)
        self.assertIsInstance(Quartz.IKFilterBrowserDefaultInputImage, str)

    def test_methods(self):
        self.assertArgIsSEL(
            Quartz.IKFilterBrowserPanel.beginWithOptions_modelessDelegate_didEndSelector_contextInfo_,
            2,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
        self.assertArgIsSEL(
            Quartz.IKFilterBrowserPanel.beginSheetWithOptions_modalForWindow_modalDelegate_didEndSelector_contextInfo_,
            3,
            b"v@:@" + objc._C_NSInteger + b"^v",
        )
