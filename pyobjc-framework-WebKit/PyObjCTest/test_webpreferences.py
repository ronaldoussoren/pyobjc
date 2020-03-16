from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWebPreferences(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.WebCacheModelDocumentViewer, 0)
        self.assertEqual(WebKit.WebCacheModelDocumentBrowser, 1)
        self.assertEqual(WebKit.WebCacheModelPrimaryWebBrowser, 2)

        self.assertIsInstance(WebKit.WebPreferencesChangedNotification, str)

    def testMethods(self):
        self.assertResultIsBOOL(WebKit.WebPreferences.userStyleSheetEnabled)
        self.assertArgIsBOOL(WebKit.WebPreferences.setUserStyleSheetEnabled_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.isJavaEnabled)
        self.assertArgIsBOOL(WebKit.WebPreferences.setJavaEnabled_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.isJavaScriptEnabled)
        self.assertArgIsBOOL(WebKit.WebPreferences.setJavaScriptEnabled_, 0)

        self.assertResultIsBOOL(
            WebKit.WebPreferences.javaScriptCanOpenWindowsAutomatically
        )
        self.assertArgIsBOOL(
            WebKit.WebPreferences.setJavaScriptCanOpenWindowsAutomatically_, 0
        )

        self.assertResultIsBOOL(WebKit.WebPreferences.arePlugInsEnabled)
        self.assertArgIsBOOL(WebKit.WebPreferences.setPlugInsEnabled_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.allowsAnimatedImages)
        self.assertArgIsBOOL(WebKit.WebPreferences.setAllowsAnimatedImages_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.allowsAnimatedImageLooping)
        self.assertArgIsBOOL(WebKit.WebPreferences.setAllowsAnimatedImageLooping_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.loadsImagesAutomatically)
        self.assertArgIsBOOL(WebKit.WebPreferences.setLoadsImagesAutomatically_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.autosaves)
        self.assertArgIsBOOL(WebKit.WebPreferences.setAutosaves_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.shouldPrintBackgrounds)
        self.assertArgIsBOOL(WebKit.WebPreferences.setShouldPrintBackgrounds_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.privateBrowsingEnabled)
        self.assertArgIsBOOL(WebKit.WebPreferences.setPrivateBrowsingEnabled_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.tabsToLinks)
        self.assertArgIsBOOL(WebKit.WebPreferences.setTabsToLinks_, 0)

        self.assertResultIsBOOL(WebKit.WebPreferences.usesPageCache)
        self.assertArgIsBOOL(WebKit.WebPreferences.setUsesPageCache_, 0)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(WebKit.WebPreferences.suppressesIncrementalRendering)
        self.assertArgIsBOOL(
            WebKit.WebPreferences.setSuppressesIncrementalRendering_, 0
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(WebKit.WebPreferences.allowsAirPlayForMediaPlayback)
        self.assertArgIsBOOL(WebKit.WebPreferences.setAllowsAirPlayForMediaPlayback_, 0)
