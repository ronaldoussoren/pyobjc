import CoreFoundation
from PyObjCTools.TestSupport import TestCase, os_level_key, os_release, min_os_level


class TestCFBundle(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFBundleRef)

    def testMainBundle(self):
        bundle = CoreFoundation.CFBundleGetMainBundle()
        self.assertIsInstance(bundle, CoreFoundation.CFBundleRef)

    def testBundleLoader(self):
        bundle = CoreFoundation.CFBundleGetBundleWithIdentifier(
            "com.apple.CoreFoundation"
        )
        self.assertIsInstance(bundle, CoreFoundation.CFBundleRef)
        array = list(CoreFoundation.CFBundleGetAllBundles())
        self.assertNotEqual(len(array), 0)
        for b in array:
            self.assertIsInstance(b, CoreFoundation.CFBundleRef)
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None,
            "/System/Library/Frameworks/Foundation.framework",
            CoreFoundation.kCFURLPOSIXPathStyle,
            True,
        )
        bundle = CoreFoundation.CFBundleCreate(None, url)
        self.assertIsInstance(bundle, CoreFoundation.CFBundleRef)
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None,
            "/System/Library/Frameworks",
            CoreFoundation.kCFURLPOSIXPathStyle,
            True,
        )
        array = CoreFoundation.CFBundleCreateBundlesFromDirectory(
            None, url, "frameworkX"
        )
        self.assertEqual(len(array), 0)

        array = CoreFoundation.CFBundleCreateBundlesFromDirectory(
            None, url, "framework"
        )
        self.assertNotEqual(len(array), 0)

        array = CoreFoundation.CFBundleCreateBundlesFromDirectory(None, url, None)
        self.assertNotEqual(len(array), 0)

    def testTypeID(self):
        v = CoreFoundation.CFBundleGetTypeID()
        self.assertIsInstance(v, int)

    def testInspection(self):
        bundle = CoreFoundation.CFBundleGetBundleWithIdentifier(
            "com.apple.CoreFoundation"
        )
        self.assertIsInstance(bundle, CoreFoundation.CFBundleRef)
        url = CoreFoundation.CFBundleCopyBundleURL(bundle)
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        v = CoreFoundation.CFBundleGetValueForInfoDictionaryKey(
            bundle, "CFBundleIdentifier"
        )
        self.assertEqual(v, "com.apple.CoreFoundation")
        v = CoreFoundation.CFBundleGetInfoDictionary(bundle)
        self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)
        self.assertTrue(v["CFBundleIdentifier"], "com.apple.CoreFoundation")

        v = CoreFoundation.CFBundleGetLocalInfoDictionary(bundle)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)
        package_type, creator = CoreFoundation.CFBundleGetPackageInfo(
            bundle, None, None
        )
        self.assertIsInstance(package_type, int)
        self.assertIsInstance(creator, int)
        identifier = CoreFoundation.CFBundleGetIdentifier(bundle)
        self.assertEqual(identifier, "com.apple.CoreFoundation")
        v = CoreFoundation.CFBundleGetVersionNumber(bundle)
        self.assertIsInstance(v, int)
        v = CoreFoundation.CFBundleGetDevelopmentRegion(bundle)
        self.assertIsInstance(v, str)
        v = CoreFoundation.CFBundleCopySupportFilesDirectoryURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFURLRef)
        v = CoreFoundation.CFBundleCopyResourcesDirectoryURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFURLRef)
        v = CoreFoundation.CFBundleCopyPrivateFrameworksURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFURLRef)
        v = CoreFoundation.CFBundleCopySharedFrameworksURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFURLRef)
        v = CoreFoundation.CFBundleCopySharedSupportURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFURLRef)
        v = CoreFoundation.CFBundleCopyBuiltInPlugInsURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CoreFoundation.CFURLRef)

    def testDirectAccess(self):
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None,
            "/System/Library/Frameworks/Foundation.framework",
            CoreFoundation.kCFURLPOSIXPathStyle,
            True,
        )

        v = CoreFoundation.CFBundleCopyInfoDictionaryInDirectory(url)
        self.assertIsInstance(v, CoreFoundation.CFDictionaryRef)
        self.assertEqual(v["CFBundleIdentifier"], "com.apple.Foundation")
        ok, bundle_type, creator = CoreFoundation.CFBundleGetPackageInfoInDirectory(
            url, None, None
        )
        self.assertIs(ok, True)
        self.assertIsInstance(bundle_type, int)
        self.assertIsInstance(creator, int)

    def testResources(self):
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None,
            "/System/Library/Frameworks/Foundation.framework",
            CoreFoundation.kCFURLPOSIXPathStyle,
            True,
        )
        bundle = CoreFoundation.CFBundleCreate(None, url)
        self.assertIsInstance(bundle, CoreFoundation.CFBundleRef)
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None,
            "/System/Library/Frameworks/Tcl.framework",
            CoreFoundation.kCFURLPOSIXPathStyle,
            True,
        )
        bundle2 = CoreFoundation.CFBundleCreate(None, url)
        self.assertIsInstance(bundle2, CoreFoundation.CFBundleRef)
        url = CoreFoundation.CFBundleCopyResourceURL(
            bundle, "Formatter", "strings", None
        )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        url = CoreFoundation.CFBundleCopyResourceURL(
            bundle, "Formatter", "strings", "helloworld.lproj"
        )
        self.assertIs(url, None)
        array = CoreFoundation.CFBundleCopyResourceURLsOfType(bundle, "strings", None)
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CoreFoundation.CFArrayRef)
        val = CoreFoundation.CFBundleCopyLocalizedString(
            bundle, "Err640.f", "value", "FoundationErrors"
        )
        self.assertIsInstance(val, str)
        self.assertNotEqual(val, "value")
        CoreFoundation.CFCopyLocalizedString("python", "error")
        CoreFoundation.CFCopyLocalizedStringFromTable("pyobjc", "python", "error")
        CoreFoundation.CFCopyLocalizedStringFromTableInBundle(
            "pyobjc", "python", bundle, "comment"
        )
        CoreFoundation.CFCopyLocalizedStringWithDefaultValue(
            "pyobjc", "python", bundle, "default", "comment"
        )

        array = CoreFoundation.CFBundleCopyBundleLocalizations(bundle)
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CoreFoundation.CFArrayRef)
        arr2 = CoreFoundation.CFBundleCopyPreferredLocalizationsFromArray(array)
        self.assertIsNot(arr2, None)
        self.assertIsInstance(arr2, CoreFoundation.CFArrayRef)
        arr2 = CoreFoundation.CFBundleCopyLocalizationsForPreferences(array, None)
        self.assertIsNot(arr2, None)
        self.assertIsInstance(arr2, CoreFoundation.CFArrayRef)
        url = CoreFoundation.CFBundleCopyResourceURLForLocalization(
            bundle, "Formatter", "strings", None, "Dutch"
        )
        if url is None:
            url = CoreFoundation.CFBundleCopyResourceURLForLocalization(
                bundle, "Formatter", "strings", None, "nl"
            )
        if url is None:
            url = CoreFoundation.CFBundleCopyResourceURLForLocalization(
                bundle, "Formatter", "strings", None, "en"
            )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)

        array = CoreFoundation.CFBundleCopyResourceURLsOfTypeForLocalization(
            bundle, "strings", None, "Dutch"
        )
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CoreFoundation.CFArrayRef)
        url = CoreFoundation.CFBundleCopyExecutableURL(bundle)
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        array = CoreFoundation.CFBundleCopyExecutableArchitectures(bundle)
        if os_level_key(os_release()) >= os_level_key("11.0"):
            self.assertIs(array, None)
        else:
            self.assertIsNot(array, None)
            self.assertIsInstance(array, CoreFoundation.CFArrayRef)
        self.assertArgIsOut(CoreFoundation.CFBundlePreflightExecutable, 1)
        ok, error = CoreFoundation.CFBundlePreflightExecutable(bundle, None)
        self.assertTrue((ok is True) or (ok is False))
        if ok:
            self.assertIs(error, None)
        else:
            self.assertIsInstance(error, CoreFoundation.CFErrorRef)
        self.assertArgIsOut(CoreFoundation.CFBundleLoadExecutableAndReturnError, 1)
        ok, error = CoreFoundation.CFBundleLoadExecutableAndReturnError(bundle2, None)
        self.assertTrue((ok is True) or (ok is False))
        if ok:
            self.assertIs(error, None)
        else:
            self.assertIsInstance(error, CoreFoundation.CFErrorRef)
        ok = CoreFoundation.CFBundleLoadExecutable(bundle2)
        self.assertTrue(ok)

        ok = CoreFoundation.CFBundleIsExecutableLoaded(bundle2)
        self.assertTrue(ok)

        CoreFoundation.CFBundleUnloadExecutable(bundle2)
        ok = CoreFoundation.CFBundleIsExecutableLoaded(bundle2)
        # self.assertFalse(ok)
        ok = CoreFoundation.CFBundleLoadExecutable(bundle2)
        self.assertTrue(ok)

        try:
            CoreFoundation.CFBundleGetFunctionPointerForName
        except AttributeError:
            pass
        else:
            self.fail("CFBundleGetFunctionPointerForName")

        try:
            CoreFoundation.CFBundleGetFunctionPointersForNames
        except AttributeError:
            pass
        else:
            self.fail("CFBundleGetFunctionPointersForNames")

        try:
            CoreFoundation.CFBundleGetDataPointerForName
        except AttributeError:
            pass
        else:
            self.fail("CFBundleGetDataPointerForName")

        try:
            CoreFoundation.CFBundleGetDataPointersForNames
        except AttributeError:
            pass
        else:
            self.fail("CFBundleGetDataPointersForNames")

        url = CoreFoundation.CFBundleCopyAuxiliaryExecutableURL(bundle, "Foundation")
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        map_id = CoreFoundation.CFBundleOpenBundleResourceMap(bundle)
        self.assertIsInstance(map_id, int)
        CoreFoundation.CFBundleCloseBundleResourceMap(bundle, map_id)

        err, id1, id2 = CoreFoundation.CFBundleOpenBundleResourceFiles(
            bundle, None, None
        )
        self.assertIsInstance(err, int)
        self.assertIsInstance(id1, int)
        self.assertIsInstance(id2, int)
        if id1 != -1:
            CoreFoundation.CFBundleCloseBundleResourceMap(bundle, id1)
        if id2 != -1:
            CoreFoundation.CFBundleCloseBundleResourceMap(bundle, id2)

    def testResourcesDirect(self):
        bundle = CoreFoundation.CFURLCreateWithFileSystemPath(
            None,
            "/System/Library/Frameworks/Foundation.framework",
            CoreFoundation.kCFURLPOSIXPathStyle,
            True,
        )
        url = CoreFoundation.CFBundleCopyResourceURLInDirectory(
            bundle, "Formatter", "strings", None
        )
        self.assertIsInstance(url, CoreFoundation.CFURLRef)
        array = CoreFoundation.CFBundleCopyResourceURLsOfTypeInDirectory(
            bundle, "strings", None
        )
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CoreFoundation.CFArrayRef)
        infoDict = CoreFoundation.CFBundleCopyInfoDictionaryForURL(bundle)
        self.assertIsInstance(infoDict, CoreFoundation.CFDictionaryRef)
        array = CoreFoundation.CFBundleCopyLocalizationsForURL(bundle)
        self.assertIsInstance(array, CoreFoundation.CFArrayRef)
        array = CoreFoundation.CFBundleCopyExecutableArchitecturesForURL(bundle)
        if os_level_key(os_release()) >= os_level_key("11.0"):
            self.assertIs(array, None)
        else:
            self.assertIsInstance(array, CoreFoundation.CFArrayRef)
            for a in array:
                self.assertIsInstance(a, int)

    def testPlugin(self):
        url = CoreFoundation.CFURLCreateWithFileSystemPath(
            None,
            "/System/Library/Components/AppleScript.component",
            CoreFoundation.kCFURLPOSIXPathStyle,
            True,
        )
        bundle = CoreFoundation.CFBundleCreate(None, url)
        self.assertIsInstance(bundle, CoreFoundation.CFBundleRef)
        ref = CoreFoundation.CFBundleGetPlugIn(bundle)
        self.assertIs(ref, None)

    def testConstants(self):
        self.assertIsInstance(CoreFoundation.kCFBundleInfoDictionaryVersionKey, str)
        self.assertIsInstance(CoreFoundation.kCFBundleExecutableKey, str)
        self.assertIsInstance(CoreFoundation.kCFBundleIdentifierKey, str)
        self.assertIsInstance(CoreFoundation.kCFBundleVersionKey, str)
        self.assertIsInstance(CoreFoundation.kCFBundleDevelopmentRegionKey, str)
        self.assertIsInstance(CoreFoundation.kCFBundleNameKey, str)
        self.assertIsInstance(CoreFoundation.kCFBundleLocalizationsKey, str)
        self.assertEqual(CoreFoundation.kCFBundleExecutableArchitectureI386, 0x00000007)
        self.assertEqual(CoreFoundation.kCFBundleExecutableArchitecturePPC, 0x00000012)
        self.assertEqual(
            CoreFoundation.kCFBundleExecutableArchitectureX86_64, 0x01000007
        )
        self.assertEqual(
            CoreFoundation.kCFBundleExecutableArchitecturePPC64, 0x01000012
        )
        self.assertEqual(
            CoreFoundation.kCFBundleExecutableArchitectureARM64, 0x0100000C
        )

    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertResultIsBOOL(CoreFoundation.CFBundleIsExecutableLoadable)
        self.assertResultIsBOOL(CoreFoundation.CFBundleIsExecutableLoadableForURL)
        self.assertResultIsBOOL(CoreFoundation.CFBundleIsArchitectureLoadable)
