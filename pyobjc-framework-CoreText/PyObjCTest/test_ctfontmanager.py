from PyObjCTools.TestSupport import *
from CoreText import *

try:
    unicode

except NameError:
    unicode = str

class TestCTFontManager (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCTFontManagerScopeNone, 0)
        self.assertEqual(kCTFontManagerScopeProcess, 1)
        self.assertEqual(kCTFontManagerScopeUser, 2)
        self.assertEqual(kCTFontManagerScopeSession, 3)

        self.assertIsInstance(kCTFontManagerBundleIdentifier, unicode)

        self.assertEqual(kCTFontManagerAutoActivationDefault, 0)
        self.assertEqual(kCTFontManagerAutoActivationDisabled, 1)
        self.assertEqual(kCTFontManagerAutoActivationEnabled, 2)
        self.assertEqual(kCTFontManagerAutoActivationPromptUser, 3)

        self.assertIsInstance(kCTFontManagerRegisteredFontsChangedNotification, unicode)


    @expectedFailure
    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.fail("CTFontManagerCopyAvailablePostScriptNames")
        self.fail("CTFontManagerCopyAvailableFontFamilyNames")
        self.fail("CTFontManagerCopyAvailableFontURLs")
        self.fail("CTFontManagerCompareFontFamilyNames")
        self.fail("CTFontManagerCreateFontDescriptorsFromURL")
        self.fail("CTFontManagerRegisterFontsForURL")
        self.fail("CTFontManagerUnregisterFontsForURL")
        self.fail("CTFontManagerRegisterFontsForURLs")
        self.fail("CTFontManagerUnregisterFontsForURLs")
        self.fail("CTFontManagerEnableFontDescriptors")
        self.fail("CTFontManagerGetScopeForURL")
        self.fail("CTFontManagerIsSupportedFont")
        self.fail("CTFontManagerCreateFontRequestRunLoopSource")
        self.fail("CTFontManagerSetAutoActivationSetting")
        self.fail("CTFontManagerGetAutoActivationSetting")

    @expectedFailure
    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.fail("CTFontManagerCreateFontDescriptorFromData")



    @expectedFailure
    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.fail("CTFontManagerCreateFontDescriptorFromData")
        self.fail("CTFontManagerRegisterGraphicsFont")
        self.fail("CTFontManagerUnregisterGraphicsFont")

if __name__ == "__main__":
    main()
