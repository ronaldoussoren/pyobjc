
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebPreferences (TestCase):
    def testConstants(self):
        self.failUnlessEqual(WebCacheModelDocumentViewer, 0)
        self.failUnlessEqual(WebCacheModelDocumentBrowser, 1)
        self.failUnlessEqual(WebCacheModelPrimaryWebBrowser, 2)

        self.failUnlessIsInstance(WebPreferencesChangedNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(WebPreferences.userStyleSheetEnabled)
        self.failUnlessArgIsBOOL(WebPreferences.setUserStyleSheetEnabled_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.isJavaEnabled)
        self.failUnlessArgIsBOOL(WebPreferences.setJavaEnabled_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.isJavaScriptEnabled)
        self.failUnlessArgIsBOOL(WebPreferences.setJavaScriptEnabled_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.javaScriptCanOpenWindowsAutomatically)
        self.failUnlessArgIsBOOL(WebPreferences.setJavaScriptCanOpenWindowsAutomatically_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.arePlugInsEnabled)
        self.failUnlessArgIsBOOL(WebPreferences.setPlugInsEnabled_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.allowsAnimatedImages)
        self.failUnlessArgIsBOOL(WebPreferences.setAllowsAnimatedImages_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.allowsAnimatedImageLooping)
        self.failUnlessArgIsBOOL(WebPreferences.setAllowsAnimatedImageLooping_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.loadsImagesAutomatically)
        self.failUnlessArgIsBOOL(WebPreferences.setLoadsImagesAutomatically_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.autosaves)
        self.failUnlessArgIsBOOL(WebPreferences.setAutosaves_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.shouldPrintBackgrounds)
        self.failUnlessArgIsBOOL(WebPreferences.setShouldPrintBackgrounds_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.privateBrowsingEnabled)
        self.failUnlessArgIsBOOL(WebPreferences.setPrivateBrowsingEnabled_, 0)

        self.failUnlessResultIsBOOL(WebPreferences.tabsToLinks)
        self.failUnlessArgIsBOOL(WebPreferences.setTabsToLinks_, 0)
        
        self.failUnlessResultIsBOOL(WebPreferences.usesPageCache)
        self.failUnlessArgIsBOOL(WebPreferences.setUsesPageCache_, 0)


if __name__ == "__main__":
    main()
