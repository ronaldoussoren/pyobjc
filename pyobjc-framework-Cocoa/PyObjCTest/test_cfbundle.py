from CoreFoundation import *
from PyObjCTools.TestSupport import *
import Foundation


try:
    long
except NameError:
    long = int


try:
    unicode
except NameError:
    unicode = str

class TestCFBundle (TestCase):

    def testTypes(self):
        self.assertIsCFType(CFBundleRef)

    def testMainBundle(self):
        bundle = CFBundleGetMainBundle()
        self.assertIsInstance(bundle, CFBundleRef)

    def testBundleLoader(self):
        bundle = CFBundleGetBundleWithIdentifier(b"com.apple.CoreFoundation".decode('ascii'))
        self.assertIsInstance(bundle, CFBundleRef)
        array = list(CFBundleGetAllBundles())
        self.assertNotEqual(len(array) , 0)
        for b in array:
            self.assertIsInstance(b, CFBundleRef)
        url = CFURLCreateWithFileSystemPath(None,
                b"/System/Library/Frameworks/Foundation.framework".decode('ascii'), kCFURLPOSIXPathStyle, True)
        bundle = CFBundleCreate(None, url)
        self.assertIsInstance(bundle, CFBundleRef)
        url = CFURLCreateWithFileSystemPath(None, b"/System/Library/Frameworks".decode('ascii'), kCFURLPOSIXPathStyle, True)
        array = CFBundleCreateBundlesFromDirectory(None, url, b"frameworkX".decode('ascii'))
        self.assertEqual(len(array), 0)

        array = CFBundleCreateBundlesFromDirectory(None, url, b"framework".decode('ascii'))
        self.assertNotEquals(len(array), 0)

        array = CFBundleCreateBundlesFromDirectory(None, url, None)
        self.assertNotEquals(len(array), 0)

    def testTypeID(self):
        v = CFBundleGetTypeID()
        self.assertIsInstance(v, (int, long))

    def testInspection(self):
        bundle = CFBundleGetBundleWithIdentifier(b"com.apple.CoreFoundation".decode('ascii'))
        self.assertIsInstance(bundle, CFBundleRef)
        url = CFBundleCopyBundleURL(bundle)
        self.assertIsInstance(url, CFURLRef)
        v = CFBundleGetValueForInfoDictionaryKey(bundle, b"CFBundleIdentifier".decode('ascii'))
        self.assertEqual(v , b"com.apple.CoreFoundation".decode('ascii'))
        v = CFBundleGetInfoDictionary(bundle)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertTrue( v['CFBundleIdentifier'], 'com.apple.CoreFoundation')

        v = CFBundleGetLocalInfoDictionary(bundle)
        if v is not None:
            self.assertIsInstance(v, CFDictionaryRef)
        type, creator = CFBundleGetPackageInfo(bundle, None, None)
        self.assertIsInstance(type, (int, long))
        self.assertIsInstance(creator, (int, long))
        identifier = CFBundleGetIdentifier(bundle)
        self.assertEqual(identifier , b"com.apple.CoreFoundation".decode('ascii'))
        v = CFBundleGetVersionNumber(bundle)
        self.assertIsInstance(v, (int, long))
        v = CFBundleGetDevelopmentRegion(bundle)
        self.assertIsInstance(v, unicode)
        v = CFBundleCopySupportFilesDirectoryURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CFURLRef)
        v = CFBundleCopyResourcesDirectoryURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CFURLRef)
        v = CFBundleCopyPrivateFrameworksURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CFURLRef)
        v = CFBundleCopySharedFrameworksURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CFURLRef)
        v = CFBundleCopySharedSupportURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CFURLRef)
        v = CFBundleCopyBuiltInPlugInsURL(bundle)
        if v is not None:
            self.assertIsInstance(v, CFURLRef)

    def testDirectAccess(self):
        url = CFURLCreateWithFileSystemPath(None,
                b"/System/Library/Frameworks/Foundation.framework".decode('ascii'), kCFURLPOSIXPathStyle, True)

        v = CFBundleCopyInfoDictionaryInDirectory(url)
        self.assertIsInstance(v, CFDictionaryRef)
        self.assertEqual(v[b"CFBundleIdentifier".decode('ascii')] , b"com.apple.Foundation".decode('ascii'))
        ok, type, creator = CFBundleGetPackageInfoInDirectory(url, None, None)
        self.assertIs(ok, True)
        self.assertIsInstance(type, (int, long))
        self.assertIsInstance(creator, (int, long))

    def testResources(self):
        url = CFURLCreateWithFileSystemPath(None,
                b"/System/Library/Frameworks/Foundation.framework".decode('ascii'), kCFURLPOSIXPathStyle, True)
        bundle = CFBundleCreate(None, url)
        self.assertIsInstance(bundle, CFBundleRef)
        url = CFURLCreateWithFileSystemPath(None,
                b"/System/Library/Frameworks/Tcl.framework".decode('ascii'), kCFURLPOSIXPathStyle, True)
        bundle2 = CFBundleCreate(None, url)
        self.assertIsInstance(bundle2, CFBundleRef)
        url = CFBundleCopyResourceURL(bundle, "Formatter", "strings", None)
        self.assertIsInstance(url, CFURLRef)
        url = CFBundleCopyResourceURL(bundle, "Formatter", "strings", "helloworld.lproj")
        self.assertIs(url, None)
        array = CFBundleCopyResourceURLsOfType(bundle, "strings", None)
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CFArrayRef)
        val = CFBundleCopyLocalizedString(bundle, "Err640.f", "value", "FoundationErrors")
        self.assertIsInstance(val, unicode)
        self.assertNotEqual(val , "value")
        CFCopyLocalizedString("python", "error")
        CFCopyLocalizedStringFromTable("pyobjc", "python", "error")
        CFCopyLocalizedStringFromTableInBundle("pyobjc", "python", bundle, "comment")
        CFCopyLocalizedStringWithDefaultValue("pyobjc", "python", bundle, "default", "comment")

        array = CFBundleCopyBundleLocalizations(bundle)
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CFArrayRef)
        arr2 = CFBundleCopyPreferredLocalizationsFromArray(array)
        self.assertIsNot(arr2, None)
        self.assertIsInstance(arr2, CFArrayRef)
        arr2 = CFBundleCopyLocalizationsForPreferences(array, None)
        self.assertIsNot(arr2, None)
        self.assertIsInstance(arr2, CFArrayRef)
        url = CFBundleCopyResourceURLForLocalization(bundle, "Formatter", "strings", None, "Dutch");
        if url is None:
            url = CFBundleCopyResourceURLForLocalization(bundle, "Formatter", "strings", None, "nl");
        if url is None:
            url = CFBundleCopyResourceURLForLocalization(bundle, "Formatter", "strings", None, "en");
        self.assertIsInstance(url, CFURLRef)

        array = CFBundleCopyResourceURLsOfTypeForLocalization(bundle, "strings", None, "Dutch")
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CFArrayRef)
        url = CFBundleCopyExecutableURL(bundle)
        self.assertIsInstance(url, CFURLRef)
        array = CFBundleCopyExecutableArchitectures(bundle)
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CFArrayRef)
        self.assertArgIsOut(CFBundlePreflightExecutable, 1)
        ok, error = CFBundlePreflightExecutable(bundle, None)
        self.assertTrue((ok is True) or (ok is False))
        if ok:
            self.assertIs(error, None)
        else:
            self.assertIsInstance(error, CFErrorRef)
        self.assertArgIsOut(CFBundleLoadExecutableAndReturnError, 1)
        ok, error = CFBundleLoadExecutableAndReturnError(bundle2, None)
        self.assertTrue((ok is True) or (ok is False))
        if ok:
            self.assertIs(error, None)
        else:
            self.assertIsInstance(error, CFErrorRef)
        ok = CFBundleLoadExecutable(bundle2)
        self.assertTrue(ok)

        ok = CFBundleIsExecutableLoaded(bundle2)
        self.assertTrue(ok)

        CFBundleUnloadExecutable(bundle2)
        ok = CFBundleIsExecutableLoaded(bundle2)
        #self.assertFalse(ok)
        ok = CFBundleLoadExecutable(bundle2)
        self.assertTrue(ok)

        try:
            CFBundleGetFunctionPointerForName
        except NameError:
            pass
        else:
            self.fail("CFBundleGetFunctionPointerForName")

        try:
            CFBundleGetFunctionPointersForNames
        except NameError:
            pass
        else:
            self.fail("CFBundleGetFunctionPointersForNames")

        try:
            CFBundleGetDataPointerForName
        except NameError:
            pass
        else:
            self.fail("CFBundleGetDataPointerForName")

        try:
            CFBundleGetDataPointersForNames
        except NameError:
            pass
        else:
            self.fail("CFBundleGetDataPointersForNames")

        url =  CFBundleCopyAuxiliaryExecutableURL(bundle, "Foundation")
        self.assertIsInstance(url, CFURLRef)
        id = CFBundleOpenBundleResourceMap(bundle)
        self.assertIsInstance(id, (int, long))
        CFBundleCloseBundleResourceMap(bundle, id)

        err,  id1, id2 = CFBundleOpenBundleResourceFiles(bundle, None, None)
        self.assertIsInstance(err, (int, long))
        self.assertIsInstance(id1, (int, long))
        self.assertIsInstance(id2, (int, long))
        if id1 != -1:
            CFBundleCloseBundleResourceMap(bundle, id1)
        if id2 != -1:
            CFBundleCloseBundleResourceMap(bundle, id2)

    def testResourcesDirect(self):
        bundle = CFURLCreateWithFileSystemPath(None,
                b"/System/Library/Frameworks/Foundation.framework".decode('ascii'), kCFURLPOSIXPathStyle, True)
        url = CFBundleCopyResourceURLInDirectory(bundle, "Formatter", "strings", None)
        self.assertIsInstance(url, CFURLRef)
        array = CFBundleCopyResourceURLsOfTypeInDirectory(bundle, "strings", None)
        self.assertIsNot(array, None)
        self.assertIsInstance(array, CFArrayRef)
        infoDict = CFBundleCopyInfoDictionaryForURL(bundle)
        self.assertIsInstance(infoDict, CFDictionaryRef)
        array = CFBundleCopyLocalizationsForURL(bundle)
        self.assertIsInstance(array, CFArrayRef)
        array = CFBundleCopyExecutableArchitecturesForURL(bundle)
        self.assertIsInstance(array, CFArrayRef)
        for a in array:
            self.assertIsInstance(a, (int, long))

    def testPlugin(self):
        url = CFURLCreateWithFileSystemPath(None,
                b"/System/Library/Components/AppleScript.component".decode('ascii'), kCFURLPOSIXPathStyle, True)
        bundle = CFBundleCreate(None, url)
        self.assertIsInstance(bundle, CFBundleRef)
        ref = CFBundleGetPlugIn(bundle)
        self.assertIs(ref, None)

    def testConstants(self):
        self.assertIsInstance(kCFBundleInfoDictionaryVersionKey, unicode)
        self.assertIsInstance(kCFBundleExecutableKey, unicode)
        self.assertIsInstance(kCFBundleIdentifierKey, unicode)
        self.assertIsInstance(kCFBundleVersionKey, unicode)
        self.assertIsInstance(kCFBundleDevelopmentRegionKey, unicode)
        self.assertIsInstance(kCFBundleNameKey, unicode)
        self.assertIsInstance(kCFBundleLocalizationsKey, unicode)
        self.assertEqual(kCFBundleExecutableArchitectureI386     , 0x00000007)
        self.assertEqual(kCFBundleExecutableArchitecturePPC      , 0x00000012)
        self.assertEqual(kCFBundleExecutableArchitectureX86_64   , 0x01000007)
        self.assertEqual(kCFBundleExecutableArchitecturePPC64    , 0x01000012)

if __name__ == "__main__":
    main()
