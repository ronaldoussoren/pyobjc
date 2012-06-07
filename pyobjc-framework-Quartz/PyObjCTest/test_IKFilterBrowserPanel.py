
from PyObjCTools.TestSupport import *
from Quartz import *

try:
    unicode
except NameError:
    unicode = str

class TestIKFilterBrowserPanel (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgIsSEL(IKFilterBrowserPanel.beginWithOptions_modelessDelegate_didEndSelector_contextInfo_, 2, b"v@:@" + objc._C_NSInteger + b"^v")
        self.assertArgIsSEL(IKFilterBrowserPanel.beginSheetWithOptions_modalForWindow_modalDelegate_didEndSelector_contextInfo_, 3, b"v@:@" + objc._C_NSInteger + b"^v")

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(IKFilterBrowserFilterSelectedNotification, unicode)
        self.assertIsInstance(IKFilterBrowserFilterDoubleClickNotification, unicode)
        self.assertIsInstance(IKFilterBrowserWillPreviewFilterNotification, unicode)
        self.assertIsInstance(IKFilterBrowserShowCategories, unicode)
        self.assertIsInstance(IKFilterBrowserShowPreview, unicode)
        self.assertIsInstance(IKFilterBrowserExcludeCategories, unicode)
        self.assertIsInstance(IKFilterBrowserExcludeFilters, unicode)
        self.assertIsInstance(IKFilterBrowserDefaultInputImage, unicode)

if __name__ == "__main__":
    main()
