from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKPreferences(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.WKPreferences.javaScriptEnabled)
        self.assertArgIsBOOL(WebKit.WKPreferences.setJavaScriptEnabled_, 0)
        self.assertResultIsBOOL(
            WebKit.WKPreferences.javaScriptCanOpenWindowsAutomatically
        )
        self.assertArgIsBOOL(
            WebKit.WKPreferences.setJavaScriptCanOpenWindowsAutomatically_, 0
        )
        self.assertResultIsBOOL(WebKit.WKPreferences.javaEnabled)
        self.assertArgIsBOOL(WebKit.WKPreferences.setJavaEnabled_, 0)
        self.assertResultIsBOOL(WebKit.WKPreferences.plugInsEnabled)
        self.assertArgIsBOOL(WebKit.WKPreferences.setPlugInsEnabled_, 0)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(WebKit.WKPreferences.tabFocusesLinks)
        self.assertArgIsBOOL(WebKit.WKPreferences.setTabFocusesLinks_, 0)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(WebKit.WKPreferences.isFraudulentWebsiteWarningEnabled)
        self.assertArgIsBOOL(
            WebKit.WKPreferences.setFraudulentWebsiteWarningEnabled_, 0
        )
