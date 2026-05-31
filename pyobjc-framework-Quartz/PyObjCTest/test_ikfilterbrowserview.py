from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestIKFilterBrowserView(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgIsBOOL(Quartz.IKFilterBrowserView.setPreviewState_, 0)
