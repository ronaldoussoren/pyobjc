from PyObjCTools.TestSupport import TestCase
import Quartz


class TestIKFilterBrowserView(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(Quartz.IKFilterBrowserView.setPreviewState_, 0)
