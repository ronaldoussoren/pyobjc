import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCTFontManager(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreText.kCTFontManagerScopeNone, 0)
        self.assertEqual(CoreText.kCTFontManagerScopeProcess, 1)
        self.assertEqual(CoreText.kCTFontManagerScopePersistent, 2)
        self.assertEqual(CoreText.kCTFontManagerScopeSession, 3)
        self.assertEqual(
            CoreText.kCTFontManagerScopeUser, CoreText.kCTFontManagerScopePersistent
        )

        self.assertIsInstance(CoreText.kCTFontManagerBundleIdentifier, str)

        self.assertEqual(CoreText.kCTFontManagerAutoActivationDefault, 0)
        self.assertEqual(CoreText.kCTFontManagerAutoActivationDisabled, 1)
        self.assertEqual(CoreText.kCTFontManagerAutoActivationEnabled, 2)
        self.assertEqual(CoreText.kCTFontManagerAutoActivationPromptUser, 3)

        self.assertIsInstance(
            CoreText.kCTFontManagerRegisteredFontsChangedNotification, str
        )

    @min_os_level("10.6")
    def testFunctions10_6(self):
        self.assertResultIsCFRetained(
            CoreText.CTFontManagerCopyAvailablePostScriptNames
        )
        self.assertResultIsCFRetained(
            CoreText.CTFontManagerCopyAvailableFontFamilyNames
        )
        self.assertResultIsCFRetained(CoreText.CTFontManagerCopyAvailableFontURLs)
        self.assertResultIsCFRetained(
            CoreText.CTFontManagerCreateFontDescriptorsFromURL
        )

        self.assertArgHasType(
            CoreText.CTFontManagerCompareFontFamilyNames, 0, b"^{__CFString=}"
        )
        self.assertArgHasType(
            CoreText.CTFontManagerCompareFontFamilyNames, 1, b"^{__CFString=}"
        )
        self.assertArgHasType(CoreText.CTFontManagerCompareFontFamilyNames, 2, b"^v")
        self.assertArgIsOut(CoreText.CTFontManagerRegisterFontsForURL, 2)
        self.assertArgIsOut(CoreText.CTFontManagerUnregisterFontsForURL, 2)
        self.assertArgIsOut(CoreText.CTFontManagerRegisterFontsForURLs, 2)
        self.assertArgIsOut(CoreText.CTFontManagerUnregisterFontsForURLs, 2)
        self.assertArgHasType(
            CoreText.CTFontManagerEnableFontDescriptors, 1, objc._C_BOOL
        )
        CoreText.CTFontManagerGetScopeForURL  # Test that function exists
        self.assertResultHasType(CoreText.CTFontManagerIsSupportedFont, objc._C_BOOL)
        self.assertResultIsCFRetained(
            CoreText.CTFontManagerCreateFontRequestRunLoopSource
        )
        self.assertArgIsBlock(
            CoreText.CTFontManagerCreateFontRequestRunLoopSource, 1, b"@@i"
        )

        CoreText.CTFontManagerGetAutoActivationSetting
        CoreText.CTFontManagerSetAutoActivationSetting

    @min_os_level("10.7")
    def testFunctions10_7(self):
        self.assertResultIsCFRetained(
            CoreText.CTFontManagerCreateFontDescriptorFromData
        )

    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertResultIsCFRetained(
            CoreText.CTFontManagerCreateFontDescriptorFromData
        )
        self.assertArgIsOut(CoreText.CTFontManagerRegisterGraphicsFont, 1)
        self.assertArgIsOut(CoreText.CTFontManagerUnregisterGraphicsFont, 1)

    @min_os_level("10.13")
    def testFunctions10_13(self):
        self.assertResultIsCFRetained(
            CoreText.CTFontManagerCreateFontDescriptorsFromData
        )

    @min_os_level("10.15")
    def testFunctions10_15(self):
        self.assertArgIsBlock(
            CoreText.CTFontManagerRegisterFontURLs,
            3,
            objc._C_BOOL + objc._C_ID + objc._C_BOOL,
        )
        self.assertArgIsBlock(
            CoreText.CTFontManagerUnregisterFontURLs,
            2,
            objc._C_BOOL + objc._C_ID + objc._C_BOOL,
        )
        self.assertArgIsBlock(
            CoreText.CTFontManagerRegisterFontDescriptors,
            3,
            objc._C_BOOL + objc._C_ID + objc._C_BOOL,
        )
        self.assertArgIsBlock(
            CoreText.CTFontManagerUnregisterFontDescriptors,
            2,
            objc._C_BOOL + objc._C_ID + objc._C_BOOL,
        )
