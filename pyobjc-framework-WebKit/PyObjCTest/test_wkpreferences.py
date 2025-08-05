from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKPreferences(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKInactiveSchedulingPolicy)
        self.assertEqual(WebKit.WKInactiveSchedulingPolicySuspend, 0)
        self.assertEqual(WebKit.WKInactiveSchedulingPolicyThrottle, 1)
        self.assertEqual(WebKit.WKInactiveSchedulingPolicyNone, 2)

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

    @min_os_level("12.0")
    def testMethods11_3(self):
        # Documented as available on 11.3, but not present in 11.6...

        self.assertResultIsBOOL(WebKit.WKPreferences.isTextInteractionEnabled)
        self.assertArgIsBOOL(WebKit.WKPreferences.setTextInteractionEnabled_, 0)

    @min_os_level("12.3")
    def testMethods12_3(self):
        self.assertResultIsBOOL(WebKit.WKPreferences.isSiteSpecificQuirksModeEnabled)
        self.assertArgIsBOOL(WebKit.WKPreferences.setSiteSpecificQuirksModeEnabled_, 0)

        self.assertResultIsBOOL(WebKit.WKPreferences.isElementFullscreenEnabled)
        self.assertArgIsBOOL(WebKit.WKPreferences.setElementFullscreenEnabled_, 0)

    @min_os_level("13.3")
    def testMethods13_3(self):
        self.assertResultIsBOOL(WebKit.WKPreferences.shouldPrintBackgrounds)
        self.assertArgIsBOOL(WebKit.WKPreferences.setShouldPrintBackgrounds_, 0)
