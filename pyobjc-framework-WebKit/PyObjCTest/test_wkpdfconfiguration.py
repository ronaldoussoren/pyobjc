from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKPDFConfiguration(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.WKPDFConfiguration.allowTransparentBackground)
        self.assertArgIsBOOL(
            WebKit.WKPDFConfiguration.setAllowTransparentBackground_, 0
        )
