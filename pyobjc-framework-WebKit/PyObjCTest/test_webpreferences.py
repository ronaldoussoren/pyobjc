
from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str

class TestWebPreferences (TestCase):
    def testConstants(self):
        self.assertEqual(WebCacheModelDocumentViewer, 0)
        self.assertEqual(WebCacheModelDocumentBrowser, 1)
        self.assertEqual(WebCacheModelPrimaryWebBrowser, 2)

        self.assertIsInstance(WebPreferencesChangedNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(WebPreferences.userStyleSheetEnabled)
        self.assertArgIsBOOL(WebPreferences.setUserStyleSheetEnabled_, 0)

        self.assertResultIsBOOL(WebPreferences.isJavaEnabled)
        self.assertArgIsBOOL(WebPreferences.setJavaEnabled_, 0)

        self.assertResultIsBOOL(WebPreferences.isJavaScriptEnabled)
        self.assertArgIsBOOL(WebPreferences.setJavaScriptEnabled_, 0)

        self.assertResultIsBOOL(WebPreferences.javaScriptCanOpenWindowsAutomatically)
        self.assertArgIsBOOL(WebPreferences.setJavaScriptCanOpenWindowsAutomatically_, 0)

        self.assertResultIsBOOL(WebPreferences.arePlugInsEnabled)
        self.assertArgIsBOOL(WebPreferences.setPlugInsEnabled_, 0)

        self.assertResultIsBOOL(WebPreferences.allowsAnimatedImages)
        self.assertArgIsBOOL(WebPreferences.setAllowsAnimatedImages_, 0)

        self.assertResultIsBOOL(WebPreferences.allowsAnimatedImageLooping)
        self.assertArgIsBOOL(WebPreferences.setAllowsAnimatedImageLooping_, 0)

        self.assertResultIsBOOL(WebPreferences.loadsImagesAutomatically)
        self.assertArgIsBOOL(WebPreferences.setLoadsImagesAutomatically_, 0)

        self.assertResultIsBOOL(WebPreferences.autosaves)
        self.assertArgIsBOOL(WebPreferences.setAutosaves_, 0)

        self.assertResultIsBOOL(WebPreferences.shouldPrintBackgrounds)
        self.assertArgIsBOOL(WebPreferences.setShouldPrintBackgrounds_, 0)

        self.assertResultIsBOOL(WebPreferences.privateBrowsingEnabled)
        self.assertArgIsBOOL(WebPreferences.setPrivateBrowsingEnabled_, 0)

        self.assertResultIsBOOL(WebPreferences.tabsToLinks)
        self.assertArgIsBOOL(WebPreferences.setTabsToLinks_, 0)

        self.assertResultIsBOOL(WebPreferences.usesPageCache)
        self.assertArgIsBOOL(WebPreferences.setUsesPageCache_, 0)


if __name__ == "__main__":
    main()
