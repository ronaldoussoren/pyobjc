from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestIKFilterBrowserPanel(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
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

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.IKFilterBrowserFilterSelectedNotification, str)
        self.assertIsInstance(Quartz.IKFilterBrowserFilterDoubleClickNotification, str)
        self.assertIsInstance(Quartz.IKFilterBrowserWillPreviewFilterNotification, str)
        self.assertIsInstance(Quartz.IKFilterBrowserShowCategories, str)
        self.assertIsInstance(Quartz.IKFilterBrowserShowPreview, str)
        self.assertIsInstance(Quartz.IKFilterBrowserExcludeCategories, str)
        self.assertIsInstance(Quartz.IKFilterBrowserExcludeFilters, str)
        self.assertIsInstance(Quartz.IKFilterBrowserDefaultInputImage, str)
